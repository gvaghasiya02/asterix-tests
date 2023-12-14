echo "wisconsin data generation"
cd ~/DBIS/JSON-Wisconsin-Data-Generator
java -jar ./target/wisconsin-datagen.jar writer=file workload=Default.json  cardinality=$1
wait
cd ~/DBIS
cp ./JSON-Wisconsin-Data-Generator/outputp_0.adm ./data/wiscondatadef.adm
wait
rm ./JSON-Wisconsin-Data-Generator/outputp_0.adm
pwd


