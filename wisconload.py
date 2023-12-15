import requests
import csv

url = "http://localhost:19002/query/service"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}


csv_filename = "query_metrics.csv"

# Define data for the query
data = {
"statement": "drop dataverse wiscon if exists; create dataverse wiscon;USE wiscon;CREATE TYPE wiscondeftype AS {unique1: int,unique2: int,two: int,four:int,ten:int,twenty:int,onePercent:int,tenPercent:int,twentyPercent:int,fiftyPercent: int,unique3:int,evenOnePercent:int,oddOnePercent:int,stringu1: string,stringu2: string,string4:string};CREATE DATASET wiscondef(wiscondeftype) PRIMARY KEY unique2;LOAD DATASET wiscondef USING localfs (('path' = 'localhost:///home/dbis-nuc10/DBIS/data/wiscondatadef.adm'),  ('format' = 'adm'));",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)