#!/bin/bash

# File to store the output
output_file="system_stats.txt"

# Interval in seconds between each data capture
interval=5

# Header for the data in the text file
echo "Timestamp, CPU Usage (%), Memory Usage (%), Disk Read (kB/s), Disk Write (kB/s)" >> $output_file

# Infinite loop to keep capturing the data
while true
do
    # Get CPU usage (%)
    cpu_usage=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')

    # Get Memory usage (%)
    memory_usage=$(free | grep Mem | awk '{print $3/$2 * 100.0}')

    # Get Disk read/write stats (kB/s)
    disk_stats=$(iostat -dkx 1 1 | awk 'NR==7 {print $6, $7}')

    # Combine the results with the timestamp
    echo "$(date +'%Y-%m-%d %H:%M:%S'), $cpu_usage, $memory_usage, $disk_stats" >> $output_file

    # Sleep for the specified interval
    sleep $interval
done
