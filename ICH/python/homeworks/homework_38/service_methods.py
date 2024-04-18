from db_methods import execute_read_query
import input_helper
import output_helper
import queries
import constants


def get_categories(connection):
    return execute_read_query(connection, queries.categories_query)


def get_tables(connection):
    return [t[0] for t in execute_read_query(connection, queries.tables_query)]


def select_and_show_table_description(connection, tables):
    while True:
        try:
            selected_table = input_helper.get_table_name_from_user(tables)
        except ValueError as err:
            print(err)
            continue

        description = execute_read_query(connection,
                                         queries.table_description_query.format(table=selected_table))
        output_helper.print_table_description(description)

        print()
        if input(constants.RETURN_MSG).lower() in ('y', 'yes'):
            break


def search_by_category(connection, categories):
    while True:
        try:
            category = input_helper.get_category_from_user(categories)
            film_amount = input_helper.get_amount_of_films_from_user()
        except ValueError as err:
            print(err)
            continue

        films = execute_read_query(connection,
                                   queries.film_by_category_query.format(id=category, amount=film_amount))
        output_helper.print_films_info(films)

        print()
        if input(constants.RETURN_MSG).lower() in ('y', 'yes'):
            break


def search_by_year(connection):
    while True:
        try:
            year = input_helper.get_production_year_from_user()
            operator = input_helper.get_search_operator_from_user()
            film_amount = input_helper.get_amount_of_films_from_user()
        except ValueError as err:
            print(err)
            continue

        films = execute_read_query(connection,
                                   queries.film_by_year_query.format(year=year, amount=film_amount, operator=operator))

        output_helper.print_films_info(films)

        print()
        if input(constants.RETURN_MSG).lower() in ('y', 'yes'):
            break
