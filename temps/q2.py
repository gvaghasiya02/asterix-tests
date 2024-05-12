import requests

url = "http://10.16.229.108:19002/query/service"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Define data for the query
data = {
"statement": "drop dataverse wiscon107 if exists; create dataverse wiscon107;USE wiscon107;CREATE TYPE wiscondeftype AS {unique1: int,unique2: int,unique3: int,two: int,four:int,five:int,ten:int,twenty:int,hundred:int,kgroups:int,tenkgroups:int,hundredkgroups:int,milliongroups:int,stringu1: string,stringu2: string,similarstring:string,variablelengthstring:string};CREATE DATASET wiscondef107(wiscondeftype) PRIMARY KEY unique2 with {'storage-block-compression': {'scheme': 'none'}};LOAD DATASET wiscondef107 USING localfs (('path' = '10.16.229.109:///home/dbis-nuc09/DBIS/data/wiscon_moregroups_107.adm'),  ('format' = 'adm'));",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)
