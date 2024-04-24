python3 ~/DBIS/asterix-tests/temps/query_count_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/temps/query_metrics_count_16gb.csv
python3 ~/DBIS/asterix-tests/temps/optquery_count_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/temps/opt_query_metrics_count_16gb.csv
python3 ~/DBIS/asterix-tests/temps/query_sum_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/temps/query_metrics_sum_16gb.csv
python3 ~/DBIS/asterix-tests/temps/optquery_sum_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/temps/opt_query_metrics_sum_16gb.csv