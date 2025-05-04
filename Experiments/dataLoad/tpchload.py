# Loading the TPC-H benchmark data into a database
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


create type lineitemtype as {
  l_orderkey: int64,
  l_partkey: int64,
  l_suppkey: int64,
  l_linenumber: int64,
  l_quantity: int32,
  l_extendedprice: double,
  l_discount: double,
  l_tax: double,
  l_returnflag: string,
  l_linestatus: string,
  l_shipdate: string,
  l_commitdate: string,
  l_receiptdate: string,
  l_shipinstruct: string,
  l_shipmode: string,
  l_comment: string
};

create type ordertype as {
  o_orderkey: int64,
  o_custkey: int64,
  o_orderstatus: string,
  o_totalprice: double,
  o_orderdate: string,
  o_orderpriority: string,
  o_clerk: string,
  o_shippriority: int32,
  o_comment: string
};

create type customertype as {
  c_custkey: int64,
  c_name: string,
  c_address: string,
  c_nationkey: int32,
  c_phone: string,
  c_acctbal: double,
  c_mktsegment: string,
  c_comment: string
};

create type parttype as {
  p_partkey: int64,
  p_name: string,
  p_mfgr: string,
  p_brand: string,
  p_type: string,
  p_size: int32,
  p_container: string,
  p_retailprice: double,
  p_comment: string
};

create type partsupptype as {
  ps_partkey: int64,
  ps_suppkey: int64,
  ps_availqty: int32,
  ps_supplycost: double,
  ps_comment: string
};

create type suppliertype as {
  s_suppkey: int64,
  s_name: string,
  s_address: string,
  s_nationkey: int32,
  s_phone: string,
  s_acctbal: double,
  s_comment: string
};

create type nationtype as {
  n_nationkey: int32,
  n_name: string,
  n_regionkey: int32,
  n_comment: string
};

create type regiontype as {
  r_regionkey: int32,
  r_name: string,
  r_comment: string
};

create dataset lineitem(lineitemtype) primary key l_orderkey, l_linenumber;
create dataset orders(ordertype)      primary key o_orderkey;
create dataset customer(customertype) primary key c_custkey;
create dataset part(parttype)         primary key p_partkey;
create dataset partsupp(partsupptype) primary key ps_partkey, ps_suppkey;
create dataset supplier(suppliertype) primary key s_suppkey;
create dataset region(regiontype)     primary key r_regionkey;
create dataset nation(nationtype)     primary key n_nationkey;

load dataset lineitem using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpch/lineitem.tbl`),(`format`=`delimited-text`),(`delimiter`=`|`));
load dataset orders using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpch/orders.tbl`),(`format`=`delimited-text`),(`delimiter`=`|`));
load dataset customer using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpch/customer.tbl`),(`format`=`delimited-text`),(`delimiter`=`|`));
load dataset part using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpch/part.tbl`),(`format`=`delimited-text`),(`delimiter`=`|`));
load dataset partsupp using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpch/partsupp.tbl`),(`format`=`delimited-text`),(`delimiter`=`|`));
load dataset supplier using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpch/supplier.tbl`),(`format`=`delimited-text`),(`delimiter`=`|`));
load dataset region using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpch/region.tbl`),(`format`=`delimited-text`),(`delimiter`=`|`));
load dataset nation using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpch/nation.tbl`),(`format`=`delimited-text`),(`delimiter`=`|`));
''',
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)
