import pandas as pd
import ast
import requests
import pandas as pd
import os
import csv
import json
import subprocess

def reformat_csv(input_csv, output_csv):
    # Read the CSV into a DataFrame
    df = pd.read_csv(input_csv, header=None)
    
    # First row is thread IDs, second row is dictionary strings containing stats
    thread_ids = df.iloc[0, :].tolist()
    stats_strings = df.iloc[1, :].tolist()

    # Initialize a dictionary to store stats keyed by stat name
    reformatted_data = {}

    # Process each thread's stats
    for thread_id, stats_str in zip(thread_ids, stats_strings):
        # Parse the dictionary-like string into a real dictionary
        stats_dict = ast.literal_eval(stats_str)
        
        # Add each stat to the reformatted_data dictionary
        for stat_key, stat_value in stats_dict.items():
            if stat_key not in reformatted_data:
                reformatted_data[stat_key] = {}
            reformatted_data[stat_key][thread_id] = stat_value

    # Convert the reformatted_data dictionary to a DataFrame
    reformatted_df = pd.DataFrame(reformatted_data).transpose()
    
    # Reorder columns so that they match the thread IDs sequence
    reformatted_df = reformatted_df[thread_ids]

    # Save the reformatted DataFrame to a new CSV file
    reformatted_df.to_csv(output_csv)

def process_log_file(filepath):
    stats_by_thread = {}

    with open(filepath, 'r') as file:
        for line in file:
            if "Closing to OptimizeGroupWriter" in line:
                parts = line.split()
                thread = parts[1]  # Extract thread ID
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
                thread = parts[1]

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
                thread = parts[1]

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
                thread = parts[1]

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

if __name__ == "__main__":
    results=[]
    result = process_log_file('/home/dbis-nuc10/DBIS/2nc2iologs/minpart20tweet32mb.txt')
    results.append(result)
    # Clear the contents of the output log file
    df = pd.DataFrame(results)

    df.to_csv('stats.csv', index=False)
    input_csv = 'stats.csv'  # Your input CSV file with the original format
    output_csv = 'formatted_stats.csv'  # The output CSV with the desired format
    reformat_csv(input_csv, output_csv)
