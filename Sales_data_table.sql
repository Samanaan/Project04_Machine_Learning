-- Create a new table
CREATE TABLE sales_data (
  	product_id VARCHAR(20) NOT NULL,
  	product_category_name VARCHAR,
	month_year DATE,
  	qty_sold INT,
  	total_price FLOAT,
	freight_price FLOAT,
	unit_price FLOAT,
	product_rating FLOAT,
	no_customers INT,
	month INT,
	year INT,
	seasonality FLOAT,
	volume INT,
	comp1_price FLOAT,
	comp1_prod_rating FLOAT,
	comp1_freight_price FLOAT,
	comp2_price FLOAT,
	comp2_prod_rating FLOAT,
	comp2_freight_price FLOAT,
	comp3_price FLOAT,
	comp3_prod_rating FLOAT,
	comp3_freight_price FLOAT,
	lag_price FLOAT
);

-- Query all fields from the table
SELECT *
FROM sale_data;

