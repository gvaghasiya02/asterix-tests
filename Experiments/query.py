import requests
import csv
import json

url = "http://10.16.229.110:19002/query/service"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Function to read queries from a text file
def read_queries(filename):
    with open(filename, 'r') as file:
        queries = file.readlines()
    return queries

# Read queries from the text file
queries = read_queries('queries.txt')

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

csv_filename = "query_metrics.csv"

# Export metrics to CSV
header = ["Query", "Run", "ElapsedTime", "ExecutionTime", "CompileTime", "QueueWaitTime", "ResultCount", "ResultSize", "ProcessedObjects","bufferCacheHitRatio","bufferCachePageReadCount"]

import os.path

# Check if the file already exists
if os.path.exists(csv_filename):
    mode = 'a'  # Append mode
else:
    mode = 'w'  # Write mode

for query in queries:
    # Number of runs
    num_runs = 11

    # List to store metrics for each run
    all_metrics = []

    # Populating queries

    querydata["statement"] = query.strip()

    # Ignore the first run
    for run in range(1, num_runs + 1):

        response=requests.post(url, headers=headers, data=fillerdata)
        if response.status_code == 200:
            metrics = response.json().get("metrics", {})
            
            print(f"Cache clear Run {run} - Execution Time: {metrics.get('executionTime', 'N/A')}")
            
        query_response = requests.post(url, headers=headers, data=querydata)
        if query_response.status_code == 200:
            metrics = query_response.json().get("metrics", {})
            all_metrics.append(metrics)
            
            print(f"Query Run {run} , {querydata['statement']}- Execution Time: {metrics.get('executionTime', 'N/A')}") 

    with open(csv_filename, mode=mode, newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        
        # If the file is newly created, write the header
        if mode == 'w':
            writer.writeheader()
            print(f"header writing done to {csv_filename}") 

        # Write data for the last 10 runs
        for run, metrics in enumerate(all_metrics[-10:], start=1):
            writer.writerow({
                "Query":querydata['statement'],
                "Run": run,
                "ElapsedTime": metrics.get('elapsedTime', 'N/A'),
                "ExecutionTime": metrics.get('executionTime', 'N/A'),
                "CompileTime": metrics.get('compileTime', 'N/A'),
                "QueueWaitTime": metrics.get('queueWaitTime', 'N/A'),
                "ResultCount": metrics.get('resultCount', 'N/A'),
                "ResultSize": metrics.get('resultSize', 'N/A'),
                "ProcessedObjects": metrics.get('processedObjects', 'N/A'),
                "bufferCacheHitRatio": metrics.get('bufferCacheHitRatio', 'N/A'),
                "bufferCachePageReadCount": metrics.get('bufferCachePageReadCount', 'N/A')
            })
        
        for run, metrics in enumerate(all_metrics_opt[-10:], start=1):
            writer.writerow({
                "Query":data2['statement'],
                "Run": run,
                "ElapsedTime": metrics.get('elapsedTime', 'N/A'),
                "ExecutionTime": metrics.get('executionTime', 'N/A'),
                "CompileTime": metrics.get('compileTime', 'N/A'),
                "QueueWaitTime": metrics.get('queueWaitTime', 'N/A'),
                "ResultCount": metrics.get('resultCount', 'N/A'),
                "ResultSize": metrics.get('resultSize', 'N/A'),
                "ProcessedObjects": metrics.get('processedObjects', 'N/A'),
                "bufferCacheHitRatio": metrics.get('bufferCacheHitRatio', 'N/A'),
                "bufferCachePageReadCount": metrics.get('bufferCachePageReadCount', 'N/A')
            })

    print(f"Metrics added to {csv_filename}")

