import requests

url = "http://localhost:19002/query/service"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Define data for the query
data = {
"statement": "drop dataverse wisconsmall if exists; create dataverse wisconsmall;USE wisconsmall;CREATE TYPE wiscondeftype AS {unique1: int,unique2: int,two: int,four:int,ten:int,twenty:int,onePercent:int,tenPercent:int,twentyPercent:int,fiftyPercent: int,unique3:int,evenOnePercent:int,oddOnePercent:int,stringu1: string,stringu2: string,string4:string};CREATE DATASET wiscondefsmall(wiscondeftype) PRIMARY KEY unique2;LOAD DATASET wiscondefsmall USING localfs (('path' = 'localhost:///home/dbis-nuc10/DBIS/data/wiscondef107.adm'),  ('format' = 'adm'));",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)