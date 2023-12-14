cd ~/DBIS
wait
echo "pulling asterix"
cd ./asterixdb_gaurav
git pull
git checkout fall
mvn clean package -DskipTests
cd ..
wait
echo "pulling datagen"
cd ./JSON-Wisconsin-Data-Generator
mvn clean package
cd ..

