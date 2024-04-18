def print_films_info(films):
    if len(films) > 0:
        for film in films:
            print("_" * 50)
            print(f"{'Name:':>19} {film[0]}")
            print(f"{'Year of production:':>19} {film[1]}")
            print(f"{'Description:':>19} {film[2]}")
    else:
        print('No films for the selected search options')


def print_table_description(description):
    print("Schema:")
    print(tuple(['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']))
    print("-" * 100)
    for row in description:
        print(row)


def print_categories(categories):
    for category in categories:
        print(f"{category[0]:>4} - {category[1]:^15}")


def print_tables(tables):
    print("Tables:", tables)
