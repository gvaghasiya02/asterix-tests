#!/bin/bash

set -e

# --- CONFIGURATION ---
DB_NAME="tpcds"
DB_USER="postgres"
DATA_DIR="/home/dbis-nuc06/DBIS/data/benchmark/tpcds"
# ----------------------

echo "🧹 Dropping existing database (if exists)..."
sudo -u "$DB_USER" psql -tc "SELECT 1 FROM pg_database WHERE datname = '$DB_NAME'" | grep -q 1 &&
  sudo -u "$DB_USER" dropdb "$DB_NAME" &&
  echo "🗑️  Existing database '$DB_NAME' dropped." ||
  echo "ℹ️  No existing database to drop."

echo "🧱 Creating PostgreSQL database..."
sudo -u "$DB_USER" createdb "$DB_NAME"

echo "🗄️ Creating TPC-DS schema..."
sudo -u "$DB_USER" psql -d "$DB_NAME" <<EOF

CREATE TABLE store_returns (
  sr_returned_date_sk BIGINT,
  sr_return_time_sk BIGINT,
  sr_item_sk BIGINT,
  sr_customer_sk BIGINT,
  sr_cdemo_sk BIGINT,
  sr_hdemo_sk BIGINT,
  sr_addr_sk BIGINT,
  sr_store_sk BIGINT,
  sr_reason_sk BIGINT,
  sr_ticket_number BIGINT,
  sr_return_quantity BIGINT,
  sr_return_amt DOUBLE PRECISION,
  sr_return_tax DOUBLE PRECISION,
  sr_return_amt_inc_tax DOUBLE PRECISION,
  sr_fee DOUBLE PRECISION,
  sr_return_ship_cost DOUBLE PRECISION,
  sr_refunded_cash DOUBLE PRECISION,
  sr_reversed_charge DOUBLE PRECISION,
  sr_store_credit DOUBLE PRECISION,
  sr_net_loss DOUBLE PRECISION,
  PRIMARY KEY (sr_item_sk, sr_ticket_number)
);

CREATE TABLE date_dim (
  d_date_sk BIGINT,
  d_date_id TEXT,
  d_date TEXT,
  d_month_seq BIGINT,
  d_week_seq BIGINT,
  d_quarter_seq BIGINT,
  d_year BIGINT,
  d_dow BIGINT,
  d_moy BIGINT,
  d_dom BIGINT,
  d_qoy BIGINT,
  d_fy_year BIGINT,
  d_fy_quarter_seq BIGINT,
  d_fy_week_seq BIGINT,
  d_day_name TEXT,
  d_quarter_name TEXT,
  d_holiday TEXT,
  d_weekend TEXT,
  d_following_holiday TEXT,
  d_first_dom BIGINT,
  d_last_dom BIGINT,
  d_same_day_ly BIGINT,
  d_same_day_lq BIGINT,
  d_current_day TEXT,
  d_current_week TEXT,
  d_current_month TEXT,
  d_current_quarter TEXT,
  d_current_year TEXT,
  PRIMARY KEY (d_date_sk)
);

CREATE TABLE store (
  s_store_sk BIGINT,
  s_store_id TEXT,
  s_rec_start_date TEXT,
  s_rec_end_date TEXT,
  s__date_sk BIGINT,
  s_store_name TEXT,
  s_number_employees BIGINT,
  s_floor_space BIGINT,
  s_hours TEXT,
  s_manager TEXT,
  s_market_id BIGINT,
  s_geography_class TEXT,
  s_market_desc TEXT,
  s_market_manager TEXT,
  s_division_id BIGINT,
  s_division_name TEXT,
  s_company_id BIGINT,
  s_company_name TEXT,
  s_street_number TEXT,
  s_street_name TEXT,
  s_street_type TEXT,
  s_suite_number TEXT,
  s_city TEXT,
  s_county TEXT,
  s_state TEXT,
  s_zip TEXT,
  s_country TEXT,
  s_gmt_offset DOUBLE PRECISION,
  s_tax_precentage DOUBLE PRECISION,
  PRIMARY KEY (s_store_sk)
);

