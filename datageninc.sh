echo "wisconsin data generation"
cd ~/DBIS/JSON-Wisconsin-Data-Generator
java -jar ./target/wisconsin-datagen.jar writer=file workload=Default.json  filesize=2048
wait
cp ./outputp_0.adm ~/DBIS/data/wiscondef2gb.adm
wait
java -jar ./target/wisconsin-datagen.jar writer=file workload=Default.json  filesize=4096
wait
cp ./outputp_0.adm ~/DBIS/data/wiscondef4gb.adm
wait
java -jar ./target/wisconsin-datagen.jar writer=file workload=Default.json  filesize=8192
wait
cp ./outputp_0.adm ~/DBIS/data/wiscondef8gb.adm
wait
java -jar ./target/wisconsin-datagen.jar writer=file workload=Default.json  filesize=16384
wait
cp ./outputp_0.adm ~/DBIS/data/wiscondef16gb.adm
wait
java -jar ./target/wisconsin-datagen.jar writer=file workload=Default.json  filesize=32768
wait
cp ./outputp_0.adm ~/DBIS/data/wiscondef32gb.adm
wait
java -jar ./target/wisconsin-datagen.jar writer=file workload=Default.json  filesize=65536
wait
cp ./outputp_0.adm ~/DBIS/data/wiscondef64gb.adm
