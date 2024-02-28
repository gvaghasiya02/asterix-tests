python3 ~/DBIS/asterix-tests/memorytestsnormal/query_count_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/memorytestsnormal/query_metrics_count_16gb.csv
python3 ~/DBIS/asterix-tests/memorytestsnormal/optquery_count_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/memorytestsnormal/opt_query_metrics_count_16gb.csv
python3 ~/DBIS/asterix-tests/memorytestsnormal/query_sum_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/memorytestsnormal/query_metrics_sum_16gb.csv
python3 ~/DBIS/asterix-tests/memorytestsnormal/optquery_sum_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/memorytestsnormal/opt_query_metrics_sum_16gb.csv
python3 ~/DBIS/asterix-tests/memorytestsnormal/query_max_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/memorytestsnormal/query_metrics_max_16gb.csv
python3 ~/DBIS/asterix-tests/memorytestsnormal/optquery_max_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/memorytestsnormal/opt_query_metrics_max_16gb.csv
python3 ~/DBIS/asterix-tests/memorytestsnormal/query_min_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/memorytestsnormal/query_metrics_min_16gb.csv
python3 ~/DBIS/asterix-tests/memorytestsnormal/optquery_min_16gb.py
wait
mv query_metrics.csv ~/DBIS/results/memorytestsnormal/opt_query_metrics_min_16gb.csv