# При запуске программы выводится список категорий (номер и название категории)
# Пользователь может ввести номер категории
# Программа выводит все фильмы в данной категории, но не более 10 фильмов. О фильме выводится следующая информация:
# название, год выпуска, описание. Опционально - список актеров.

from dotenv import load_dotenv
from os import getenv
from db_methods import create_connection, execute_read_query
import queries

load_dotenv()
db_config = {'host': getenv('db_host'),
             'user': getenv('db_user'),
             'password': getenv('db_password'),
             'database': 'sakila'}


def get_valid_category_from_user(categories):
    usr_input = input("Enter Id of category: ")
    if int(usr_input) not in [category_id for category_id, _ in categories]:
        raise ValueError("Invalid category Id. Try again")

    return int(usr_input)


def get_amount_of_films_from_user():
    usr_input = input("Enter amount of films you wanna get: ")
    if not usr_input.isdigit():
        raise ValueError("You entered an invalid value. Try again")

    return int(usr_input)


def print_film_info(film):
    print("_" * 50)
    print(f"{'Name:':>19} {film[0]}")
    print(f"{'Year of production:':>19} {film[1]}")
    print(f"{'Description:':>19} {film[2]}")


def main():
    connection = create_connection(**db_config)
    categories = execute_read_query(connection, queries.categories_query)
    for category in categories:
        print(f"{category[0]:>4} - {category[1]:^15}")

    while True:
        try:
            category = get_valid_category_from_user(categories)
            film_amount = get_amount_of_films_from_user()
        except ValueError as err:
            print(err)
            continue

        films = execute_read_query(connection, queries.film_by_category_query.format(id=category, amount=film_amount))
        for film in films:
            print_film_info(film)

        print()
        if input('Doy you wanna quit? (y/n): ').lower() in ('y', 'yes'):
            break


main()
