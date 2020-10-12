CREATE TABLE retail.products (
	product_id int4 NOT NULL,
	product_name varchar(50) NULL,
	model varchar(50) NULL,
	maker varchar(255) NULL,
	stock int4 NULL,
	price float8 NULL,
	created_on timestamp NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT products_pkey PRIMARY KEY (product_id)
);