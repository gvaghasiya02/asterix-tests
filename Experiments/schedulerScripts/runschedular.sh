# This script is used to run the BigFun scheduler in the background and kill it after 4 hours
#!/bin/bash
export BIGFUN_HOME=/home/dbis-nuc10/DBIS/SchedularRunnerFinal/
cd /home/dbis-nuc10/DBIS/SchedularRunnerFinal/target
java -jar bigfun-driver.jar cc=10.16.229.110 conf=bigfun_schedulerSetup.json >> schedularrunning.txt &
var_pid=$!
echo $var_pid
now=“$(date)”
printf “Current date and time1 %s\n” “$now”
sleep 14400
now=“$(date)”
printf “Current date and time2 %s\n” “$now”
kill -9 $var_pid
sleep 5\
