# Loads the TPC-DS dataset
import requests

url = "http://localhost:19002/query/service"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Define data for the query
data = {
    "statement": '''
drop dataverse tpcds if exists;
create dataverse tpcds;

use tpcds;


create type tpcds.store_returns_type as
  {
  sr_returned_date_sk : int64?,
  sr_return_time_sk : int64?,
  sr_item_sk : int64,
  sr_customer_sk : int64?,
  sr_cdemo_sk : int64?,
  sr_hdemo_sk : int64?,
  sr_addr_sk : int64?,
  sr_store_sk : int64?,
  sr_reason_sk : int64?,
  sr_ticket_number : int64,
  sr_return_quantity : int64?,
  sr_return_amt : double,
  sr_return_tax : double?,
  sr_return_amt_inc_tax : double?,
  sr_fee : double?,
  sr_return_ship_cost : double?,
  sr_refunded_cash : double?,
  sr_reversed_charge : double?,
  sr_store_credit : double?,
  sr_net_loss : double?
};

create dataset store_returns(store_returns_type) primary key sr_item_sk, sr_ticket_number;

load dataset store_returns using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpcds/store_returns.dat`),(`format`=`delimited-text`),(`delimiter`=`|`),(`null`=""));


create type tpcds.date_dim_type as
  {
  d_date_sk : int64,
  d_date_id : string,
  d_date : string?,
  d_month_seq : int64?,
  d_week_seq : int64?,
  d_quarter_seq : int64?,
  d_year : int64? ,
  d_dow : int64? ,
  d_moy : int64?,
  d_dom : int64?,
  d_qoy : int64?,
  d_fy_year : int64?,
  d_fy_quarter_seq : int64?,
  d_fy_week_seq : int64?,
  d_day_name : string?,
  d_quarter_name : string?,
  d_holiday : string?,
  d_weekend : string?,
  d_following_holiday : string?,
  d_first_dom : int64?,
  d_last_dom : int64?,
  d_same_day_ly : int64?,
  d_same_day_lq : int64?,
  d_current_day : string?,
  d_current_week : string?,
  d_current_month : string?,
  d_current_quarter : string?,
  d_current_year : string?
};

create dataset date_dim(date_dim_type) primary key d_date_sk;

load dataset date_dim using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpcds/date_dim.dat`),(`format`=`delimited-text`),(`delimiter`=`|`),(`null`=""));


create type tpcds.store_type as
  {
  s_store_sk : int64,
  s_store_id : string,
  s_rec_start_date : string?,
  s_rec_end_date : string?,
  s__date_sk : int64?,
  s_store_name : string?,
  s_number_employees : int64?,
  s_floor_space : int64?,
  s_hours : string?,
  s_manager : string?,
  s_market_id : int64?,
  s_geography_class : string?,
  s_market_desc : string?,
  s_market_manager : string?,
  s_division_id : int64?,
  s_division_name : string?,
  s_company_id : int64?,
  s_company_name : string?,
  s_street_number : string?,
  s_street_name : string?,
  s_street_type : string?,
  s_suite_number : string?,
  s_city : string?,
  s_county : string?,
  s_state : string?,
  s_zip : string?,
  s_country : string?,
  s_gmt_offset : double?,
  s_tax_precentage : double?
};

create dataset store(store_type) primary key s_store_sk;

load dataset store using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpcds/store.dat`),(`format`=`delimited-text`),(`delimiter`=`|`),(`null`=""));


create type tpcds.customer_type as
  {
  c_customer_sk : int64,
  c_customer_id : string,
  c_current_cdemo_sk : int64?,
  c_current_hdemo_sk : int64?,
  c_current_addr_sk : int64?,
  c_first_shipto_date_sk : int64?,
  c_first_sales_date_sk : int64?,
  c_salutation : string?,
  c_first_name : string?,
  c_last_name : string?,
  c_preferred_cust_flag : string?,
  c_birth_day : int64?,
  c_birth_month : int64?,
  c_birth_year : int64?,
  c_birth_country : string?,
  c_login : string?,
  c_email_address : string?,
  c_last_review_date : string?
};

create dataset customer(customer_type) primary key c_customer_sk;

load dataset customer using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpcds/customer.dat`),(`format`=`delimited-text`),(`delimiter`=`|`),(`null`=""));


create type tpcds.item_type as
  {
  i_item_sk : bigint,
  i_item_id : string,
  i_rec_start_date : string?,
  i_rec_end_date : string?,
  i_item_desc : string?,
  i_current_price : double?,
  i_wholesale_cost : double?,
  i_brand_id : bigint?,
  i_brand : string?,
  i_class_id : bigint?,
  i_class : string?,
  i_category_id : bigint?,
  i_category : string?,
  i_manufact_id : bigint?,
  i_manufact : string?,
  i_size : string?,
  i_formulation : string?,
  i_color : string?,
  i_units : string?,
  i_container : string?,
  i_manager_id : bigint?,
  i_product_name : string?
};

create dataset item(item_type) primary key i_item_sk;

load dataset item using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpcds/item.dat`),(`format`=`delimited-text`),(`delimiter`=`|`),(`null`=""));


create type tpcds.store_sales_type as
  {
  ss_sold_date_sk:           bigint?,
  ss_sold_time_sk:           bigint?,
  ss_item_sk:                bigint,
  ss_customer_sk:            bigint?,
  ss_cdemo_sk:               bigint?,
  ss_hdemo_sk:               bigint?,
  ss_addr_sk:                bigint?,
  ss_store_sk:               bigint?,
  ss_promo_sk:               bigint?,
  ss_ticket_number:          bigint,
  ss_quantity:               bigint?,
  ss_wholesale_cost:         double?,
  ss_list_price:             double?,
  ss_sales_price:            double?,
  ss_ext_discount_amt:       double?,
  ss_ext_sales_price:        double?,
  ss_ext_wholesale_cost:     double?,
  ss_ext_list_price:         double?,
  ss_ext_tax:                double?,
  ss_coupon_amt:             double?,
  ss_net_paid:               double?,
  ss_net_paid_inc_tax:       double?,
  ss_net_profit:             double?
};

create dataset store_sales(store_sales_type) primary key ss_item_sk, ss_ticket_number;

load dataset store_sales using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpcds/store_sales.dat`),(`format`=`delimited-text`),(`delimiter`=`|`),(`null`=""));


create type tpcds.catalog_page_type as
  {
  cp_catalog_page_sk:         bigint,
  cp_catalog_page_id:         string,
  cp_start_date_sk:           bigint?,
  cp_end_date_sk:             bigint?,
  cp_department:              string?,
  cp_catalog_number:          bigint?,
  cp_catalog_page_number:     bigint?,
  cp_description:             string?,
  cp_type:                    string?
};

create dataset catalog_page(catalog_page_type) primary key cp_catalog_page_sk;

load dataset catalog_page using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpcds/catalog_page.dat`),(`format`=`delimited-text`),(`delimiter`=`|`),(`null`=""));


create type tpcds.catalog_sales_type as
  {
  cs_sold_date_sk:           bigint?,
  cs_sold_time_sk:           bigint?,
  cs_ship_date_sk:           bigint?,
  cs_bill_customer_sk:       bigint?,
  cs_bill_cdemo_sk:          bigint?,
  cs_bill_hdemo_sk:          bigint?,
  cs_bill_addr_sk:           bigint?,
  cs_ship_customer_sk:       bigint?,
  cs_ship_cdemo_sk:          bigint?,
  cs_ship_hdemo_sk:          bigint?,
  cs_ship_addr_sk:           bigint?,
  cs_call_center_sk:         bigint?,
  cs_catalog_page_sk:        bigint?,
  cs_ship_mode_sk:           bigint?,
  cs_warehouse_sk:           bigint?,
  cs_item_sk:                bigint,
  cs_promo_sk:               bigint?,
  cs_order_number:           bigint,
  cs_quantity:               bigint?,
  cs_wholesale_cost:         double?,
  cs_list_price:             double?,
  cs_sales_price:            double?,
  cs_ext_discount_amt:       double?,
  cs_ext_sales_price:        double?,
  cs_ext_wholesale_cost:     double?,
  cs_ext_list_price:         double?,
  cs_ext_tax:                double?,
  cs_coupon_amt:             double?,
  cs_ext_ship_cost:          double?,
  cs_net_paid:               double?,
  cs_net_paid_inc_tax:       double?,
  cs_net_paid_inc_ship:      double?,
  cs_net_paid_inc_ship_tax:  double?,
  cs_net_profit:             double?
};

create dataset catalog_sales(catalog_sales_type) primary key cs_item_sk, cs_order_number;

load dataset catalog_sales using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpcds/catalog_sales.dat`),(`format`=`delimited-text`),(`delimiter`=`|`),(`null`=""));


create type tpcds.catalog_returns_type as
  {
  cr_returned_date_sk : bigint?,
  cr_returned_time_sk : bigint?,
  cr_item_sk : bigint,
  cr_refunded_customer_sk : bigint?,
  cr_refunded_cdemo_sk : bigint?,
  cr_refunded_hdemo_sk : bigint?,
  cr_refunded_addr_sk : bigint?,
  cr_returning_customer_sk : bigint?,
  cr_returning_cdemo_sk : bigint?,
  cr_returning_hdemo_sk : bigint?,
  cr_returning_addr_sk : bigint?,
  cr_call_center_sk : bigint?,
  cr_catalog_page_sk : bigint?,
  cr_ship_mode_sk : bigint?,
  cr_warehouse_sk : bigint?,
  cr_reason_sk : bigint?,
  cr_order_number : bigint,
  cr_return_quantity : bigint?,
  cr_return_amount : double?,
  cr_return_tax : double?,
  cr_return_amt_inc_tax : double?,
  cr_fee : double?,
  cr_return_ship_cost : double?,
  cr_refunded_cash : double?,
  cr_reversed_charge : double?,
  cr_store_credit : double?,
  cr_net_loss : double?
};

create dataset catalog_returns(catalog_returns_type) primary key cr_item_sk, cr_order_number;

load dataset catalog_returns using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpcds/catalog_returns.dat`),(`format`=`delimited-text`),(`delimiter`=`|`),(`null`=""));


create type tpcds.web_site_type as
  {
  web_site_sk:               bigint,
  web_site_id:               string,
  web_rec_start_date:        string?,
  web_rec_end_date:          string?,
  web_name:                  string?,
  web_open_date_sk:          bigint?,
  web_close_date_sk:         bigint?,
  web_class:                 string?,
  web_manager:               string?,
  web_mkt_id:                bigint?,
  web_mkt_class:             string?,
  web_mkt_desc:              string?,
  web_market_manager:        string?,
  web_company_id:            bigint?,
  web_company_name:          string?,
  web_street_number:         string?,
  web_street_name:           string?,
  web_street_type:           string?,
  web_suite_number:          string?,
  web_city:                  string?,
  web_county:                string?,
  web_state:                 string?,
  web_zip:                   string?,
  web_country:               string?,
  web_gmt_offset:            double?,
  web_tax_percentage:        double?
};

create dataset web_site(web_site_type) primary key web_site_sk;

load dataset web_site using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpcds/web_site.dat`),(`format`=`delimited-text`),(`delimiter`=`|`),(`null`=""));


create type tpcds.web_sales_type as
  {
  ws_sold_date_sk : int64?,
  ws_sold_time_sk : int64?,
  ws_ship_date_sk : int64?,
  ws_item_sk : int64,
  ws_bill_customer_sk : int64?,
  ws_bill_cdemo_sk : int64?,
  ws_bill_hdemo_sk : int64?,
  ws_bill_addr_sk : int64?,
  ws_ship_customer_sk : int64?,
  ws_ship_cdemo_sk : int64?,
  ws_ship_hdemo_sk : int64?,
  ws_ship_addr_sk : int64?,
  ws_web_page_sk : int64?,
  ws_web_site_sk : int64?,
  ws_ship_mode_sk : int64?,
  ws_warehouse_sk : int64?,
  ws_promo_sk : int64?,
  ws_order_number : int64,
  ws_quantity : int64?,
  ws_wholesale_cost : double?,
  ws_list_price : double?,
  ws_sales_price : double?,
  ws_ext_discount_amt : double?,
  ws_ext_sales_price : double?,
  ws_ext_wholesale_cost : double?,
  ws_ext_list_price : double?,
  ws_ext_tax : double?,
  ws_coupon_amt : double?,
  ws_ext_ship_cost : double?,
  ws_net_paid : double?,
  ws_net_paid_inc_tax : double?,
  ws_net_paid_inc_ship : double?,
  ws_net_paid_inc_ship_tax : double?,
  ws_net_profit : double?
};

create dataset web_sales(web_sales_type) primary key ws_item_sk, ws_order_number;

load dataset web_sales using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpcds/web_sales.dat`),(`format`=`delimited-text`),(`delimiter`=`|`),(`null`=""));


create type tpcds.web_returns_type as
  {
  wr_returned_date_sk : bigint?,
  wr_returned_time_sk : bigint?,
  wr_item_sk : bigint,
  wr_refunded_customer_sk : bigint?,
  wr_refunded_cdemo_sk : bigint?,
  wr_refunded_hdemo_sk : bigint?,
  wr_refunded_addr_sk : bigint?,
  wr_returning_customer_sk : bigint?,
  wr_returning_cdemo_sk : bigint?,
  wr_returning_hdemo_sk : bigint?,
  wr_returning_addr_sk : bigint?,
  wr_web_page_sk : bigint?,
  wr_reason_sk : bigint?,
  wr_order_number : bigint,
  wr_return_quantity : bigint?,
  wr_return_amt : double?,
  wr_return_tax : double?,
  wr_return_amt_inc_tax : double?,
  wr_fee : double?,
  wr_return_ship_cost: double?,
  wr_refunded_cash: double?,
  wr_reversed_charge: double?,
  wr_account_credit: double?,
  wr_net_loss: double?
};

create dataset web_returns(web_returns_type) primary key wr_item_sk, wr_order_number;

load dataset web_returns using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpcds/web_returns.dat`),(`format`=`delimited-text`),(`delimiter`=`|`),(`null`=""));


create type tpcds.customer_demographics_type as
  {
  cd_demo_sk : bigint,
  cd_gender : string?,
  cd_marital_status : string?,
  cd_education_status : string?,
  cd_purchase_estimate : bigint?,
  cd_credit_rating : string?,
  cd_dep_count : bigint?,
  cd_dep_employed_count : bigint?,
  cd_dep_college_count : bigint?
};

create dataset customer_demographics(customer_demographics_type) primary key cd_demo_sk;

load dataset customer_demographics using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpcds/customer_demographics.dat`),(`format`=`delimited-text`),(`delimiter`=`|`),(`null`=""));


create type tpcds.promotion_type as
  {
  p_promo_sk : bigint,
  p_promo_id : string,
  p_start_date_sk : bigint?,
  p_end_date_sk : bigint?,
  p_item_sk : bigint?,
  p_cost : double?,
  p_response_target : bigint?,
  p_promo_name : string?,
  p_channel_dmail : string?,
  p_channel_email : string?,
  p_channel_catalog : string?,
  p_channel_tv : string?,
  p_channel_radio : string?,
  p_channel_press : string?,
  p_channel_event : string?,
  p_channel_demo :  string?,
  p_channel_details : string?,
  p_purpose : string?,
  p_discount_active : string?
};

create dataset promotion(promotion_type) primary key p_promo_sk;

load dataset promotion using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpcds/promotion.dat`),(`format`=`delimited-text`),(`delimiter`=`|`),(`null`=""));


create type tpcds.reason_type as
  {
  r_reason_sk : int64,
  r_reason_id : string,
  r_reason_desc : string?
};

create dataset reason(reason_type) primary key r_reason_sk;

load dataset reason using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpcds/reason.dat`),(`format`=`delimited-text`),(`delimiter`=`|`),(`null`=""));


create type tpcds.customer_address_type as   {
  ca_address_sk : bigint,
  ca_address_id : string,
  ca_street_number : string?,
  ca_street_name : string?,
  ca_street_type : string?,
  ca_suite_number : string?,
  ca_city : string?,
  ca_county : string?,
  ca_state : string?,
  ca_zip : string?,
  ca_country : string?,
  ca_gmt_offset : double?,
  ca_location_type : string?
 };

create dataset customer_address(customer_address_type) primary key ca_address_sk;

load dataset customer_address using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpcds/customer_address.dat`),(`format`=`delimited-text`),(`delimiter`=`|`),(`null`=""));


create type tpcds.call_center_type as
  {
  cc_call_center_sk : bigint,
  cc_call_center_id : string,
  cc_rec_start_date : string?,
  cc_rec_end_date : string?,
  cc__date_sk : bigint?,
  cc_open_date_sk : bigint?,
  cc_name : string?,
  cc_class : string?,
  cc_employees : bigint?,
  cc_sq_ft : bigint?,
  cc_hours : string?,
  cc_manager : string?,
  cc_mkt_id : bigint?,
  cc_mkt_class : string?,
  cc_mkt_desc : string?,
  cc_market_manager : string?,
  cc_division : bigint?,
  cc_division_name : string?,
  cc_company : bigint?,
  cc_company_name : string?,
  cc_street_number : bigint?,
  cc_street_name : string?,
  cc_street_type : string?,
  cc_suite_number : string?,
  cc_city : string?,
  cc_county : string?,
  cc_state : string?,
  cc_zip : string?,
  cc_country : string?,
  cc_gmt_offset : double?,
  cc_tax_percentage : double?
};

create dataset call_center(call_center_type) primary key cc_call_center_sk;

load dataset call_center using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpcds/call_center.dat`),(`format`=`delimited-text`),(`delimiter`=`|`),(`null`=""));


create type tpcds.household_demographics_type as
  {
  hd_demo_sk : bigint,
  hd_income_band_sk : bigint?,
  hd_buy_potential : string?,
  hd_dep_count : bigint?,
  hd_vehicle_count : bigint?
};

create dataset household_demographics(household_demographics_type) primary key hd_demo_sk;

load dataset household_demographics using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpcds/household_demographics.dat`),(`format`=`delimited-text`),(`delimiter`=`|`),(`null`=""));


create type tpcds.inventory_type as
  {
  inv_date_sk : bigint,
  inv_item_sk : bigint,
  inv_warehouse_sk : bigint,
  inv_quantity_on_hand : bigint?
};

create dataset inventory(inventory_type) primary key inv_date_sk, inv_item_sk, inv_warehouse_sk;

load dataset inventory using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpcds/inventory.dat`),(`format`=`delimited-text`),(`delimiter`=`|`),(`null`=""));


create type tpcds.ship_mode_type as
  {
  sm_ship_mode_sk : bigint,
  sm_ship_mode_id : string,
  sm_type : string?,
  sm_code : string?,
  sm_carrier : string?,
  sm_contract : string?
};

create dataset ship_mode(ship_mode_type) primary key sm_ship_mode_sk;

load dataset ship_mode using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpcds/ship_mode.dat`),(`format`=`delimited-text`),(`delimiter`=`|`),(`null`=""));


create type tpcds.time_dim_type as
  {
  t_time_sk : bigint,
  t_time_id : string,
  t_time : bigint?,
  t_hour : bigint?,
  t_minute : bigint?,
  t_second : bigint?,
  t_am_pm : string?,
  t_shift : string?,
  t_sub_shift : string?,
  t_meal_time : string?
};

create dataset time_dim(time_dim_type) primary key t_time_sk;

load dataset time_dim using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpcds/time_dim.dat`),(`format`=`delimited-text`),(`delimiter`=`|`),(`null`=""));


create type tpcds.warehouse_type as
  {
  w_warehouse_sk : bigint,
  w_warehouse_id : string,
  w_warehouse_name : string?,
  w_warehouse_sq_ft : bigint?,
  w_street_number : string?,
  w_street_name : string?,
  w_street_type : string?,
  w_suite_number : string?,
  w_city : string?,
  w_county : string?,
  w_state : string?,
  w_zip : string?,
  w_country : string?,
  w_gmt_offset : double?
};

create dataset warehouse(warehouse_type) primary key w_warehouse_sk;

load dataset warehouse using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpcds/warehouse.dat`),(`format`=`delimited-text`),(`delimiter`=`|`),(`null`=""));


create type tpcds.web_page_type as
  {
  wp_web_page_sk : int64,
  wp_web_page_id : string,
  wp_rec_start_date : string?,
  wp_rec_end_date : string?,
  wp_creation_date_sk : int64?,
  wp_access_date_sk : int64?,
  wp_autogen_flag : string?,
  wp_customer_sk : int64?,
  wp_url : string?,
  wp_type : string?,
  wp_char_count : int64?,
  wp_link_count : int64?,
  wp_image_count : int64?,
  wp_max_ad_count : int64?
};

create dataset web_page(web_page_type) primary key wp_web_page_sk;

load dataset web_page using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpcds/web_page.dat`),(`format`=`delimited-text`),(`delimiter`=`|`),(`null`=""));


create type tpcds.income_band_type as
     {    
        ib_income_band_sk : int64,
        ib_lower_bound : int64?,
        ib_upper_bound : int64?
    };

create dataset income_band(income_band_type) primary key ib_income_band_sk;

load dataset income_band using localfs ((`path`=`localhost:///home/dbis-nuc10/DBIS/data/benchmark/tpcds/income_band.dat`),(`format`=`delimited-text`),(`delimiter`=`|`),(`null`=""));


''',
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)
