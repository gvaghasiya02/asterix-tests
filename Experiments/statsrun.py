import requests
import pandas as pd
import os
import csv
import json
import subprocess

url = "http://10.16.229.110:19002/query/service"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Function to read queries from a text file
def read_queries(filename):
    with open(filename, 'r') as file:
        queries = file.readlines()
    return queries

querydata = {
    "statement": "SET `compiler.optimize.groupby` 'false';USE wiscon106; SELECT ten, COUNT(ten) AS count FROM wiscondef106 GROUP BY wiscondef106.ten;",
    "pretty": "true",
    "client_context_id": "xyz"
}


def consolidate_logs(local_log_path, remote_log_path, output_log_path, remote_host, remote_user):
    try:
        # Step 1: Clear the destination file
        with open(output_log_path, 'w') as f:
            f.truncate()

        # Step 2: Copy contents from remote file to local file
        print(remote_log_path)
        scp_command = f"sshpass -p 'dbis2023' scp {remote_user}@{remote_host}:{remote_log_path} {output_log_path}"
        subprocess.run(scp_command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Content copied successfully.")

        # Step 3: Clear the contents of the original file on the remote host
        clear_command = f"sshpass -p 'dbis2023' ssh {remote_user}@{remote_host} 'cat /dev/null > {remote_log_path}'"
        subprocess.run(clear_command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Original file contents cleared successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error during operations: {e.stderr}")

    with open(output_log_path, 'a') as outfile:
        # Local log
        with open(local_log_path, 'r') as infile:
            outfile.write(infile.read())

        open(local_log_path, 'w').close()

def process_log_file(filepath):
    processed_records = 0
    processed_frames = 0
    spilled_data_bytes = 0
    sorttuplecount = 0
    totalcomp = 0
    aggregated_records_spill_to_network=0
    collected_frames=0
    timetocollect=0

    with open(filepath, 'r') as file:
        for line in file:
            if "Closing to OptimizeGroupWriter" in line:
                parts = line.split()
                processed_records += int(parts[parts.index("processedRecords") + 1])
                processed_frames += int(parts[parts.index("processedFrames") + 1])
                aggregated_records_spill_to_network += int(parts[parts.index("aggregatedRecords") + 1])

            if "bytes to /home" in line:
                parts = line.split()
                spilled_data_bytes += int(parts[parts.index("bytes") - 1])

            if "Sorting Tuple References" in line and "Total Comparisions" in line:
                parts = line.split()
                sorttuplecount += int(parts[parts.index("References") + 1])
                totalcomp += int(parts[parts.index("Comparisions") + 1])

            if "Garbage Collection" in line and "Hash table" in line:
                parts = line.split()
                collected_frames += int(parts[parts.index("Deallocated") + 1][7:])
                timetocollect += int(parts[parts.index("time") + 1])

    # print(spilled_data_bytes,processed_frames,processed_records)
    return {
        "spilled_data_bytes": spilled_data_bytes,
        "processed_frames": processed_frames,
        "processed_records": processed_records,
        "sorttuplecount": sorttuplecount,
        "totalcomp": totalcomp,
        "aggregated_records_spill_to_network":aggregated_records_spill_to_network,
        "Collected_garbage_frames":collected_frames,
        "Time_collect_garbage_frames":timetocollect
    }


def main():
    queries_path = 'queries.txt'
    output_log_path = 'path_to_log_file.txt'
    local_log_path = '/home/dbis-nuc10/asterixdb/logs/nc-1.log'
    remote_log_path = '/home/dbis-nuc06/asterixdb/logs/nc-2.log'
    remote_host = '10.16.229.106'
    remote_user = 'dbis-nuc06'

    results = []
    queries = read_queries(queries_path)
    for query in queries:
        querydata["statement"] = query.strip()       
        response=requests.post(url, headers=headers, data=querydata)
        consolidate_logs(local_log_path, remote_log_path, output_log_path, remote_host, remote_user)
        result = process_log_file(output_log_path)
        result['statement'] = query.strip()
        results.append(result)
        # Clear the contents of the output log file
        open(output_log_path, 'w').close()
        df = pd.DataFrame(results)

        df.to_csv('stats.csv', index=False)

    # df = pd.DataFrame(results)

    # df.to_csv('ll.csv', index=False)  # Save the DataFrame to a CSV file

if __name__ == "__main__":
    main()
