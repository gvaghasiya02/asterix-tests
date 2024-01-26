echo "wisconsin data generation"
cd ~/DBIS/JSON-Wisconsin-Data-Generator
java -jar ./target/wisconsin-datagen.jar writer=file workload=Default.json  cardinality=2147483648
wait
cp ./outputp_0.adm ~/DBIS/data/wiscondef2gb.adm
wait
java -jar ./target/wisconsin-datagen.jar writer=file workload=Default.json  cardinality=4294967296
wait
cp ./outputp_0.adm ~/DBIS/data/wiscondef4gb.adm
wait
java -jar ./target/wisconsin-datagen.jar writer=file workload=Default.json  cardinality=8589934592
wait
cp ./outputp_0.adm ~/DBIS/data/wiscondef8gb.adm
wait
java -jar ./target/wisconsin-datagen.jar writer=file workload=Default.json  cardinality=17179869184
wait
cp ./outputp_0.adm ~/DBIS/data/wiscondef16gb.adm
wait
java -jar ./target/wisconsin-datagen.jar writer=file workload=Default.json  cardinality=34359738368
wait
cp ./outputp_0.adm ~/DBIS/data/wiscondef32gb.adm
wait
java -jar ./target/wisconsin-datagen.jar writer=file workload=Default.json  cardinality=68719476736
wait
cp ./outputp_0.adm ~/DBIS/data/wiscondef64gb.adm
