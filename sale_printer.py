import argparse
import pandas.io.sql as sqlio
import psycopg2
import os

conn = psycopg2.connect(dbname="postgres",
                        user="postgres",
                        password=os.environ.get('psql_pass'),
                        host=os.environ.get('psql_ip'))
cursor = conn.cursor()

parser = argparse.ArgumentParser(description='Receipt')
parser.add_argument('-sid', '--saleid', help='Receipt of selected sale ID', default=None)
args = parser.parse_args()

def get_receipt(id):
    df = sqlio.read_sql_query(f"SELECT * FROM ksp.sales WHERE sale_id = {id}", conn)
    return df


def get_costumer(costumer_id):
    df = sqlio.read_sql_query(f"SELECT * FROM ksp.costumers WHERE costumer_id = {int(costumer_id)}", conn)
    costumer_details = {'first_name': df['first_name'][0],
                        'last_name': df['last_name'][0]}
    # print(costumer_details)
    return costumer_details


def print_sale_details(id):
    sale_details_df = sqlio.read_sql_query(f"SELECT * FROM ksp.sale_details WHERE sale_id ={id}", conn)
    total_sale_price = 0
    for index, row in sale_details_df.iterrows():
        product_id = row['product_id']
        product_quantity = row['quantity']
        product_detail_df = sqlio.read_sql_query(
            f"SELECT product_name, price FROM ksp.products WHERE product_id = {product_id}", conn)
        product_name = product_detail_df['product_name'][0]
        product_price = product_detail_df['price'][0]
        total_per_quantity = product_quantity * product_price
        total_sale_price += total_per_quantity
        if product_quantity == 1:
            print(
                f"Product name: {product_name}\n\tQuantity: {product_quantity}\t\t\tUnit price {product_price:.2f}₪")
        else:
            print(f"Product name: {product_name}\n\tQuantity: {product_quantity}\t\t\tUnit price"
                  f" {product_price:.2f}₪\tTotal {total_per_quantity:.2f}₪")
    print('---------------------------------------------------------------------------------------')
    print(f"Total Price:\t\t\t\t\t\t{total_sale_price}")


def print_receipt(df):
    costumer_dict = get_costumer(df['costumer_id'])
    full_name = f"{costumer_dict['first_name']} {costumer_dict['last_name']}"
    print(f"Sale number: {df['sale_id'][0]}\t\t\t\t\t Costumer name: {full_name}")
    print('---------------------------------------------------------------------------------------')



if __name__ == '__main__':
    print_receipt(get_receipt(args.saleid))
    print_sale_details(args.saleid)
