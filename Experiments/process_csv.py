import pandas as pd
import re


# Create a DataFrame from the data
data = pd.read_csv('query_statistics.csv')

# Function to process the 'Query' column and extract new fields
def process_query(query):
    if "set `compiler.optimize.groupby` 'false';" in query:
        type_ = 'sort'
        realquery = query.replace("set `compiler.optimize.groupby` 'false';", '').strip()
    elif "set `compiler.optimize.groupby` 'true';" in query:
        type_ = 'opt'
        realquery = query.replace("set `compiler.optimize.groupby` 'true';", '').strip()
    elif '/*+ hash */ ' in query:
        type_ = 'hash'
        realquery = query.replace('/*+ hash */ ', '').strip()
    else:
        type_ = 'unknown'
        realquery = query.strip()

    # Extract size
    size_match = re.search(r'wiscondefopen(\d+)gb', query)
    size_gb = size_match.group(1) if size_match else 'unknown'

    return realquery, size_gb, type_

# Apply the function to the 'Query' column
data[['realquery', 'size(gb)', 'type']] = data['Query'].apply(lambda x: pd.Series(process_query(x)))

def extract_groupby_attributes(query):
    # Find the part of the query after 'group by'
    group_by_part = query.split('group by')[-1].strip()
    # Extract the attributes, ignoring any SQL following the attribute list
    attributes = group_by_part.split(';')[0].strip()
    cleaned_attributes = ','.join(attr.split('.')[-1] for attr in attributes.split(','))
    return cleaned_attributes

# Function to extract the aggregation type from a query
def extract_aggregate(query):
    aggregates = ['sum', 'count', 'min', 'max']
    for agg in aggregates:
        if agg in query.lower():
            return agg
    return None

# Apply functions to create new columns
data['groupbyattribute'] = data['realquery'].apply(extract_groupby_attributes)
data['aggregate'] = data['realquery'].apply(extract_aggregate)


data['nc'] = 2
data['dp'] = 1
data['groupmemory(MB)'] = 32

# Write the new DataFrame to a CSV file
data.to_csv('processed_queries.csv', index=False)
