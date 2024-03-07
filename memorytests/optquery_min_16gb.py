import requests
import csv

url = "http://10.16.229.109:19002/query/service"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}


csv_filename = "query_metrics.csv"

data = {
    "statement": "SET `compiler.optimize.groupby` 'true';USE wiscon16gb; SELECT onePercent, MIN(ten) as min FROM wiscondef16gb GROUP BY wiscondef16gb.onePercent;",
    "pretty": "true",
    "client_context_id": "xyz"
}

data2= {
    "statement": "USE filler; SELECT COUNT(*) FROM wisconfiller;",
    "pretty": "true",
    "client_context_id": "xyz"
}
# Number of runs
num_runs = 11

# List to store metrics for each run
all_metrics = []

# Ignore the first run
for run in range(1, num_runs + 1):
    
    response2=requests.post(url, headers=headers, data=data2)
    if response2.status_code == 200:
        # Parse metrics from the response
        metrics = response2.json().get("metrics", {})
        
        print(f"Run {run} - Elapsed Time: {metrics.get('elapsedTime', 'N/A')}")
        
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        # Parse metrics from the response
        metrics = response.json().get("metrics", {})
        
        
        # Add metrics to the list
        all_metrics.append(metrics)
        
        print(f"Run {run} - Elapsed Time: {metrics.get('elapsedTime', 'N/A')}")
    
    

# Export metrics to CSV
header = ["Run", "ElapsedTime", "ExecutionTime", "CompileTime", "QueueWaitTime", "ResultCount", "ResultSize", "ProcessedObjects"]

with open(csv_filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    
    # Write header
    writer.writeheader()
    
    # Write data for the last 10 runs
    for run, metrics in enumerate(all_metrics[-10:], start=1):
        writer.writerow({
            "Run": run,
            "ElapsedTime": metrics.get('elapsedTime', 'N/A'),
            "ExecutionTime": metrics.get('executionTime', 'N/A'),
            "CompileTime": metrics.get('compileTime', 'N/A'),
            "QueueWaitTime": metrics.get('queueWaitTime', 'N/A'),
            "ResultCount": metrics.get('resultCount', 'N/A'),
            "ResultSize": metrics.get('resultSize', 'N/A'),
            "ProcessedObjects": metrics.get('processedObjects', 'N/A')
        })

print(f"Metrics exported to {csv_filename}")

