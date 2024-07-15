queries = """

"""
# Add the queries here

# Split the large string into individual queries
query_list = queries.strip().split('\n')

# This will store the final output
output = []

for query in query_list:
    # Strip any excess whitespace from the ends
    query = query.strip().lower()
    # Create three versions of each query
    no_optimize = f"set `compiler.optimize.groupby` 'false';{query}"
    optimize = f"set `compiler.optimize.groupby` 'true';{query}"
    hash_optimize = query.replace("group by", "/*+ hash */ group by")
    
    # Append to output
    output.extend([no_optimize, optimize, hash_optimize])

# Join all output lines into a single string with line breaks
final_output = "\n".join(output)

# Writing to a file
file_path = 'transformed_queries.txt'
with open(file_path, 'w') as file:
    file.write(final_output)

file_path
