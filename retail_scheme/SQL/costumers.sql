CREATE TABLE retail.costumers (
	costumer_id int4 NOT NULL,
	first_name varchar(50) NULL,
	last_name varchar(50) NULL,
	phone_number varchar(255) NULL,
	created_on timestamp NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT costumers_pkey PRIMARY KEY (costumer_id)
);