import requests
import csv
import json

url = "http://localhost:19002/query/service"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data1 = {
    "statement": "SET `compiler.optimize.groupby` 'false';USE wiscon106; SELECT ten, COUNT(ten) AS count FROM wiscondef106 GROUP BY wiscondef106.ten;",
    "pretty": "true",
    "profile":"timings",
    "optimized-logical-plan":"true",
    "plan-format":"STRING",
    "client_context_id": "xyz"
}

data2 = {
    "statement": "SET `compiler.optimize.groupby` 'true';USE wiscon106; SELECT ten, COUNT(ten) AS count FROM wiscondef106 GROUP BY wiscondef106.ten;",
    "pretty": "true",
    "profile":"timings",
    "optimized-logical-plan":"true",
    "plan-format":"STRING",
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
        
        print(f"Cache clear Run {run} - Execution Time: {metrics.get('executionTime', 'N/A')}")
        
    response1 = requests.post(url, headers=headers, data=data1)
    if response1.status_code == 200:
        metrics = response1.json().get("metrics", {})
        profile=json.dumps(response1.json().get("profile",{}),indent=4)
        plan=response1.json().get("plans",{})
        
        print(f"Non Optimized Run {run} , {data1['statement']}- Execution Time: {metrics.get('executionTime', 'N/A')}")
        print(metrics)
        print(plan)
        print(profile)

    response=requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        metrics = response.json().get("metrics", {})
        
        print(f"Cache clear Run {run} - Execution Time: {metrics.get('executionTime', 'N/A')}")

    response2 = requests.post(url, headers=headers, data=data2)
    if response2.status_code == 200:
        metrics = response2.json().get("metrics", {})
        profile=json.dumps(response1.json().get("profile",{}),indent=4)
        plan=response1.json().get("plans",{})

        print(f"Optimized Run {run} , {data2['statement']} - Execution Time: {metrics.get('executionTime', 'N/A')}")
        print(metrics)
        print(plan)
        print(profile)
    
    res1 = response1.json().get("results", {})
    res2 = response2.json().get("results", {})
    result = res1==res2
    print("JSONs are equal:", result)
