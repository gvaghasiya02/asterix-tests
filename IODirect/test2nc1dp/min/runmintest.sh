# min
# 2gb
python3 ~/DBIS/asterix-tests/IODirect/test2nc1dp/min/query_min_2gb.py
wait
mv query_metrics.csv ~/DBIS/results/IODirect/test2nc1dp/min/query_metrics_min_2gb.csv
python3 ~/DBIS/asterix-tests/IODirect/test2nc1dp/min/optquery_min_2gb.py
wait
mv query_metrics.csv ~/DBIS/results/IODirect/test2nc1dp/min/opt_query_metrics_min_2gb.csv
# 4gb
python3 ~/DBIS/asterix-tests/IODirect/test2nc1dp/min/query_min_4gb.py
wait
mv query_metrics.csv ~/DBIS/results/IODirect/test2nc1dp/min/query_metrics_min_4gb.csv
python3 ~/DBIS/asterix-tests/IODirect/test2nc1dp/min/optquery_min_4gb.py
wait
mv query_metrics.csv ~/DBIS/results/IODirect/test2nc1dp/min/opt_query_metrics_min_4gb.csv
# 8gb
python3 ~/DBIS/asterix-tests/IODirect/test2nc1dp/min/query_min_8gb.py
wait
mv query_metrics.csv ~/DBIS/results/IODirect/test2nc1dp/min/query_metrics_min_8gb.csv
python3 ~/DBIS/asterix-tests/IODirect/test2nc1dp/min/optquery_min_8gb.py
wait
mv query_metrics.csv ~/DBIS/results/IODirect/test2nc1dp/min/opt_query_metrics_min_8gb.csv
# 16gb
python3 ~/DBIS/asterix-tests/IODirect/test2nc1dp/min/query_min_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/IODirect/test2nc1dp/min/query_metrics_min_16gb.csv
python3 ~/DBIS/asterix-tests/IODirect/test2nc1dp/min/optquery_min_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/IODirect/test2nc1dp/min/opt_query_metrics_min_16gb.csv
# 32gb
python3 ~/DBIS/asterix-tests/IODirect/test2nc1dp/min/query_min_32gb.py
wait
mv query_metrics.csv ~/DBIS/results/IODirect/test2nc1dp/min/query_metrics_min_32gb.csv
python3 ~/DBIS/asterix-tests/IODirect/test2nc1dp/min/optquery_min_32gb.py
wait
mv query_metrics.csv ~/DBIS/results/IODirect/test2nc1dp/min/opt_query_metrics_min_32gb.csv
# 64gb
python3 ~/DBIS/asterix-tests/IODirect/test2nc1dp/min/query_min_64gb.py
wait
mv query_metrics.csv ~/DBIS/results/IODirect/test2nc1dp/min/query_metrics_min_64gb.csv
python3 ~/DBIS/asterix-tests/IODirect/test2nc1dp/min/optquery_min_64gb.py
wait
mv query_metrics.csv ~/DBIS/results/IODirect/test2nc1dp/min/opt_query_metrics_min_64gb.csv