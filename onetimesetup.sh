cd ~/DBIS
suso apt install maven python3 git
mvn --version
python3 --version
git --version
wait
rm -r asterixdb data JSON-Wisconsin-Data-Generator
echo "cloning asterixdb"
git clone https://github.com/gvaghasiya02/asterixdb_gaurav.git
wait 
echo "cloning datagen"
git clone https://github.com/shivajah/JSON-Wisconsin-Data-Generator.git
wait
mkdir data


