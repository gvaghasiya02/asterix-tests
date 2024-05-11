import requests
import csv
import json

url = "http://10.16.229.108:19002/query/service"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data1 = {
    "statement": "SET `compiler.optimize.groupby` 'false';USE wiscon16gb; SELECT ten, COUNT(ten) AS count FROM wiscondef16gb GROUP BY wiscondef16gb.ten;",
    "pretty": "true",
    "client_context_id": "xyz"
}

data2 = {
    "statement": "SET `compiler.optimize.groupby` 'true';USE wiscon16gb; SELECT ten, COUNT(ten) AS count FROM wiscondef16gb GROUP BY wiscondef16gb.ten;",
    "pretty": "true",
    "client_context_id": "xyz"
}

data= {
    "statement": "USE filler; SELECT COUNT(*) FROM wisconfiller;",
    "pretty": "true",
    "client_context_id": "xyz"
}

# Number of runs
num_runs = 1


# Ignore the first run
for run in range(1, num_runs + 1):
    
    response=requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        metrics = response.json().get("metrics", {})
        
        print(f"Cache clear Run {run} - Elapsed Time: {metrics.get('executionTime', 'N/A')}")
        
    response1 = requests.post(url, headers=headers, data=data1)
    if response.status_code == 200:
        metrics = response.json().get("metrics", {})
        print(metrics)
        
        print(f"Non Optimized Run {run} , {data1['statement']}- Elapsed Time: {metrics.get('executionTime', 'N/A')}")

    response=requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        metrics = response2.json().get("metrics", {})
        
        print(f"Cache clear Run {run} - Elapsed Time: {metrics.get('executionTime', 'N/A')}")

    response2 = requests.post(url, headers=headers, data=data2)
    if response2.status_code == 200:
        metrics = response2.json().get("metrics", {})

        print(f"Optimized Run {run} , {data2['statement']} - Elapsed Time: {metrics.get('executionTime', 'N/A')}")
    
    res1 = response1.json().get("results", {})
    res2 = response2.json().get("results", {})
    result = res1==res2
    print("JSONs are equal:", result)