CREATE TABLE customer (
  c_customer_sk BIGINT,
  c_customer_id TEXT,
  c_current_cdemo_sk BIGINT,
  c_current_hdemo_sk BIGINT,
  c_current_addr_sk BIGINT,
  c_first_shipto_date_sk BIGINT,
  c_first_sales_date_sk BIGINT,
  c_salutation TEXT,
  c_first_name TEXT,
  c_last_name TEXT,
  c_preferred_cust_flag TEXT,
  c_birth_day BIGINT,
  c_birth_month BIGINT,
  c_birth_year BIGINT,
  c_birth_country TEXT,
  c_login TEXT,
  c_email_address TEXT,
  c_last_review_date TEXT,
  PRIMARY KEY (c_customer_sk)
);

CREATE TABLE item (
  i_item_sk BIGINT,
  i_item_id TEXT,
  i_rec_start_date TEXT,
  i_rec_end_date TEXT,
  i_item_desc TEXT,
  i_current_price DOUBLE PRECISION,
  i_wholesale_cost DOUBLE PRECISION,
  i_brand_id BIGINT,
  i_brand TEXT,
  i_class_id BIGINT,
  i_class TEXT,
  i_category_id BIGINT,
  i_category TEXT,
  i_manufact_id BIGINT,
  i_manufact TEXT,
  i_size TEXT,
  i_formulation TEXT,
  i_color TEXT,
  i_units TEXT,
  i_container TEXT,
  i_manager_id BIGINT,
  i_product_name TEXT,
  PRIMARY KEY (i_item_sk)
);

CREATE TABLE store_sales (
  ss_sold_date_sk BIGINT,
  ss_sold_time_sk BIGINT,
  ss_item_sk BIGINT,
  ss_customer_sk BIGINT,
  ss_cdemo_sk BIGINT,
  ss_hdemo_sk BIGINT,
  ss_addr_sk BIGINT,
  ss_store_sk BIGINT,
  ss_promo_sk BIGINT,
  ss_ticket_number BIGINT,
  ss_quantity BIGINT,
  ss_wholesale_cost DOUBLE PRECISION,
  ss_list_price DOUBLE PRECISION,
  ss_sales_price DOUBLE PRECISION,
  ss_ext_discount_amt DOUBLE PRECISION,
  ss_ext_sales_price DOUBLE PRECISION,
  ss_ext_wholesale_cost DOUBLE PRECISION,
  ss_ext_list_price DOUBLE PRECISION,
  ss_ext_tax DOUBLE PRECISION,
  ss_coupon_amt DOUBLE PRECISION,
  ss_net_paid DOUBLE PRECISION,
  ss_net_paid_inc_tax DOUBLE PRECISION,
  ss_net_profit DOUBLE PRECISION,
  PRIMARY KEY (ss_item_sk, ss_ticket_number)
);

CREATE TABLE catalog_page (
  cp_catalog_page_sk BIGINT,
  cp_catalog_page_id TEXT,
  cp_start_date_sk BIGINT,
  cp_end_date_sk BIGINT,
  cp_department TEXT,
  cp_catalog_number BIGINT,
  cp_catalog_page_number BIGINT,
  cp_description TEXT,
  cp_type TEXT,
  PRIMARY KEY (cp_catalog_page_sk)
);

