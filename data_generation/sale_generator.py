from typing import NoReturn
import datetime
import random
import psycopg2
import os
import logging
import pandas.io.sql as sqlio
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO,format='%(levelname)s:%(name)s:%(funcName)s:%(message)s')

conn = psycopg2.connect(dbname="postgres",
                        user="postgres",
                        password=os.environ.get('psql_pass'),
                        host=os.environ.get('psql_ip'))
cursor = conn.cursor()


def get_valid_sale_id() -> str:
    cursor.execute('select MAX(sale_id) from ksp.sales')
    highest_id = cursor.fetchall()
    logger.debug(f'Highest id found was{highest_id} adding one to it')
    return highest_id[0][0] + 1


def get_random_costumer_id() -> str:
    dat = sqlio.read_sql_query('select costumer_id from ksp.costumers', conn)
    random_existing_costumer = random.choice(list(dat['costumer_id']))
    logger.debug(f'Random costumer from selected list{random_existing_costumer}')
    return random_existing_costumer


def get_valid_sale_details(product_amount):
    output = []
    for i in range(product_amount):
        data_products = sqlio.read_sql_query('select product_id from ksp.products', conn)
        output.append((random.choice(list(data_products['product_id'])), random.randint(1, 10)))
    valid_sale = {
        'sale_id': get_valid_sale_id(),
        'costumer_id': get_random_costumer_id(),
        'time': datetime.datetime.utcfromtimestamp(get_timestamp_for_last_30D()),
        'sale_details': output
    }
    logger.debug(f"costumer {valid_sale['costumer_id']} bought these items{output} at {valid_sale['time']}")
    return valid_sale


def get_timestamp_for_last_30D():
    current_time = datetime.datetime.now().timestamp()
    seconds_in_month = 2_591_999
    return random.randint(int(current_time - seconds_in_month), int(current_time))


def insert_sale(sale) -> NoReturn:
    time = sale['time']
    list_of_items = []
    cursor.execute(f"INSERT INTO ksp.sales VALUES ({sale['sale_id']}, {sale['costumer_id']}, '{time}')")
    logger.info(f"sale_ID {sale['sale_id']} was inserted into table ksp.sales")
    for product_id, quantity in sale['sale_details']:
        cursor.execute(f"INSERT INTO ksp.sale_details VALUES ({sale['sale_id']}, {product_id}, {quantity})")
        list_of_items.append(product_id)

    logger.info(f"sale_ID {sale['sale_id']} these items were inserted into ksp.sale_details {list_of_items} were inserted")
    conn.commit()


if __name__ == '__main__':
    for i in range(100):
        insert_sale(get_valid_sale_details(random.randint(1, 10)))
