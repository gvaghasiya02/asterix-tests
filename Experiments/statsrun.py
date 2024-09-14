import requests
import pandas as pd
import os

import requests
import csv
import json

url = "http://localhost:19002/query/service"

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

import subprocess

def copy_content_and_clear(remote_path, local_path, remote_host, remote_user):
    try:
        # Step 1: Clear the destination file
        with open(local_path, 'w') as f:
            f.truncate()

        # Step 2: Copy contents from remote file to local file
        print(remote_path)
        scp_command = f"sshpass -p 'dbis2023' scp {remote_user}@{remote_host}:{remote_path} {local_path}"
        subprocess.run(scp_command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Content copied successfully.")
        # print("yyggggggg")
        # with open(local_path, 'r') as f:
        #     ss=f.readlines()
        #     print(ss)

        # Step 3: Clear the contents of the original file on the remote host
        clear_command = f"sshpass -p 'dbis2023' ssh {remote_user}@{remote_host} 'cat /dev/null > {remote_path}'"
        subprocess.run(clear_command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Original file contents cleared successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error during operations: {e.stderr}")

# Example usage


def consolidate_logs(local_log_path, remote_log_path, output_path):
    copy_content_and_clear(remote_log_path, output_path, '10.16.229.106', 'dbis-nuc06')
    with open(output_path, 'a') as outfile:
        # Local log
        with open(local_log_path, 'r') as infile:
            outfile.write(infile.read())

        open(local_log_path, 'w').close()
    # with open(output_path, 'r') as f:
    #         ss=f.readlines()
    #         print(ss)

def process_log_file(filepath):
    processed_records = 0
    processed_frames = 0
    spilled_data_bytes = 0
    sorttuplecount = 0
    totalcomp = 0
    aggregated_records_spill_to_network=0

    with open(filepath, 'r') as file:
        for line in file:
            if "Closing to OptimizeGroupWriter" in line:
                parts = line.split()
                processed_records += int(parts[parts.index("records") + 1])
                processed_frames += int(parts[parts.index("aggregated") - 1][6:])
                aggregated_records_spill_to_network += int(parts[parts.index("Closing") - 1])

            if "bytes to /home" in line:
                parts = line.split()
                spilled_data_bytes += int(parts[parts.index("bytes") - 1])

            if "Sorting Tuple References" in line and "Total Comparisions" in line:
                parts = line.split()
                sorttuplecount += int(parts[parts.index("References") + 1])
                totalcomp += int(parts[parts.index("Comparisions") + 1])

    # print(spilled_data_bytes,processed_frames,processed_records)
    return {
        "spilled_data_bytes": spilled_data_bytes,
        "processed_frames": processed_frames,
        "processed_records": processed_records,
        "sorttuplecount": sorttuplecount,
        "totalcomp": totalcomp,
        "aggregated_records_spill_to_network":aggregated_records_spill_to_network
    }


def main():
    queries_path = 'queries.txt'
    output_log_path = 'path_to_log_file.txt'
    local_log_path = '/home/dbis-nuc10/asterixdb/logs/nc-1.log'
    remote_log_path = '/home/dbis-nuc06/asterixdb/logs/nc-2.log'  # Adjust this path as needed

    results = []
    queries = read_queries(queries_path)
    for query in queries:
        querydata["statement"] = query.strip()       
        response=requests.post(url, headers=headers, data=querydata)
        consolidate_logs(local_log_path, remote_log_path, output_log_path)
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