CREATE TABLE catalog_sales (
  cs_sold_date_sk BIGINT,
  cs_sold_time_sk BIGINT,
  cs_ship_date_sk BIGINT,
  cs_bill_customer_sk BIGINT,
  cs_bill_cdemo_sk BIGINT,
  cs_bill_hdemo_sk BIGINT,
  cs_bill_addr_sk BIGINT,
  cs_ship_customer_sk BIGINT,
  cs_ship_cdemo_sk BIGINT,
  cs_ship_hdemo_sk BIGINT,
  cs_ship_addr_sk BIGINT,
  cs_call_center_sk BIGINT,
  cs_catalog_page_sk BIGINT,
  cs_ship_mode_sk BIGINT,
  cs_warehouse_sk BIGINT,
  cs_item_sk BIGINT,
  cs_promo_sk BIGINT,
  cs_order_number BIGINT,
  cs_quantity BIGINT,
  cs_wholesale_cost DOUBLE PRECISION,
  cs_list_price DOUBLE PRECISION,
  cs_sales_price DOUBLE PRECISION,
  cs_ext_discount_amt DOUBLE PRECISION,
  cs_ext_sales_price DOUBLE PRECISION,
  cs_ext_wholesale_cost DOUBLE PRECISION,
  cs_ext_list_price DOUBLE PRECISION,
  cs_ext_tax DOUBLE PRECISION,
  cs_coupon_amt DOUBLE PRECISION,
  cs_ext_ship_cost DOUBLE PRECISION,
  cs_net_paid DOUBLE PRECISION,
  cs_net_paid_inc_tax DOUBLE PRECISION,
  cs_net_paid_inc_ship DOUBLE PRECISION,
  cs_net_paid_inc_ship_tax DOUBLE PRECISION,
  cs_net_profit DOUBLE PRECISION,
  PRIMARY KEY (cs_item_sk, cs_order_number)
);

CREATE TABLE catalog_returns (
  cr_returned_date_sk BIGINT,
  cr_returned_time_sk BIGINT,
  cr_item_sk BIGINT,
  cr_refunded_customer_sk BIGINT,
  cr_refunded_cdemo_sk BIGINT,
  cr_refunded_hdemo_sk BIGINT,
  cr_refunded_addr_sk BIGINT,
  cr_returning_customer_sk BIGINT,
  cr_returning_cdemo_sk BIGINT,
  cr_returning_hdemo_sk BIGINT,
  cr_returning_addr_sk BIGINT,
  cr_call_center_sk BIGINT,
  cr_catalog_page_sk BIGINT,
  cr_ship_mode_sk BIGINT,
  cr_warehouse_sk BIGINT,
  cr_reason_sk BIGINT,
  cr_order_number BIGINT,
  cr_return_quantity BIGINT,
  cr_return_amount DOUBLE PRECISION,
  cr_return_tax DOUBLE PRECISION,
  cr_return_amt_inc_tax DOUBLE PRECISION,
  cr_fee DOUBLE PRECISION,
  cr_return_ship_cost DOUBLE PRECISION,
  cr_refunded_cash DOUBLE PRECISION,
  cr_reversed_charge DOUBLE PRECISION,
  cr_store_credit DOUBLE PRECISION,
  cr_net_loss DOUBLE PRECISION,
  PRIMARY KEY (cr_item_sk, cr_order_number)
);

CREATE TABLE web_site (
  web_site_sk BIGINT,
  web_site_id TEXT,
  web_rec_start_date TEXT,
  web_rec_end_date TEXT,
  web_name TEXT,
  web_open_date_sk BIGINT,
  web_close_date_sk BIGINT,
  web_class TEXT,
  web_manager TEXT,
  web_mkt_id BIGINT,
  web_mkt_class TEXT,
  web_mkt_desc TEXT,
  web_market_manager TEXT,
  web_company_id BIGINT,
  web_company_name TEXT,
  web_street_number TEXT,
  web_street_name TEXT,
  web_street_type TEXT,
  web_suite_number TEXT,
  web_city TEXT,
  web_county TEXT,
  web_state TEXT,
  web_zip TEXT,
  web_country TEXT,
  web_gmt_offset DOUBLE PRECISION,
  web_tax_percentage DOUBLE PRECISION,
  PRIMARY KEY (web_site_sk)
);

