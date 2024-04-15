# В базе данных ich_edit три таблицы. Users с полями (id, name, age), Products с полями (pid, prod, quantity) и Sales с
# полями (sid, id, pid). Программа должна запросить у пользователя название таблицы и вывести все ее строки или
# сообщение, что такой таблицы нет.

from dotenv import load_dotenv
from os import getenv
import queries
from db_methods import create_connection, execute_read_query

if __name__ == "__main__":
    load_dotenv()
    dbconfig = {'host': getenv('db_host'),
                'user': getenv('db_user'),
                'password': getenv('db_password'),
                'database': 'ich_edit'}

    table_name = input("Enter a table name you want to fetch: ")

    connection = create_connection(**dbconfig)
    if connection is not None:
        result = execute_read_query(connection, queries.select_all_from_table.format(table=table_name))

        if result is not None:
            for row in result:
                print(row)
        else:
            tables = execute_read_query(connection, queries.show_tables)
            print("The list of existing tables:")
            for table in tables:
                print("-", table[0])

        connection.close()
