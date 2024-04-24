import requests
import csv
import json

url = "http://10.16.229.110:19002/query/service"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "statement": "SET `compiler.codegen` 'true';USE wiscon16gb; SELECT ten, COUNT(ten) AS count FROM wiscondef16gb GROUP BY wiscondef16gb.ten;",
    "pretty": "true",
    "client_context_id": "xyz"
}

data1 = {
    "statement": "SET `compiler.codegen` 'false';USE wiscon16gb; SELECT ten, COUNT(ten) AS count FROM wiscondef16gb GROUP BY wiscondef16gb.ten;",
    "pretty": "true",
    "client_context_id": "xyz"
}

data2= {
    "statement": "USE filler; SELECT COUNT(*) FROM wisconfiller;",
    "pretty": "true",
    "client_context_id": "xyz"
}
# Number of runs
num_runs = 1


# Ignore the first run
for run in range(1, num_runs + 1):
    
    response2=requests.post(url, headers=headers, data=data2)
    print(response2.text)
    if response2.status_code == 200:
        # Parse metrics from the response
        metrics = response2.json().get("metrics", {})
        
        print(f"Run {run} - Elapsed Time: {metrics.get('elapsedTime', 'N/A')}")
        
    response = requests.post(url, headers=headers, data=data)
    # print(response.text)
    if response.status_code == 200:
        # Parse metrics from the response
        metrics = response.json().get("metrics", {})
        print(metrics)
        # print(response.text)
        # Add metrics to the list
        # all_metrics.append(metrics)
        
        print(f"Non Optimized Run {run} , {data['statement']}- Elapsed Time: {metrics.get('elapsedTime', 'N/A')}")

    response2=requests.post(url, headers=headers, data=data2)
    if response2.status_code == 200:
        # Parse metrics from the response
        metrics = response2.json().get("metrics", {})
        
        # print(f"Run {run} - Elapsed Time: {metrics.get('elapsedTime', 'N/A')}")

    response1 = requests.post(url, headers=headers, data=data1)
    if response1.status_code == 200:
        # Parse metrics from the response
        metrics = response1.json().get("metrics", {})
        print(metrics)
        # print(response1.text)
        # Add metrics to the list
        # all_metrics.append(metrics)
        
        print(f"Optimized Run {run} , {data1['statement']} - Elapsed Time: {metrics.get('elapsedTime', 'N/A')}")
    
    res = response.json().get("results", {})
    res1 = response1.json().get("results", {})
    result = res==res1
    print("JSONs are equal:", result)


# data = {
#     "statement": "SET `compiler.codegen` 'false';USE wiscon16gb; SELECT string4, COUNT(string4) AS count FROM wiscondef16gb GROUP BY wiscondef16gb.string4;",
#     "pretty": "true",
#     "client_context_id": "xyz"
# }

# data1 = {
#     "statement": "SET `compiler.codegen` 'true';USE wiscon16gb; SELECT string4, COUNT(string4) AS count FROM wiscondef16gb GROUP BY wiscondef16gb.string4;",
#     "pretty": "true",
#     "client_context_id": "xyz"
# }

# data2= {
#     "statement": "USE filler; SELECT COUNT(*) FROM wisconfiller;",
#     "pretty": "true",
#     "client_context_id": "xyz"
# }
# # Number of runs
# num_runs = 2


# # Ignore the first run
# for run in range(1, num_runs + 1):
    
#     response2=requests.post(url, headers=headers, data=data2)
#     if response2.status_code == 200:
#         # Parse metrics from the response
#         metrics = response2.json().get("metrics", {})
        
#         # print(f"Run {run} - Elapsed Time: {metrics.get('elapsedTime', 'N/A')}")
        
#     response = requests.post(url, headers=headers, data=data)
#     # print(response.text)
#     if response.status_code == 200:
#         # Parse metrics from the response
#         metrics = response.json().get("metrics", {})
#         # print(metrics)
        
#         # Add metrics to the list
#         # all_metrics.append(metrics)
        
#         print(f"Non Optimized Run {run} , {data['statement']}- Elapsed Time: {metrics.get('elapsedTime', 'N/A')}")

#     response2=requests.post(url, headers=headers, data=data2)
#     if response2.status_code == 200:
#         # Parse metrics from the response
#         metrics = response2.json().get("metrics", {})
        
#         # print(f"Run {run} - Elapsed Time: {metrics.get('elapsedTime', 'N/A')}")

#     response1 = requests.post(url, headers=headers, data=data1)
#     if response1.status_code == 200:
#         # Parse metrics from the response
#         metrics = response1.json().get("metrics", {})
#         # print(metrics)
        
#         # Add metrics to the list
#         # all_metrics.append(metrics)
        
#         print(f"Optimized Run {run} , {data['statement']} - Elapsed Time: {metrics.get('elapsedTime', 'N/A')}")
    
#     res = response.json().get("results", {})
#     res1 = response1.json().get("results", {})
#     result = res==res1
#     print("JSONs are equal:", result)