CREATE TABLE web_sales (
  ws_sold_date_sk BIGINT,
  ws_sold_time_sk BIGINT,
  ws_ship_date_sk BIGINT,
  ws_item_sk BIGINT,
  ws_bill_customer_sk BIGINT,
  ws_bill_cdemo_sk BIGINT,
  ws_bill_hdemo_sk BIGINT,
  ws_bill_addr_sk BIGINT,
  ws_ship_customer_sk BIGINT,
  ws_ship_cdemo_sk BIGINT,
  ws_ship_hdemo_sk BIGINT,
  ws_ship_addr_sk BIGINT,
  ws_web_page_sk BIGINT,
  ws_web_site_sk BIGINT,
  ws_ship_mode_sk BIGINT,
  ws_warehouse_sk BIGINT,
  ws_promo_sk BIGINT,
  ws_order_number BIGINT,
  ws_quantity BIGINT,
  ws_wholesale_cost DOUBLE PRECISION,
  ws_list_price DOUBLE PRECISION,
  ws_sales_price DOUBLE PRECISION,
  ws_ext_discount_amt DOUBLE PRECISION,
  ws_ext_sales_price DOUBLE PRECISION,
  ws_ext_wholesale_cost DOUBLE PRECISION,
  ws_ext_list_price DOUBLE PRECISION,
  ws_ext_tax DOUBLE PRECISION,
  ws_coupon_amt DOUBLE PRECISION,
  ws_ext_ship_cost DOUBLE PRECISION,
  ws_net_paid DOUBLE PRECISION,
  ws_net_paid_inc_tax DOUBLE PRECISION,
  ws_net_paid_inc_ship DOUBLE PRECISION,
  ws_net_paid_inc_ship_tax DOUBLE PRECISION,
  ws_net_profit DOUBLE PRECISION,
  PRIMARY KEY (ws_item_sk, ws_order_number)
);

CREATE TABLE web_returns (
  wr_returned_date_sk BIGINT,
  wr_returned_time_sk BIGINT,
  wr_item_sk BIGINT,
  wr_refunded_customer_sk BIGINT,
  wr_refunded_cdemo_sk BIGINT,
  wr_refunded_hdemo_sk BIGINT,
  wr_refunded_addr_sk BIGINT,
  wr_returning_customer_sk BIGINT,
  wr_returning_cdemo_sk BIGINT,
  wr_returning_hdemo_sk BIGINT,
  wr_returning_addr_sk BIGINT,
  wr_web_page_sk BIGINT,
  wr_reason_sk BIGINT,
  wr_order_number BIGINT,
  wr_return_quantity BIGINT,
  wr_return_amt DOUBLE PRECISION,
  wr_return_tax DOUBLE PRECISION,
  wr_return_amt_inc_tax DOUBLE PRECISION,
  wr_fee DOUBLE PRECISION,
  wr_return_ship_cost DOUBLE PRECISION,
  wr_refunded_cash DOUBLE PRECISION,
  wr_reversed_charge DOUBLE PRECISION,
  wr_account_credit DOUBLE PRECISION,
  wr_net_loss DOUBLE PRECISION,
  PRIMARY KEY (wr_item_sk, wr_order_number)
);

CREATE TABLE customer_demographics (
  cd_demo_sk BIGINT,
  cd_gender TEXT,
  cd_marital_status TEXT,
  cd_education_status TEXT,
  cd_purchase_estimate BIGINT,
  cd_credit_rating TEXT,
  cd_dep_count BIGINT,
  cd_dep_employed_count BIGINT,
  cd_dep_college_count BIGINT,
  PRIMARY KEY (cd_demo_sk)
);

