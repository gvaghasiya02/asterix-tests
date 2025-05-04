echo "wisconsin data generation"
cd ~/DBIS/JSON-Wisconsin-Data-Generator
java -jar ./target/wisconsin-datagen.jar writer=file workload=final.json  filesize=2048
wait
cp ./outputp_0.adm ~/DBIS/data/wiscon_moregroups_2gb.adm
wait
java -jar ./target/wisconsin-datagen.jar writer=file workload=final.json  filesize=4096
wait
cp ./outputp_0.adm ~/DBIS/data/wiscon_moregroups_4gb.adm
wait
java -jar ./target/wisconsin-datagen.jar writer=file workload=final.json  filesize=8192
wait
cp ./outputp_0.adm ~/DBIS/data/wiscon_moregroups_8gb.adm
wait
java -jar ./target/wisconsin-datagen.jar writer=file workload=final.json  filesize=16384
wait
cp ./outputp_0.adm ~/DBIS/data/wiscon_moregroups_16gb.adm
wait
java -jar ./target/wisconsin-datagen.jar writer=file workload=final.json  filesize=32768
wait
cp ./outputp_0.adm ~/DBIS/data/wiscon_moregroups_32gb.adm
wait
java -jar ./target/wisconsin-datagen.jar writer=file workload=final.json  filesize=65536
wait
cp ./outputp_0.adm ~/DBIS/data/wiscon_moregroups_64gb.adm
wait
java -jar ./target/wisconsin-datagen.jar writer=file workload=final.json  cardinality=1000000
wait
cp ./outputp_0.adm ~/DBIS/data/wiscon_moregroups_106.adm
wait
java -jar ./target/wisconsin-datagen.jar writer=file workload=final.json  cardinality=10000000
wait
cp ./outputp_0.adm ~/DBIS/data/wiscon_moregroups_107.adm
wait
java -jar ./target/wisconsin-datagen.jar writer=file workload=final.json  cardinality=100000000
wait
cp ./outputp_0.adm ~/DBIS/data/wiscon_moregroups_108.adm
