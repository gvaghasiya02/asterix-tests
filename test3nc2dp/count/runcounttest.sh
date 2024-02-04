# count
# 2gb
python3 ~/DBIS/asterix-tests/test4nc2dp/count/query_count_2gb.py
wait
mv query_metrics.csv ~/DBIS/results/test4nc2dp/count/query_metrics_count_2gb.csv
python3 ~/DBIS/asterix-tests/test4nc2dp/count/optquery_count_2gb.py
wait
mv query_metrics.csv ~/DBIS/results/test4nc2dp/count/opt_query_metrics_count_2gb.csv
# 4gb
python3 ~/DBIS/asterix-tests/test4nc2dp/count/query_count_4gb.py
wait
mv query_metrics.csv ~/DBIS/results/test4nc2dp/count/query_metrics_count_4gb.csv
python3 ~/DBIS/asterix-tests/test4nc2dp/count/optquery_count_4gb.py
wait
mv query_metrics.csv ~/DBIS/results/test4nc2dp/count/opt_query_metrics_count_4gb.csv
# 8gb
python3 ~/DBIS/asterix-tests/test4nc2dp/count/query_count_8gb.py
wait
mv query_metrics.csv ~/DBIS/results/test4nc2dp/count/query_metrics_count_8gb.csv
python3 ~/DBIS/asterix-tests/test4nc2dp/count/optquery_count_8gb.py
wait
mv query_metrics.csv ~/DBIS/results/test4nc2dp/count/opt_query_metrics_count_8gb.csv
# 16gb
python3 ~/DBIS/asterix-tests/test4nc2dp/count/query_count_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/test4nc2dp/count/query_metrics_count_16gb.csv
python3 ~/DBIS/asterix-tests/test4nc2dp/count/optquery_count_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/test4nc2dp/count/opt_query_metrics_count_16gb.csv
# 32gb
python3 ~/DBIS/asterix-tests/test4nc2dp/count/query_count_32gb.py
wait
mv query_metrics.csv ~/DBIS/results/test4nc2dp/count/query_metrics_count_32gb.csv
python3 ~/DBIS/asterix-tests/test4nc2dp/count/optquery_count_32gb.py
wait
mv query_metrics.csv ~/DBIS/results/test4nc2dp/count/opt_query_metrics_count_32gb.csv
# 64gb
python3 ~/DBIS/asterix-tests/test4nc2dp/count/query_count_64gb.py
wait
mv query_metrics.csv ~/DBIS/results/test4nc2dp/count/query_metrics_count_64gb.csv
python3 ~/DBIS/asterix-tests/test4nc2dp/count/optquery_count_64gb.py
wait
mv query_metrics.csv ~/DBIS/results/test4nc2dp/count/opt_query_metrics_count_64gb.csv