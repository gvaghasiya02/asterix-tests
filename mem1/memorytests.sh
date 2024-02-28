python3 ~/DBIS/asterix-tests/mem1/query_count_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/mem1/query_metrics_count_16gb.csv
python3 ~/DBIS/asterix-tests/mem1/optquery_count_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/mem1/opt_query_metrics_count_16gb.csv
python3 ~/DBIS/asterix-tests/mem1/query_sum_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/mem1/query_metrics_sum_16gb.csv
python3 ~/DBIS/asterix-tests/mem1/optquery_sum_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/mem1/opt_query_metrics_sum_16gb.csv
python3 ~/DBIS/asterix-tests/mem1/query_max_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/mem1/query_metrics_max_16gb.csv
python3 ~/DBIS/asterix-tests/mem1/optquery_max_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/mem1/opt_query_metrics_max_16gb.csv
python3 ~/DBIS/asterix-tests/mem1/query_min_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/mem1/query_metrics_min_16gb.csv
python3 ~/DBIS/asterix-tests/mem1/optquery_min_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/mem1/opt_query_metrics_min_16gb.csv