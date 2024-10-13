import requests
import pandas as pd
import os
import csv
import json
import subprocess

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

fillerdata= {
    "statement": "USE filler; SELECT COUNT(*) FROM wisconfiller;",
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
    stats_by_thread = {}

    with open(filepath, 'r') as file:
        for line in file:
            if "Closing to OptimizeGroupWriter" in line:
                parts = line.split()
                thread = int(parts[parts.index("SA:JID") + 1].split(":")[-1])  # Extract thread ID
                processed_records = int(parts[parts.index("records") + 1])
                processed_frames = int(parts[parts.index("aggregated") - 1][6:])
                aggregated_records_spill_to_network = int(parts[parts.index("Closing") - 1])

                if thread not in stats_by_thread:
                    stats_by_thread[thread] = {
                        "spilled_data_bytes": 0,
                        "processed_frames": 0,
                        "processed_records": 0,
                        "sorttuplecount": 0,
                        "totalcomp": 0,
                        "aggregated_records_spill_to_network": 0,
                        "Collected_garbage_frames": 0,
                        "Time_collect_garbage_frames": 0
                    }

                stats_by_thread[thread]["processed_records"] += processed_records
                stats_by_thread[thread]["processed_frames"] += processed_frames
                stats_by_thread[thread]["aggregated_records_spill_to_network"] += aggregated_records_spill_to_network

            if "bytes to /home" in line:
                parts = line.split()
                spilled_data_bytes = int(parts[parts.index("bytes") - 1])
                thread = int(parts[parts.index("Written") - 1])

                if thread not in stats_by_thread:
                    stats_by_thread[thread] = {
                        "spilled_data_bytes": 0,
                        "processed_frames": 0,
                        "processed_records": 0,
                        "sorttuplecount": 0,
                        "totalcomp": 0,
                        "aggregated_records_spill_to_network": 0,
                        "Collected_garbage_frames": 0,
                        "Time_collect_garbage_frames": 0
                    }

                stats_by_thread[thread]["spilled_data_bytes"] += spilled_data_bytes

            if "Sorting Tuple References" in line and "Total Comparisions" in line:
                parts = line.split()
                sorttuplecount = int(parts[parts.index("References") + 1])
                totalcomp = int(parts[parts.index("Comparisions") + 1])
                thread = int(parts[parts.index("SA:JID") + 1].split(":")[-1])  # Extract thread ID

                if thread not in stats_by_thread:
                    stats_by_thread[thread] = {
                        "spilled_data_bytes": 0,
                        "processed_frames": 0,
                        "processed_records": 0,
                        "sorttuplecount": 0,
                        "totalcomp": 0,
                        "aggregated_records_spill_to_network": 0,
                        "Collected_garbage_frames": 0,
                        "Time_collect_garbage_frames": 0
                    }

                stats_by_thread[thread]["sorttuplecount"] += sorttuplecount
                stats_by_thread[thread]["totalcomp"] += totalcomp

            if "Garbage Collection" in line and "Hash table" in line:
                parts = line.split()
                collected_frames = int(parts[parts.index("Deallocated") + 1][7:])
                timetocollect = int(parts[parts.index("time") + 1])
                thread = thread=int(parts[parts.index("Garbage") - 1])

                if thread not in stats_by_thread:
                    stats_by_thread[thread] = {
                        "spilled_data_bytes": 0,
                        "processed_frames": 0,
                        "processed_records": 0,
                        "sorttuplecount": 0,
                        "totalcomp": 0,
                        "aggregated_records_spill_to_network": 0,
                        "Collected_garbage_frames": 0,
                        "Time_collect_garbage_frames": 0
                    }

                stats_by_thread[thread]["Collected_garbage_frames"] += collected_frames
                stats_by_thread[thread]["Time_collect_garbage_frames"] += timetocollect

    return stats_by_thread



def main():
    queries_path = 'queries.txt'
    output_log_path = 'path_to_log_file.txt'
    local_log_path = '/home/dbis-nuc07/asterixdb/logs/nc-1.log'
    remote_log_path = '/home/dbis-nuc05/asterixdb/logs/nc-2.log'
    remote_host = '10.16.229.105'
    remote_user = 'dbis-nuc05'

    results = []
    queries = read_queries(queries_path)
    for query in queries:
        querydata["statement"] = query.strip()       
        response=requests.post(url, headers=headers, data=querydata)
        consolidate_logs(local_log_path, remote_log_path, output_log_path, remote_host, remote_user)
        result = process_log_file(output_log_path)
        results.append(result)
        # Clear the contents of the output log file
        open(output_log_path, 'w').close()
        df = pd.DataFrame(results)

        df.to_csv('stats.csv', index=False)

    # df = pd.DataFrame(results)

    # df.to_csv('ll.csv', index=False)  # Save the DataFrame to a CSV file

if __name__ == "__main__":
    main()
