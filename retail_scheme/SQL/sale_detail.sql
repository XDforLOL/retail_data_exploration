CREATE TABLE retail.sale_details (
	sale_id int4 NOT NULL references retail.sales(sale_id),
	product_id int4 NOT NULL references retail.products(product_id),
	quantity int4 NULL,
	created_on timestamp NULL DEFAULT CURRENT_TIMESTAMP
);