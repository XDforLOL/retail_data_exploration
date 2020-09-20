from product_generator import *
import psycopg2
import os

conn = psycopg2.connect(dbname="postgres",
                        user="postgres",
                        password=os.environ.get('psql_pass'),
                        host=os.environ.get('psql_ip'))
cursor = conn.cursor()


def test_get_valid_product_id():
    result = get_valid_product_id()
    cursor.execute('select MAX(product_id) from ksp.products')
    highest_id = cursor.fetchall()
    assert result - 1 == highest_id[0][0]
    assert type(result) == int


def test_get_valid_product():
    # TODO find missing tests todo
    result = get_valid_product()
    assert type(result) == dict
    assert list(result.keys()) == ['product_id', 'product_name', 'model', 'maker', 'stock', 'price']
    assert [int, str, str, str, int, float] == [type(value) for key, value in result.items()]