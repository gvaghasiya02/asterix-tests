import csv

def convert_to_milliseconds(time_str):
    if time_str.endswith("ns"):
        return float(time_str[:-2]) / 1000000
    elif time_str.endswith("ms"):
        return float(time_str[:-2])
    elif time_str.endswith("s"):
        return float(time_str[:-1]) * 1000
    else:
        raise ValueError("Invalid time format")

def main():
    input_file = "query_metrics.csv"
    output_file = "avg.csv"

    query_exec_times = {}

    with open(input_file, newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header
        for row in reader:
            query = row[0]
            execution_time = row[3]
            execution_time_ms = convert_to_milliseconds(execution_time)

            if query in query_exec_times:
                query_exec_times[query].append(execution_time_ms)
            else:
                query_exec_times[query] = [execution_time_ms]

    with open(output_file, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Query", "AverageExecutionTime(ms)"])
        for query, exec_times in query_exec_times.items():
            avg_exec_time_ms = sum(exec_times) / len(exec_times)
            writer.writerow([query, avg_exec_time_ms])

if __name__ == "__main__":
    main()