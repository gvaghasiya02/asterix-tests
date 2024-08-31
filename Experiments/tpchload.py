import requests

url = "http://localhost:19002/query/service"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Define data for the query
data = {
    "statement": '''
drop dataverse tpch if exists;
create dataverse tpch;
use tpch;

create type lineitemtype as open {id: uuid};

create type ordertype as open {id: uuid};

create type customertype as open {id: uuid};

create type parttype as  open {id: uuid};

create type partsupptype as open {id: uuid};

create type suppliertype as open {id: uuid};

create type nationtype as open {id: uuid};

create type regiontype as open {id: uuid};

create dataset lineitem(lineitemtype) primary key id autogenerated;
create dataset orders(ordertype)      primary key id autogenerated;
create dataset customer(customertype) primary key id autogenerated;
create dataset part(parttype)         primary key id autogenerated;
create dataset partsupp(partsupptype) primary key id autogenerated;
create dataset supplier(suppliertype) primary key id autogenerated;
create dataset region(regiontype)     primary key id autogenerated;
create dataset nation(nationtype)     primary key id autogenerated;

load dataset lineitem using localfs ((`path`=`10.16.229.110:///home/dbis-nuc10/DBIS/data/benchmark/tpch/lineitem.tbl`),(`format`=`delimited-text`),(`delimiter`=`|`));
load dataset orders using localfs ((`path`=`10.16.229.110:///home/dbis-nuc10/DBIS/data/benchmark/tpch/orders.tbl`),(`format`=`delimited-text`),(`delimiter`=`|`));
load dataset customer using localfs ((`path`=`10.16.229.110:///home/dbis-nuc10/DBIS/data/benchmark/tpch/customer.tbl`),(`format`=`delimited-text`),(`delimiter`=`|`));
load dataset part using localfs ((`path`=`10.16.229.110:///home/dbis-nuc10/DBIS/data/benchmark/tpch/part.tbl`),(`format`=`delimited-text`),(`delimiter`=`|`));
load dataset partsupp using localfs ((`path`=`10.16.229.110:///home/dbis-nuc10/DBIS/data/benchmark/tpch/partsupp.tbl`),(`format`=`delimited-text`),(`delimiter`=`|`));
load dataset supplier using localfs ((`path`=`10.16.229.110:///home/dbis-nuc10/DBIS/data/benchmark/tpch/supplier.tbl`),(`format`=`delimited-text`),(`delimiter`=`|`));
load dataset region using localfs ((`path`=`10.16.229.110:///home/dbis-nuc10/DBIS/data/benchmark/tpch/region.tbl`),(`format`=`delimited-text`),(`delimiter`=`|`));
load dataset nation using localfs ((`path`=`10.16.229.110:///home/dbis-nuc10/DBIS/data/benchmark/tpch/nation.tbl`),(`format`=`delimited-text`),(`delimiter`=`|`));
''',
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)
