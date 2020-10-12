import psycopg2
import os
import logging

logger = logging.getLogger(__name__)


def execute_query(query:str) -> bool:
    conn = psycopg2.connect(dbname="postgres",
                            user="postgres",
                            password=os.environ.get('psql_pass'),
                            host=os.environ.get('psql_ip'))
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
    except Exception as e:
        logger.error(query)
        raise e


