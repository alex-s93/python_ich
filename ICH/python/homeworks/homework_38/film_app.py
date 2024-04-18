# Доработать мини-интерфейс к базе данных, который был сделан на занятии. Новые возможности интерфейса:
# - Ввести список полей выбранной таблицы.
# - При вводе искомого значения добавить возможность выбора знака - найти записи, в которых выбранное поле больше,
# меньше или равно введенному значению.

from os import getenv
from sys import exit
from dotenv import load_dotenv

from ICH.python.homeworks.homework_38 import output_helper
from db_methods import create_connection
import input_helper
import service_methods
import constants


def main():
    load_dotenv()
    db_config = {'host': getenv('db_host'),
                 'user': getenv('db_user'),
                 'password': getenv('db_password'),
                 'database': 'sakila'}

    connection = create_connection(**db_config)
    if connection is None:
        print(constants.DB_CONNECTION_ERROR_MSG)
        exit()

    while True:
        try:
            user_request = input_helper.get_user_choice()
        except ValueError as err:
            print(err)
            continue

        if user_request == constants.SEARCH_FILMS:
            while True:
                try:
                    search_criteria = input_helper.get_search_criteria_from_user()
                except ValueError as err:
                    print(err)
                    continue

                if search_criteria == constants.CATEGORY:
                    categories = service_methods.get_categories(connection)

                    output_helper.print_categories(categories)

                    service_methods.search_by_category(connection, categories)

                if search_criteria == constants.PRODUCTION_YEAR:
                    service_methods.search_by_year(connection)

                print()
                print(constants.CURRENT_LEVEL_MSG.format(constants.SEARCH_FILMS))
                if input(constants.RETURN_MSG).lower() in ('y', 'yes'):
                    break

        if user_request == constants.TABLE_DESCRIPTION:
            tables = service_methods.get_tables(connection)

            output_helper.print_tables(tables)

            service_methods.select_and_show_table_description(connection, tables)

        print()
        print(constants.CURRENT_LEVEL_MSG.format('main'))
        if input(constants.QUIT_MSG).lower() in ('y', 'yes'):
            connection.close()
            break


main()
