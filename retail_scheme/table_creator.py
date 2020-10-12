from db_connector import execute_query
from os import listdir
from os.path import isfile, join

mypath = r'./SQL'
sql_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

if __name__ == '__main__':
    execute_query("CREATE SCHEMA retail")
    for f in sql_files:
        with open(f'SQL/{f}', 'r') as sql_queries:
            execute_query(sql_queries.read())




