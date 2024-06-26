import requests

url = "http://10.16.229.109:19002/query/service"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Define data for the query
data = {
"statement": "drop dataverse wiscon2gb if exists; create dataverse wiscon2gb;USE wiscon2gb;CREATE TYPE wiscondeftype AS {unique1: int,unique2: int,two: int,four:int,ten:int,twenty:int,onePercent:int,tenPercent:int,twentyPercent:int,fiftyPercent: int,unique3:int,evenOnePercent:int,oddOnePercent:int,stringu1: string,stringu2: string,string4:string};CREATE DATASET wiscondef2gb(wiscondeftype) PRIMARY KEY unique2;LOAD DATASET wiscondef2gb USING localfs (('path' = '10.16.229.110:///home/dbis-nuc10/DBIS/data/wiscondef2gb.adm'),  ('format' = 'adm'));",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)

data = {
"statement": "drop dataverse wiscon4gb if exists; create dataverse wiscon4gb;USE wiscon4gb;CREATE TYPE wiscondeftype AS {unique1: int,unique2: int,two: int,four:int,ten:int,twenty:int,onePercent:int,tenPercent:int,twentyPercent:int,fiftyPercent: int,unique3:int,evenOnePercent:int,oddOnePercent:int,stringu1: string,stringu2: string,string4:string};CREATE DATASET wiscondef4gb(wiscondeftype) PRIMARY KEY unique2;LOAD DATASET wiscondef4gb USING localfs (('path' = '10.16.229.110:///home/dbis-nuc10/DBIS/data/wiscondef4gb.adm'),  ('format' = 'adm'));",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)

data = {
"statement": "drop dataverse wiscon8gb if exists; create dataverse wiscon8gb;USE wiscon8gb;CREATE TYPE wiscondeftype AS {unique1: int,unique2: int,two: int,four:int,ten:int,twenty:int,onePercent:int,tenPercent:int,twentyPercent:int,fiftyPercent: int,unique3:int,evenOnePercent:int,oddOnePercent:int,stringu1: string,stringu2: string,string4:string};CREATE DATASET wiscondef8gb(wiscondeftype) PRIMARY KEY unique2;LOAD DATASET wiscondef8gb USING localfs (('path' = '10.16.229.110:///home/dbis-nuc10/DBIS/data/wiscondef8gb.adm'),  ('format' = 'adm'));",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)

data = {
"statement": "drop dataverse wiscon16gb if exists; create dataverse wiscon16gb;USE wiscon16gb;CREATE TYPE wiscondeftype AS {unique1: int,unique2: int,two: int,four:int,ten:int,twenty:int,onePercent:int,tenPercent:int,twentyPercent:int,fiftyPercent: int,unique3:int,evenOnePercent:int,oddOnePercent:int,stringu1: string,stringu2: string,string4:string};CREATE DATASET wiscondef16gb(wiscondeftype) PRIMARY KEY unique2;LOAD DATASET wiscondef16gb USING localfs (('path' = '10.16.229.110:///home/dbis-nuc10/DBIS/data/wiscondef16gb.adm'),  ('format' = 'adm'));",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)

data = {
"statement": "drop dataverse wiscon32gb if exists; create dataverse wiscon32gb;USE wiscon32gb;CREATE TYPE wiscondeftype AS {unique1: int,unique2: int,two: int,four:int,ten:int,twenty:int,onePercent:int,tenPercent:int,twentyPercent:int,fiftyPercent: int,unique3:int,evenOnePercent:int,oddOnePercent:int,stringu1: string,stringu2: string,string4:string};CREATE DATASET wiscondef32gb(wiscondeftype) PRIMARY KEY unique2;LOAD DATASET wiscondef32gb USING localfs (('path' = '10.16.229.110:///home/dbis-nuc10/DBIS/data/wiscondef32gb.adm'),  ('format' = 'adm'));",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)

data = {
"statement": "drop dataverse wiscon64gb if exists; create dataverse wiscon64gb;USE wiscon64gb;CREATE TYPE wiscondeftype AS {unique1: int,unique2: int,two: int,four:int,ten:int,twenty:int,onePercent:int,tenPercent:int,twentyPercent:int,fiftyPercent: int,unique3:int,evenOnePercent:int,oddOnePercent:int,stringu1: string,stringu2: string,string4:string};CREATE DATASET wiscondef64gb(wiscondeftype) PRIMARY KEY unique2;LOAD DATASET wiscondef64gb USING localfs (('path' = '10.16.229.110:///home/dbis-nuc10/DBIS/data/wiscondef64gb.adm'),  ('format' = 'adm'));",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)