# data = {
#     "statement": "SET `compiler.codegen` 'false';USE wiscon16gb; SELECT string5, COUNT(string5) AS count FROM wiscondef16gb GROUP BY wiscondef16gb.string5;",
#     "pretty": "true",
#     "client_context_id": "xyz"
# }

# data1 = {
#     "statement": "SET `compiler.codegen` 'true';USE wiscon16gb; SELECT string5, COUNT(string5) AS count FROM wiscondef16gb GROUP BY wiscondef16gb.string5;",
#     "pretty": "true",
#     "client_context_id": "xyz"
# }

# data2= {
#     "statement": "USE filler; SELECT COUNT(*) FROM wisconfiller;",
#     "pretty": "true",
#     "client_context_id": "xyz"
# }
# # Number of runs
# num_runs = 2


# # Ignore the first run
# for run in range(1, num_runs + 1):
    
#     response2=requests.post(url, headers=headers, data=data2)
#     if response2.status_code == 200:
#         # Parse metrics from the response
#         metrics = response2.json().get("metrics", {})
        
#         # print(f"Run {run} - Elapsed Time: {metrics.get('elapsedTime', 'N/A')}")
        
#     response = requests.post(url, headers=headers, data=data)
#     # print(response.text)
#     if response.status_code == 200:
#         # Parse metrics from the response
#         metrics = response.json().get("metrics", {})
#         # print(metrics)
        
#         # Add metrics to the list
#         # all_metrics.append(metrics)
        
#         print(f"Non Optimized Run {run} , {data['statement']}- Elapsed Time: {metrics.get('elapsedTime', 'N/A')}")

#     response2=requests.post(url, headers=headers, data=data2)
#     if response2.status_code == 200:
#         # Parse metrics from the response
#         metrics = response2.json().get("metrics", {})
        
#         # print(f"Run {run} - Elapsed Time: {metrics.get('elapsedTime', 'N/A')}")

#     response1 = requests.post(url, headers=headers, data=data1)
#     if response1.status_code == 200:
#         # Parse metrics from the response
#         metrics = response1.json().get("metrics", {})
#         # print(metrics)
        
#         # Add metrics to the list
#         # all_metrics.append(metrics)
        
#         print(f"Optimized Run {run} , {data['statement']} - Elapsed Time: {metrics.get('elapsedTime', 'N/A')}")
    
#     res = response.json().get("results", {})
#     res1 = response1.json().get("results", {})
#     result = res==res1
#     print("JSONs are equal:", result)


# data = {
#     "statement": "SET `compiler.codegen` 'false';USE wiscon16gb; SELECT hundredkgroups,string4 COUNT(*) AS count FROM wiscondef16gb GROUP BY wiscondef16gb.hundredkgroups,wiscondef16gb.string4;",
#     "pretty": "true",
#     "client_context_id": "xyz"
# }

# data1 = {
#     "statement": "SET `compiler.codegen` 'true';USE wiscon16gb; SELECT hundredkgroups,string4 COUNT(*) AS count FROM wiscondef16gb GROUP BY wiscondef16gb.hundredkgroups,wiscondef16gb.string4;",
#     "pretty": "true",
#     "client_context_id": "xyz"
# }

# data2= {
#     "statement": "USE filler; SELECT COUNT(*) FROM wisconfiller;",
#     "pretty": "true",
#     "client_context_id": "xyz"
# }
# # Number of runs
# num_runs = 2


# # Ignore the first run
# for run in range(1, num_runs + 1):
    
#     response2=requests.post(url, headers=headers, data=data2)
#     if response2.status_code == 200:
#         # Parse metrics from the response
#         metrics = response2.json().get("metrics", {})
        
#         # print(f"Run {run} - Elapsed Time: {metrics.get('elapsedTime', 'N/A')}")
        
#     response = requests.post(url, headers=headers, data=data)
#     # print(response.text)
#     if response.status_code == 200:
#         # Parse metrics from the response
#         metrics = response.json().get("metrics", {})
#         # print(metrics)
        
#         # Add metrics to the list
#         # all_metrics.append(metrics)
        
#         print(f"Non Optimized Run {run} , {data['statement']}- Elapsed Time: {metrics.get('elapsedTime', 'N/A')}")

#     response2=requests.post(url, headers=headers, data=data2)
#     if response2.status_code == 200:
#         # Parse metrics from the response
#         metrics = response2.json().get("metrics", {})
        
#         # print(f"Run {run} - Elapsed Time: {metrics.get('elapsedTime', 'N/A')}")

#     response1 = requests.post(url, headers=headers, data=data1)
#     if response1.status_code == 200:
#         # Parse metrics from the response
#         metrics = response1.json().get("metrics", {})
#         # print(metrics)
        
#         # Add metrics to the list
#         # all_metrics.append(metrics)
        
#         print(f"Optimized Run {run} , {data['statement']} - Elapsed Time: {metrics.get('elapsedTime', 'N/A')}")
    
#     res = response.json().get("results", {})
#     res1 = response1.json().get("results", {})
#     result = res==res1
#     print("JSONs are equal:", result)