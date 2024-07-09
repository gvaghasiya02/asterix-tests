import csv
import re

# Input and output file names
input_file_name = 'avg.csv'
output_file_name = 'final.csv'

# Open input file for reading and output file for writing
with open(input_file_name, mode='r', newline='') as input_csvfile, \
     open(output_file_name, mode='w', newline='') as output_csvfile:
    
    # Setup CSV reader and writer
    reader = csv.reader(input_csvfile)
    fieldnames = ['Query', 'AverageExecutionTime(ms)', 'Size(GB)', 'IsOptimize', 'OpenType', 'AggregationType', 'NCs', 'DPs']
    writer = csv.DictWriter(output_csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Skip header if present in the input CSV
    next(reader, None)

    # Process each row in the input CSV
    for row in reader:
        if not row:
            continue
        query, time = row  # Assuming two columns in the input CSV

        # Extract size with an updated regex that handles 'open' keyword
        size_match = re.search(r'wiscon(?:open)?(\d+)gb', query, re.IGNORECASE)
        size_gb = size_match.group(1) if size_match else 'Unknown'

        # Check for optimization
        is_optimize = 'NA'
        if "`compiler.optimize.groupby` 'true'" in query:
            is_optimize = 'true'
        elif "`compiler.optimize.groupby` 'false'" in query:
            is_optimize = 'false'

        # Check for open type
        open_type = 'true' if 'open' in query.lower() else 'false'

        # Determine aggregation type
        if 'COUNT(' in query.upper():
            aggregation_type = 'COUNT'
        elif 'SUM(' in query.upper():
            aggregation_type = 'SUM'
        else:
            aggregation_type = 'Unknown'

        # Write to output CSV
        writer.writerow({
            'Query': query,
            'AverageExecutionTime(ms)': time,
            'Size(GB)': size_gb,
            'IsOptimize': is_optimize,
            'OpenType': open_type,
            'AggregationType': aggregation_type,
            'NCs': 1,
            'DPs': 1
        })

print("CSV processing complete. The data has been saved to 'processed_queries.csv'.")
