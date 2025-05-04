# Loading Wiscon data into a dataset with data types defined
import requests

url = "http://localhost:19002/query/service"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Define data for the query
data = {
"statement": "drop dataverse wiscon2gb if exists; create dataverse wiscon2gb;USE wiscon2gb;CREATE TYPE wiscondeftype AS {unique1: int,unique2: int,unique3: int,two: int,four:int,five:int,ten:int,twenty:int,hundred:int,kgroups:int,tenkgroups:int,hundredkgroups:int,milliongroups:int,stringu1: string,stringu2: string,normalsmallstring:string,normallargestring:string,similarstring:string,similarsmallstring:string,variablelengthstring:string};CREATE DATASET wiscondef2gb(wiscondeftype) PRIMARY KEY unique2 with {'storage-block-compression': {'scheme': 'none'}};LOAD DATASET wiscondef2gb USING localfs (('path' = 'localhost:///home/dbis-nuc10/DBIS/data/wiscon_moregroups_2gb.adm'),  ('format' = 'adm'));",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)

# Define data for the query
data = {
"statement": "drop dataverse wiscon4gb if exists; create dataverse wiscon4gb;USE wiscon4gb;CREATE TYPE wiscondeftype AS {unique1: int,unique2: int,unique3: int,two: int,four:int,five:int,ten:int,twenty:int,hundred:int,kgroups:int,tenkgroups:int,hundredkgroups:int,milliongroups:int,stringu1: string,stringu2: string,normalsmallstring:string,normallargestring:string,similarstring:string,similarsmallstring:string,variablelengthstring:string};CREATE DATASET wiscondef4gb(wiscondeftype) PRIMARY KEY unique2 with {'storage-block-compression': {'scheme': 'none'}};LOAD DATASET wiscondef4gb USING localfs (('path' = 'localhost:///home/dbis-nuc10/DBIS/data/wiscon_moregroups_4gb.adm'),  ('format' = 'adm'));",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)

# Define data for the query
data = {
"statement": "drop dataverse wiscon8gb if exists; create dataverse wiscon8gb;USE wiscon8gb;CREATE TYPE wiscondeftype AS {unique1: int,unique2: int,unique3: int,two: int,four:int,five:int,ten:int,twenty:int,hundred:int,kgroups:int,tenkgroups:int,hundredkgroups:int,milliongroups:int,stringu1: string,stringu2: string,normalsmallstring:string,normallargestring:string,similarstring:string,similarsmallstring:string,variablelengthstring:string};CREATE DATASET wiscondef8gb(wiscondeftype) PRIMARY KEY unique2 with {'storage-block-compression': {'scheme': 'none'}};LOAD DATASET wiscondef8gb USING localfs (('path' = 'localhost:///home/dbis-nuc10/DBIS/data/wiscon_moregroups_8gb.adm'),  ('format' = 'adm'));",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)

# Define data for the query
data = {
"statement": "drop dataverse wiscon16gb if exists; create dataverse wiscon16gb;USE wiscon16gb;CREATE TYPE wiscondeftype AS {unique1: int,unique2: int,unique3: int,two: int,four:int,five:int,ten:int,twenty:int,hundred:int,kgroups:int,tenkgroups:int,hundredkgroups:int,milliongroups:int,stringu1: string,stringu2: string,normalsmallstring:string,normallargestring:string,similarstring:string,similarsmallstring:string,variablelengthstring:string};CREATE DATASET wiscondef16gb(wiscondeftype) PRIMARY KEY unique2 with {'storage-block-compression': {'scheme': 'none'}};LOAD DATASET wiscondef16gb USING localfs (('path' = 'localhost:///home/dbis-nuc10/DBIS/data/wiscon_moregroups_16gb.adm'),  ('format' = 'adm'));",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)

# Define data for the query
data = {
"statement": "drop dataverse wiscon32gb if exists; create dataverse wiscon32gb;USE wiscon32gb;CREATE TYPE wiscondeftype AS {unique1: int,unique2: int,unique3: int,two: int,four:int,five:int,ten:int,twenty:int,hundred:int,kgroups:int,tenkgroups:int,hundredkgroups:int,milliongroups:int,stringu1: string,stringu2: string,normalsmallstring:string,normallargestring:string,similarstring:string,similarsmallstring:string,variablelengthstring:string};CREATE DATASET wiscondef32gb(wiscondeftype) PRIMARY KEY unique2 with {'storage-block-compression': {'scheme': 'none'}};LOAD DATASET wiscondef32gb USING localfs (('path' = 'localhost:///home/dbis-nuc10/DBIS/data/wiscon_moregroups_32gb.adm'),  ('format' = 'adm'));",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)

# Define data for the query
data = {
"statement": "drop dataverse wiscon64gb if exists; create dataverse wiscon64gb;USE wiscon64gb;CREATE TYPE wiscondeftype AS {unique1: int,unique2: int,unique3: int,two: int,four:int,five:int,ten:int,twenty:int,hundred:int,kgroups:int,tenkgroups:int,hundredkgroups:int,milliongroups:int,stringu1: string,stringu2: string,normalsmallstring:string,normallargestring:string,similarstring:string,similarsmallstring:string,variablelengthstring:string};CREATE DATASET wiscondef64gb(wiscondeftype) PRIMARY KEY unique2 with {'storage-block-compression': {'scheme': 'none'}};LOAD DATASET wiscondef64gb USING localfs (('path' = 'localhost:///home/dbis-nuc10/DBIS/data/wiscon_moregroups_64gb.adm'),  ('format' = 'adm'));",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)