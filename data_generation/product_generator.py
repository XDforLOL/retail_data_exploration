from typing import NoReturn
import os
import random
import psycopg2
import string


conn = psycopg2.connect(dbname="postgres",
                        user="postgres",
                        password=os.environ.get('psql_pass'),
                        host=os.environ.get('psql_ip'))
cursor = conn.cursor()


def insert_product(product_id, product_name, model, maker, stock, price) -> NoReturn:
    cursor.execute(f"INSERT INTO ksp.products VALUES ({product_id},"
                   f"'{product_name}','{model}','{maker}' ,'{stock}', '{price}')")
    conn.commit()


def get_model() -> str:
    sample_str = ''.join((random.choice(string.ascii_letters) for i in range(6)))
    sample_str += ''.join((random.choice(string.digits) for i in range(3)))
    model_list = list(sample_str)
    random.shuffle(model_list)
    model = ''.join(model_list)
    return model


def get_valid_product_id() -> int:
    cursor.execute('select MAX(product_id) from ksp.products')
    highest_id = cursor.fetchall()
    return highest_id[0][0] + 1


def get_valid_product() -> dict:
    makers = ['Asus', 'HTC', 'Huawei', 'LG Electronics', 'Meizu', 'Motorola Mobility', 'Xiaomi', 'OnePlus']
    model = get_model()
    maker = random.choice(makers)
    product_name = f"{maker} {model}"
    price = round(random.uniform(300, 3500), 1)
    return {
        'product_id': get_valid_product_id(),
        'product_name': product_name,
        'model': model,
        'maker': maker,
        'stock': random.randint(0, 99),
        'price': price,
    }


if __name__ == '__main__':
    for i in range(1):
        product = get_valid_product()
        insert_product(**product)
        print(f'Product ID: #{product["product_id"]} Name:'
              f'{product["product_name"]} {product["model"]} {product["maker"]} Inserted')
