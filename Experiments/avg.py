# get average of the query metrics based on queries
import csv
import numpy as np

def convert_to_milliseconds(time_str):
    if time_str.endswith("ns"):
        return float(time_str[:-2]) / 1000000
    elif time_str.endswith("ms"):
        return float(time_str[:-2])
    elif time_str.endswith("s"):
        return float(time_str[:-1]) * 1000
    else:
        raise ValueError("Invalid time format")

def convert_to_float(fraction_str):
    try:
        return float(fraction_str.strip('%')) / 100
    except ValueError:
        return 0.0

def main():
    input_file = "query_metrics.csv"
    output_file = "query_statistics.csv"

    stats = {}

    with open(input_file, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            query = row['Query']
            if query not in stats:
                stats[query] = {
                    'ExecutionTime': [],
                    'ElapsedTime': [],
                    'CompileTime': [],
                    'QueueWaitTime': [],
                    'ResultCount': [],
                    'ResultSize': [],
                    'ProcessedObjects': [],
                    'bufferCacheHitRatio': [],
                    'bufferCachePageReadCount': []
                }

            stats[query]['ExecutionTime'].append(convert_to_milliseconds(row['ExecutionTime']))
            stats[query]['ElapsedTime'].append(convert_to_milliseconds(row['ElapsedTime']))
            stats[query]['CompileTime'].append(convert_to_milliseconds(row['CompileTime']))
            stats[query]['QueueWaitTime'].append(convert_to_milliseconds(row['QueueWaitTime']))
            stats[query]['ResultCount'].append(float(row['ResultCount']))
            stats[query]['ResultSize'].append(float(row['ResultSize']))
            stats[query]['ProcessedObjects'].append(float(row['ProcessedObjects']))
            stats[query]['bufferCacheHitRatio'].append(convert_to_float(row['bufferCacheHitRatio']))
            stats[query]['bufferCachePageReadCount'].append(float(row['bufferCachePageReadCount']))

    with open(output_file, mode="w", newline="") as csvfile:
        fieldnames = ['Query', 'AverageExecutionTime(ms)', 'StdDevExecutionTime(ms)',
                      'AverageElapsedTime(ms)', 'AverageCompileTime(ms)', 'AverageQueueWaitTime(ms)',
                      'AverageResultCount', 'AverageResultSize', 'AverageProcessedObjects',
                      'AverageBufferCacheHitRatio', 'AverageBufferCachePageReadCount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for query, data in stats.items():
            averages = {key: np.mean(values) for key, values in data.items()}
            std_devs = {key: np.std(values) for key, values in data.items()}

            writer.writerow({
                'Query': query,
                'AverageExecutionTime(ms)': averages['ExecutionTime'],
                'StdDevExecutionTime(ms)': std_devs['ExecutionTime'],
                'AverageElapsedTime(ms)': averages['ElapsedTime'],
                'AverageCompileTime(ms)': averages['CompileTime'],
                'AverageQueueWaitTime(ms)': averages['QueueWaitTime'],
                'AverageResultCount': averages['ResultCount'],
                'AverageResultSize': averages['ResultSize'],
                'AverageProcessedObjects': averages['ProcessedObjects'],
                'AverageBufferCacheHitRatio': averages['bufferCacheHitRatio'],
                'AverageBufferCachePageReadCount': averages['bufferCachePageReadCount']
            })

if __name__ == "__main__":
    main()
