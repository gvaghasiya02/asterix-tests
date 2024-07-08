import requests

url = "http://10.16.229.110:19002/query/service"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Define data for the query
data = {
"statement": "drop dataverse wisconopen2gb if exists; create dataverse wisconopen2gb;USE wisconopen2gb;CREATE TYPE Opentype AS {unique2:int};CREATE DATASET wiscondefopen2gb(Opentype) PRIMARY KEY unique2 with {'storage-block-compression': {'scheme': 'none'}};copy wiscondefopen2gb from localfs path ('10.16.229.110:///home/dbis-nuc10/DBIS/data/wiscon_moregroups_2gb.adm') with {'format' = 'adm'};",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)

# Define data for the query
data = {
"statement": "drop dataverse wisconopen4gb if exists; create dataverse wisconopen4gb;USE wisconopen4gb;CREATE TYPE Opentype AS {unique2:int};CREATE DATASET wiscondefopen4gb(Opentype) PRIMARY KEY unique2 with {'storage-block-compression': {'scheme': 'none'}};copy wiscondefopen4gb from localfs path ('10.16.229.110:///home/dbis-nuc10/DBIS/data/wiscon_moregroups_4gb.adm') with {'format' = 'adm'};",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)

# Define data for the query
data = {
"statement": "drop dataverse wisconopen8gb if exists; create dataverse wisconopen8gb;USE wisconopen8gb;CREATE TYPE Opentype AS {unique2:int};CREATE DATASET wiscondefopen8gb(Opentype) PRIMARY KEY unique2 with {'storage-block-compression': {'scheme': 'none'}};copy wiscondefopen8gb from localfs path ('10.16.229.110:///home/dbis-nuc10/DBIS/data/wiscon_moregroups_8gb.adm') with {'format' = 'adm'};",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)

# Define data for the query
data = {
"statement": "drop dataverse wisconopen16gb if exists; create dataverse wisconopen16gb;USE wisconopen16gb;CREATE TYPE Opentype AS {unique2:int};CREATE DATASET wiscondefopen16gb(Opentype) PRIMARY KEY unique2 with {'storage-block-compression': {'scheme': 'none'}};copy wiscondefopen16gb from localfs path ('10.16.229.110:///home/dbis-nuc10/DBIS/data/wiscon_moregroups_16gb.adm') with {'format' = 'adm'};",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)

# Define data for the query
data = {
"statement": "drop dataverse wisconopen32gb if exists; create dataverse wisconopen32gb;USE wisconopen32gb;CREATE TYPE Opentype AS {unique2:int};CREATE DATASET wiscondefopen32gb(Opentype) PRIMARY KEY unique2 with {'storage-block-compression': {'scheme': 'none'}};copy wiscondefopen32gb from localfs path ('10.16.229.110:///home/dbis-nuc10/DBIS/data/wiscon_moregroups_32gb.adm') with {'format' = 'adm'};",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)

# Define data for the query
data = {
"statement": "drop dataverse wisconopen64gb if exists; create dataverse wisconopen64gb;USE wisconopen64gb;CREATE TYPE Opentype AS {unique2:int};CREATE DATASET wiscondefopen64gb(Opentype) PRIMARY KEY unique2 with {'storage-block-compression': {'scheme': 'none'}};copy wiscondefopen64gb from localfs path ('10.16.229.110:///home/dbis-nuc10/DBIS/data/wiscon_moregroups_64gb.adm') with {'format' = 'adm'};",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)