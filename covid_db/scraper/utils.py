import json

from datetime import datetime
from psycopg2 import connect, sql

def format_date(date: str) -> str:
    """
    Converts date string i.e. "6 August 2020" to date string in ISO format i.e. "2020-08-06".
    """
    return datetime.strptime(date, "%d %B %Y").date().isoformat()

def save(data: dict) -> None:
    """
    Save data into postgreSQL database.
    """

    # Add details of postgresql database
    conn = connect(
        dbname = '',
        user = '',
        host = '',
        password = '',
        port = '')
    cursor = conn.cursor()

    TABLENAME = 'public.dashboard_record'
    sql_query = f"INSERT INTO {TABLENAME} VALUES (\'{data['date']}\', {data['num_imported']}, {data['num_dormitories']}, {data['num_community']});"
    print(sql_query)
    sql_object = sql.SQL(sql_query)
    try:
        cursor.execute(sql_object)
        conn.commit()
        print('save() ended')
    except Exception as err:
        print ("save() ERROR:", err)
    finally:
        cursor.close()
        conn.close()
