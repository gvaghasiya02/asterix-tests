# Comapring results with the same query for different group by approaches
import requests

# URL for the query service
url = "http://localhost:19002/query/service"

# Common headers for all HTTP requests
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Function to run a single query with the given optimization setting
def run_query(statement, optimize=True):
    prefix = "set `compiler.optimize.groupby` 'true';" if optimize else "set `compiler.optimize.groupby` 'false';"
    full_statement = prefix + statement
    data = {
        "statement": full_statement,
        "pretty": "true",
        "client_context_id": "xyz"
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json().get("results", {})

# Function to read queries and run them with and without optimization
def test_queries(file_path):
    with open(file_path, 'r') as file:
        queries = file.readlines()
    
    for query in queries:
        query = query.strip()
        if not query:
            continue
        # Run query with optimization enabled and disabled
        result_opt_true = run_query(query, optimize=True)
        result_opt_false = run_query(query, optimize=False)
        
        # Compare results
        is_equal = result_opt_true == result_opt_false
        print(f"Query: {query}")
        print("JSONs are equal:", is_equal)

# Path to the queries file
queries_file_path = 'queries.txt'
test_queries(queries_file_path)
