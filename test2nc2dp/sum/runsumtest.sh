# sum
# 2gb
python3 ~/DBIS/asterix-tests/test2nc2dp/sum/query_sum_2gb.py
wait
mv ~/DBIS/asterix-tests/test2nc2dp/sum/query_metrics.csv ~/DBIS/results/test2nc2dp/sum/query_metrics_sum_2gb.csv
python3 ~/DBIS/asterix-tests/test2nc2dp/sum/optquery_sum_2gb.py
wait
mv ~/DBIS/asterix-tests/test2nc2dp/sum/query_metrics.csv ~/DBIS/results/test2nc2dp/sum/opt_query_metrics_sum_2gb.csv
# 4gb
python3 ~/DBIS/asterix-tests/test2nc2dp/sum/query_sum_4gb.py
wait
mv ~/DBIS/asterix-tests/test2nc2dp/sum/query_metrics.csv ~/DBIS/results/test2nc2dp/sum/query_metrics_sum_4gb.csv
python3 ~/DBIS/asterix-tests/test2nc2dp/sum/optquery_sum_4gb.py
wait
mv ~/DBIS/asterix-tests/test2nc2dp/sum/query_metrics.csv ~/DBIS/results/test2nc2dp/sum/opt_query_metrics_sum_4gb.csv
# 8gb
python3 ~/DBIS/asterix-tests/test2nc2dp/sum/query_sum_8gb.py
wait
mv ~/DBIS/asterix-tests/test2nc2dp/sum/query_metrics.csv ~/DBIS/results/test2nc2dp/sum/query_metrics_sum_8gb.csv
python3 ~/DBIS/asterix-tests/test2nc2dp/sum/optquery_sum_8gb.py
wait
mv ~/DBIS/asterix-tests/test2nc2dp/sum/query_metrics.csv ~/DBIS/results/test2nc2dp/sum/opt_query_metrics_sum_8gb.csv
# 16gb
python3 ~/DBIS/asterix-tests/test2nc2dp/sum/query_sum_16gb.py
wait
mv ~/DBIS/asterix-tests/test2nc2dp/sum/query_metrics.csv ~/DBIS/results/test2nc2dp/sum/query_metrics_sum_16gb.csv
python3 ~/DBIS/asterix-tests/test2nc2dp/sum/optquery_sum_16gb.py
wait
mv ~/DBIS/asterix-tests/test2nc2dp/sum/query_metrics.csv ~/DBIS/results/test2nc2dp/sum/opt_query_metrics_sum_16gb.csv
# 32gb
python3 ~/DBIS/asterix-tests/test2nc2dp/sum/query_sum_32gb.py
wait
mv ~/DBIS/asterix-tests/test2nc2dp/sum/query_metrics.csv ~/DBIS/results/test2nc2dp/sum/query_metrics_sum_32gb.csv
python3 ~/DBIS/asterix-tests/test2nc2dp/sum/optquery_sum_32gb.py
wait
mv ~/DBIS/asterix-tests/test2nc2dp/sum/query_metrics.csv ~/DBIS/results/test2nc2dp/sum/opt_query_metrics_sum_32gb.csv
# 64gb
python3 ~/DBIS/asterix-tests/test2nc2dp/sum/query_sum_64gb.py
wait
mv ~/DBIS/asterix-tests/test2nc2dp/sum/query_metrics.csv ~/DBIS/results/test2nc2dp/sum/query_metrics_sum_64gb.csv
python3 ~/DBIS/asterix-tests/test2nc2dp/sum/optquery_sum_64gb.py
wait
mv ~/DBIS/asterix-tests/test2nc2dp/sum/query_metrics.csv ~/DBIS/results/test2nc2dp/sum/opt_query_metrics_sum_64gb.csv