import csv
import json

# Cleaning Data from Extractor.py

def process_json_to_csv(input_json_path, output_csv_path):
    # Load JSON data from file
    with open(input_json_path, 'r') as f:
        data = json.load(f)

    # Temporary list to hold raw values before normalization
    raw_rows = []
    min_time = float('inf')

    # First pass to gather data and find minimum valid timestamp
    for entry in data:
        user_info = entry.get("user", "")
        try:
            user_id = int(user_info.split('-')[1].split('=')[0])
            query_class = user_info.split('=')[1]
        except (IndexError, ValueError):
            user_id = ""
            query_class = ""

        metrics = entry.get("content", {}).get("metrics", {})
        added_queue = metrics.get("addedToTheQueueTimeNano", -1)
        added_mem_queue = metrics.get("addedToTheMemoryQueueTimeNano", -1)
        exec_start = metrics.get("executionStartTimeNano", 0)
        exec_end = metrics.get("executionEndTimeNano", 0)

        # Update min_time (ignoring -1)
        for t in (added_queue, added_mem_queue, exec_start):
            if t != -1:
                min_time = min(min_time, t)

        request_id = entry.get("content", {}).get("requestID", "")

        raw_rows.append({
            "user_id": user_id,
            "query_class": query_class,
            "added_queue": added_queue,
            "added_mem_queue": added_mem_queue,
            "exec_start": exec_start,
            "exec_end": exec_end,
            "request_id": request_id
        })

    # Second pass to process and normalize time fields
    csv_rows = []
    for row in raw_rows:
        added_queue = row["added_queue"]
        added_mem_queue = row["added_mem_queue"]
        exec_start = row["exec_start"]
        exec_end = row["exec_end"]

        # Normalize timestamps (only if they are not -1)
        added_queue_adj = int((added_queue - min_time)/1e9) if added_queue != -1 else -1
        added_mem_queue_adj = int((added_mem_queue - min_time)/1e9) if added_mem_queue != -1 else -1
        exec_start_adj = int((exec_start - min_time)/1e9)
        exec_end_adj = int((exec_end - min_time)/1e9)

        # Recompute durations based on adjusted times
        if added_queue_adj == -1:
            queue_duration = 0
        elif added_mem_queue_adj == -1:
            queue_duration = (exec_start_adj - added_queue_adj)
        else:
            queue_duration = (added_mem_queue_adj - added_queue_adj)

        memory_q_duration = -1 if added_mem_queue_adj == -1 else (exec_start_adj - added_mem_queue_adj)
        exec_duration = exec_end_adj - exec_start_adj

        csv_rows.append([
            row["user_id"],
            row["query_class"],
            added_queue_adj,
            queue_duration,
            added_mem_queue_adj,
            memory_q_duration,
            exec_start_adj,
            exec_duration,
            row["request_id"]
        ])

    # Write to CSV
    with open(output_csv_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["UserID", "QueryClass", "StartQueueTime", "Queue_Duration", "MemoryQStartTime",
                         "MemoryQDuration", "ExecutionStart", "ExecutionDuration", "RequestID"])
        writer.writerows(csv_rows)
    print(f"Data written to {output_csv_path}"+min_time.__str__())

if __name__ == "__main__":
    process_json_to_csv("./Results/FIFO_CP_48.json", "./Results/FIFO_CP_48.csv")
    process_json_to_csv("./Results/FIFOOrdered_CP_48.json", "./Results/FIFOOrdered_CP_48.csv")
    process_json_to_csv("./Results/Wiscon_V1_CP_48.json", "./Results/Wiscon_V1_CP_48.csv")
    process_json_to_csv("./Results/Wiscon_V2_CP_48.json", "./Results/Wiscon_V2_CP_48.csv")
    process_json_to_csv("./Results/Wiscon_V3_CP_48.json", "./Results/Wiscon_V3_CP_48.csv")
    process_json_to_csv("./Results/Colorado_V1_CP_48.json", "./Results/Colorado_V1_CP_48.csv")
    process_json_to_csv("./Results/Colorado_V2_CP_48.json", "./Results/Colorado_V2_CP_48.csv")
