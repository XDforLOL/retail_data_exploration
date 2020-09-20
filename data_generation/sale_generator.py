from typing import NoReturn
import datetime
import random
import psycopg2
import os
import pandas as pd
import pandas.io.sql as sqlio

conn = psycopg2.connect(dbname="postgres",
                        user="postgres",
                        password=os.environ.get('psql_pass'),
                        host=os.environ.get('psql_ip'))
cursor = conn.cursor()


def get_valid_sale_id() -> str:
    cursor.execute('select MAX(sale_id) from ksp.sales')
    highest_id = cursor.fetchall()
    return highest_id[0][0] + 1


def get_random_costumer_id() -> str:
    dat = sqlio.read_sql_query('select costumer_id from ksp.costumers', conn)
    return random.choice(list(dat['costumer_id']))


def get_valid_sale_details(product_amount):
    output = []
    for i in range(product_amount):
        data_products = sqlio.read_sql_query('select product_id from ksp.products', conn)
        output.append((random.choice(list(data_products['product_id'])), random.randint(1, 10)))
    # print(f"costumer {random.choice(list(data_costumers['costumer_id']))} has bought these items{output}")
    return {
        'sale_id': get_valid_sale_id(),
        'costumer_id': get_random_costumer_id(),
        'time': datetime.datetime.now(),
        'sale_details': output
    }


def insert_sale(sale) -> NoReturn:
    time = sale['time']
    cursor.execute(f"INSERT INTO ksp.sales VALUES ({sale['sale_id']}, {sale['costumer_id']}, '{time}')")
    for product_id, quantity in sale['sale_details']:
        cursor.execute(f"INSERT INTO ksp.sale_details VALUES ({sale['sale_id']}, {product_id}, {quantity})")
    conn.commit()


if __name__ == '__main__':
    insert_sale(get_valid_sale_details(4))
