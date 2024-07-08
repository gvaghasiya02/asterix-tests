import requests

url = "http://localhost:19002/query/service"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Define data for the query
data = {
    "statement": "SET `compiler.optimize.groupby` 'true'; USE wiscon; SELECT * FROM wiscondef LIMIT 1;",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)
