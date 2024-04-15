# В базе данных ich_edit три таблицы. Users с полями (id, name, age), Products с полями (pid, prod, quantity) и Sales с
# полями (sid, id, pid). Программа должна вывести все имена из таблицы users, дать пользователю выбрать одно из них и
# вывести все покупки этого пользователя.

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

    connection = create_connection(**dbconfig)
    if connection is not None:
        users = execute_read_query(connection, queries.get_all_users_names)
        print("List of users:")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}")

        user_id = input("Select one name and enter ID of this user: ")
        orders = execute_read_query(connection, queries.get_sales_by_user_id.format(id=user_id))

        if len(orders) == 0:
            print("No orders for user with ID {}".format(user_id))
        else:
            print("Orders list:")
            for order in orders:
                print(f"order_id: {order[0]}, product: {order[1]}, quantity: {order[2]}")
