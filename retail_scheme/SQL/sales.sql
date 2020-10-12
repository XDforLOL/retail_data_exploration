CREATE TABLE retail.sales (
	sale_id int4 NOT NULL,
	costumer_id int4 NULL references retail.costumers(costumer_id),
	"time" timestamp NULL,
	created_on timestamp NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT sales_pkey PRIMARY KEY (sale_id)
);