CREATE TABLE promotion (
  p_promo_sk BIGINT,
  p_promo_id TEXT,
  p_start_date_sk BIGINT,
  p_end_date_sk BIGINT,
  p_item_sk BIGINT,
  p_cost DOUBLE PRECISION,
  p_response_target BIGINT,
  p_promo_name TEXT,
  p_channel_dmail TEXT,
  p_channel_email TEXT,
  p_channel_catalog TEXT,
  p_channel_tv TEXT,
  p_channel_radio TEXT,
  p_channel_press TEXT,
  p_channel_event TEXT,
  p_channel_demo TEXT,
  p_channel_details TEXT,
  p_purpose TEXT,
  p_discount_active TEXT,
  PRIMARY KEY (p_promo_sk)
);

CREATE TABLE reason (
  r_reason_sk BIGINT,
  r_reason_id TEXT,
  r_reason_desc TEXT,
  PRIMARY KEY (r_reason_sk)
);

CREATE TABLE customer_address (
  ca_address_sk BIGINT,
  ca_address_id TEXT,
  ca_street_number TEXT,
  ca_street_name TEXT,
  ca_street_type TEXT,
  ca_suite_number TEXT,
  ca_city TEXT,
  ca_county TEXT,
  ca_state TEXT,
  ca_zip TEXT,
  ca_country TEXT,
  ca_gmt_offset DOUBLE PRECISION,
  ca_location_type TEXT,
  PRIMARY KEY (ca_address_sk)
);

CREATE TABLE call_center (
  cc_call_center_sk BIGINT,
  cc_call_center_id TEXT,
  cc_rec_start_date TEXT,
  cc_rec_end_date TEXT,
  cc__date_sk BIGINT,
  cc_open_date_sk BIGINT,
  cc_name TEXT,
  cc_class TEXT,
  cc_employees BIGINT,
  cc_sq_ft BIGINT,
  cc_hours TEXT,
  cc_manager TEXT,
  cc_mkt_id BIGINT,
  cc_mkt_class TEXT,
  cc_mkt_desc TEXT,
  cc_market_manager TEXT,
  cc_division BIGINT,
  cc_division_name TEXT,
  cc_company BIGINT,
  cc_company_name TEXT,
  cc_street_number BIGINT,
  cc_street_name TEXT,
  cc_street_type TEXT,
  cc_suite_number TEXT,
  cc_city TEXT,
  cc_county TEXT,
  cc_state TEXT,
  cc_zip TEXT,
  cc_country TEXT,
  cc_gmt_offset DOUBLE PRECISION,
  cc_tax_percentage DOUBLE PRECISION,
  PRIMARY KEY (cc_call_center_sk)
);

CREATE TABLE household_demographics (
  hd_demo_sk BIGINT,
  hd_income_band_sk BIGINT,
  hd_buy_potential TEXT,
  hd_dep_count BIGINT,
  hd_vehicle_count BIGINT,
  PRIMARY KEY (hd_demo_sk)
);

CREATE TABLE inventory (
  inv_date_sk BIGINT,
  inv_item_sk BIGINT,
  inv_warehouse_sk BIGINT,
  inv_quantity_on_hand BIGINT,
  PRIMARY KEY (inv_date_sk, inv_item_sk, inv_warehouse_sk)
);

CREATE TABLE ship_mode (
  sm_ship_mode_sk BIGINT,
  sm_ship_mode_id TEXT,
  sm_type TEXT,
  sm_code TEXT,
  sm_carrier TEXT,
  sm_contract TEXT,
  PRIMARY KEY (sm_ship_mode_sk)
);

CREATE TABLE time_dim (
  t_time_sk BIGINT,
  t_time_id TEXT,
  t_time BIGINT,
  t_hour BIGINT,
  t_minute BIGINT,
  t_second BIGINT,
  t_am_pm TEXT,
  t_shift TEXT,
  t_sub_shift TEXT,
  t_meal_time TEXT,
  PRIMARY KEY (t_time_sk)
);

CREATE TABLE warehouse (
  w_warehouse_sk BIGINT,
  w_warehouse_id TEXT,
  w_warehouse_name TEXT,
  w_warehouse_sq_ft BIGINT,
  w_street_number TEXT,
  w_street_name TEXT,
  w_street_type TEXT,
  w_suite_number TEXT,
  w_city TEXT,
  w_county TEXT,
  w_state TEXT,
  w_zip TEXT,
  w_country TEXT,
  w_gmt_offset DOUBLE PRECISION,
  PRIMARY KEY (w_warehouse_sk)
);

