cd ~/DBIS
# sh .asterix-tests/onetimesetup.sh
sh ./asterix-tests/runsetup.sh
wait
sh ./asterix-tests/wiscondefdatagen.sh $1
wait
sh ./asterix-tests/asterixdbstop.sh
wait
sh ./asterix-tests/asterixdbstart.sh
wait
python3 ./asterix-tests/wisconload.py
wait
sh ./asterix-tests/asterixdbstop.sh
wait
sh ./asterix-tests/asterixdbstart.sh
wait
python3 ./asterix-tests/query.py
wait
sh ./asterix-tests/asterixdbstop.sh
wait
sh ./asterix-tests/asterixdbstart.sh
wait
python3 ./asterix-tests/optquery.py
wait
sh ./asterix-tests/asterixdbstop.sh