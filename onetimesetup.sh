cd ~/DBIS
sudo apt install maven python3 git
mvn --version
python3 --version
git --version
wait
rm -rf asterixdb_gaurav data JSON-Wisconsin-Data-Generator
echo "cloning datagen"
git clone https://github.com/shivajah/JSON-Wisconsin-Data-Generator.git
wait
mkdir data
echo "cloning asterixdb"
git clone https://github.com/gvaghasiya02/asterixdb_gaurav.git
wait
ls -l