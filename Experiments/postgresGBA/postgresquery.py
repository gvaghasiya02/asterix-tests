import psycopg2
import csv
import subprocess
import os

# Configuration
DB_NAME = "tpcds"
DB_USER = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"
QUERY_FILE = "queries.txt"
CSV_FILE = "query_metrics_postgres.csv"
NUM_RUNS = 11

# CSV Header
header = [
    "Query",
    "Run",
    "ExecutionTime_ms",
    "SharedHits",
    "SharedReads",
    "ReturnedRows",
]


def clear_cache():
    print("🧹 Dropping Linux system cache...")
    subprocess.run(
        "sync; echo 3 | sudo tee /proc/sys/vm/drop_caches",
        shell=True,
        stdout=subprocess.DEVNULL,
    )


def parse_explain_output(output_lines):
    execution_time = None
    shared_hit = 0
    shared_read = 0
    rows = 0

    for line in output_lines:
        line = line.strip()
        if "Execution Time" in line:
            try:
                execution_time = float(line.split("Execution Time:")[1].split()[0])
            except:
                pass
        if "actual time=" in line and "rows=" in line:
            try:
                part = line.split("rows=")[1]
                rows = int(part.split()[0])
            except:
                pass
        if "Buffers:" in line:
            if "shared hit=" in line:
                shared_hit = int(line.split("shared hit=")[1].split()[0])
            if "shared read=" in line:
                shared_read = int(line.split("shared read=")[1].split()[0])

    return {
        "ExecutionTime_ms": execution_time,
        "SharedHits": shared_hit,
        "SharedReads": shared_read,
        "ReturnedRows": rows,
    }


def run_benchmark():
    with psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, host=DB_HOST, port=DB_PORT
    ) as conn:
        with conn.cursor() as cursor:
            with open(QUERY_FILE, "r") as qf, open(
                CSV_FILE, "w", newline=""
            ) as out_csv:
                queries = [line.strip() for line in qf if line.strip()]
                writer = csv.DictWriter(out_csv, fieldnames=header)
                writer.writeheader()

                for query in queries:
                    print(f"\n🧪 Running query: {query[:60]}...")
                    for run in range(1, NUM_RUNS + 1):
                        clear_cache()

                        explain_query = f"EXPLAIN (ANALYZE, BUFFERS, TIMING) {query}"
                        cursor.execute(explain_query)
                        plan = cursor.fetchall()
                        plan_lines = [row[0] for row in plan]
                        metrics = parse_explain_output(plan_lines)
                        metrics["Query"] = query
                        metrics["Run"] = run
                        writer.writerow(metrics)

                        print(
                            f"✅ Run {run}: {metrics['ExecutionTime_ms']} ms, Rows: {metrics['ReturnedRows']}"
                        )


if __name__ == "__main__":
    run_benchmark()
