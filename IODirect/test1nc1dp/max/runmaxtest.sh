# max
# 2gb
python3 ~/DBIS/asterix-tests/IODirect/test1nc1dp/max/query_max_2gb.py
wait
mv query_metrics.csv ~/DBIS/results/IODirect/test1nc1dp/max/query_metrics_max_2gb.csv
python3 ~/DBIS/asterix-tests/IODirect/test1nc1dp/max/optquery_max_2gb.py
wait
mv query_metrics.csv ~/DBIS/results/IODirect/test1nc1dp/max/opt_query_metrics_max_2gb.csv
# 4gb
python3 ~/DBIS/asterix-tests/IODirect/test1nc1dp/max/query_max_4gb.py
wait
mv query_metrics.csv ~/DBIS/results/IODirect/test1nc1dp/max/query_metrics_max_4gb.csv
python3 ~/DBIS/asterix-tests/IODirect/test1nc1dp/max/optquery_max_4gb.py
wait
mv query_metrics.csv ~/DBIS/results/IODirect/test1nc1dp/max/opt_query_metrics_max_4gb.csv
# 8gb
python3 ~/DBIS/asterix-tests/IODirect/test1nc1dp/max/query_max_8gb.py
wait
mv query_metrics.csv ~/DBIS/results/IODirect/test1nc1dp/max/query_metrics_max_8gb.csv
python3 ~/DBIS/asterix-tests/IODirect/test1nc1dp/max/optquery_max_8gb.py
wait
mv query_metrics.csv ~/DBIS/results/IODirect/test1nc1dp/max/opt_query_metrics_max_8gb.csv
# 16gb
python3 ~/DBIS/asterix-tests/IODirect/test1nc1dp/max/query_max_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/IODirect/test1nc1dp/max/query_metrics_max_16gb.csv
python3 ~/DBIS/asterix-tests/IODirect/test1nc1dp/max/optquery_max_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/IODirect/test1nc1dp/max/opt_query_metrics_max_16gb.csv
# 32gb
python3 ~/DBIS/asterix-tests/IODirect/test1nc1dp/max/query_max_32gb.py
wait
mv query_metrics.csv ~/DBIS/results/IODirect/test1nc1dp/max/query_metrics_max_32gb.csv
python3 ~/DBIS/asterix-tests/IODirect/test1nc1dp/max/optquery_max_32gb.py
wait
mv query_metrics.csv ~/DBIS/results/IODirect/test1nc1dp/max/opt_query_metrics_max_32gb.csv
# 64gb
python3 ~/DBIS/asterix-tests/IODirect/test1nc1dp/max/query_max_64gb.py
wait
mv query_metrics.csv ~/DBIS/results/IODirect/test1nc1dp/max/query_metrics_max_64gb.csv
python3 ~/DBIS/asterix-tests/IODirect/test1nc1dp/max/optquery_max_64gb.py
wait
mv query_metrics.csv ~/DBIS/results/IODirect/test1nc1dp/max/opt_query_metrics_max_64gb.csv