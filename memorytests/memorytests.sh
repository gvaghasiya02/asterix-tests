python3 ~/DBIS/asterix-tests/memorytests/count/query_count_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/memorytests/query_metrics_count_16gb.csv
python3 ~/DBIS/asterix-tests/memorytests/count/optquery_count_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/memorytests/opt_query_metrics_count_16gb.csv
python3 ~/DBIS/asterix-tests/memorytests/count/query_sum_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/memorytests/query_metrics_sum_16gb.csv
python3 ~/DBIS/asterix-tests/memorytests/count/optquery_sum_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/memorytests/opt_query_metrics_sum_16gb.csv