CREATE TABLE web_page (
  wp_web_page_sk BIGINT,
  wp_web_page_id TEXT,
  wp_rec_start_date TEXT,
  wp_rec_end_date TEXT,
  wp_creation_date_sk BIGINT,
  wp_access_date_sk BIGINT,
  wp_autogen_flag TEXT,
  wp_customer_sk BIGINT,
  wp_url TEXT,
  wp_type TEXT,
  wp_char_count BIGINT,
  wp_link_count BIGINT,
  wp_image_count BIGINT,
  wp_max_ad_count BIGINT,
  PRIMARY KEY (wp_web_page_sk)
);

CREATE TABLE income_band (
  ib_income_band_sk BIGINT,
  ib_lower_bound BIGINT,
  ib_upper_bound BIGINT,
  PRIMARY KEY (ib_income_band_sk)
);

\COPY store_returns FROM '$DATA_DIR/store_returns.dat' DELIMITER '|' CSV;
\COPY date_dim FROM '$DATA_DIR/date_dim.dat' DELIMITER '|' CSV;
\COPY store FROM '$DATA_DIR/store.dat' DELIMITER '|' CSV;
\COPY customer FROM '$DATA_DIR/customer.dat' DELIMITER '|' CSV;
\COPY call_center FROM '$DATA_DIR/call_center.dat' DELIMITER '|' CSV;
\COPY catalog_page FROM '$DATA_DIR/catalog_page.dat' DELIMITER '|' CSV;
\COPY catalog_returns FROM '$DATA_DIR/catalog_returns.dat' DELIMITER '|' CSV;
\COPY catalog_sales FROM '$DATA_DIR/catalog_sales.dat' DELIMITER '|' CSV;
\COPY customer_address FROM '$DATA_DIR/customer_address.dat' DELIMITER '|' CSV;
\COPY customer_demographics FROM '$DATA_DIR/customer_demographics.dat' DELIMITER '|' CSV;
\COPY household_demographics FROM '$DATA_DIR/household_demographics.dat' DELIMITER '|' CSV;
\COPY income_band FROM '$DATA_DIR/income_band.dat' DELIMITER '|' CSV;
\COPY inventory FROM '$DATA_DIR/inventory.dat' DELIMITER '|' CSV;
\COPY item FROM '$DATA_DIR/item.dat' DELIMITER '|' CSV;
\COPY promotion FROM '$DATA_DIR/promotion.dat' DELIMITER '|' CSV;
\COPY reason FROM '$DATA_DIR/reason.dat' DELIMITER '|' CSV;
\COPY ship_mode FROM '$DATA_DIR/ship_mode.dat' DELIMITER '|' CSV;
\COPY store_sales FROM '$DATA_DIR/store_sales.dat' DELIMITER '|' CSV;
\COPY time_dim FROM '$DATA_DIR/time_dim.dat' DELIMITER '|' CSV;
\COPY warehouse FROM '$DATA_DIR/warehouse.dat' DELIMITER '|' CSV;
\COPY web_page FROM '$DATA_DIR/web_page.dat' DELIMITER '|' CSV;
\COPY web_returns FROM '$DATA_DIR/web_returns.dat' DELIMITER '|' CSV;
\COPY web_sales FROM '$DATA_DIR/web_sales.dat' DELIMITER '|' CSV;
\COPY web_site FROM '$DATA_DIR/web_site.dat' DELIMITER '|' CSV;
EOF

# echo "📊 Running ANALYZE..."
# sudo -u "$DB_USER" psql -d "$DB_NAME" -c "ANALYZE;"

# echo "✅ TPC-DS data load complete (subset: store_sales, customer, item, date_dim, store)"
