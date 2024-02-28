python3 ~/DBIS/asterix-tests/memorytests/query_count_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/memorytests/query_metrics_count_16gb.csv
python3 ~/DBIS/asterix-tests/memorytests/optquery_count_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/memorytests/opt_query_metrics_count_16gb.csv
python3 ~/DBIS/asterix-tests/memorytests/query_sum_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/memorytests/query_metrics_sum_16gb.csv
python3 ~/DBIS/asterix-tests/memorytests/optquery_sum_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/memorytests/opt_query_metrics_sum_16gb.csv
python3 ~/DBIS/asterix-tests/memorytests/query_max_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/memorytests/query_metrics_max_16gb.csv
python3 ~/DBIS/asterix-tests/memorytests/optquery_max_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/memorytests/opt_query_metrics_max_16gb.csv
python3 ~/DBIS/asterix-tests/memorytests/query_min_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/memorytests/query_metrics_min_16gb.csv
python3 ~/DBIS/asterix-tests/memorytests/optquery_min_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/memorytests/opt_query_metrics_min_16gb.csv