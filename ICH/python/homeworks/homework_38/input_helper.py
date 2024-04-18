def get_category_from_user(categories):
    usr_input = input("Enter Id of category: ")
    if int(usr_input) not in [category_id for category_id, _ in categories]:
        raise ValueError(f"Invalid category Id '{usr_input}'. Try again")

    return int(usr_input)


def get_production_year_from_user():
    usr_input = input("Enter production year: ")
    if len(usr_input) != 4:
        raise ValueError(f"Invalid year '{usr_input}'. Try again")

    return int(usr_input)


def get_amount_of_films_from_user():
    usr_input = input("Enter amount of films you wanna get: ")
    if not usr_input.isdigit():
        raise ValueError(f"Invalid value '{usr_input}'. Try again")

    return int(usr_input)


def get_search_operator_from_user():
    options = ['<', ">", '<=', '>=', '=', '!=']
    usr_input = input(f"Enter an operator for search. Options {options}: ")
    if usr_input not in options:
        raise ValueError(f"Invalid operator '{usr_input}'. Try again")

    return usr_input


def get_table_name_from_user(tables):
    selected_table = input("Which table description do you wanna see? ")
    if selected_table not in tables:
        raise ValueError(f"Invalid table name '{selected_table}'. Try again")

    return selected_table


def get_search_criteria_from_user():
    options = ['category', 'production year']
    search_criteria = input(f"You can search by: {options}. What do you prefer? ").lower()
    if search_criteria not in options:
        raise ValueError(f"Invalid search criteria '{search_criteria}'. Try again")

    return search_criteria


def get_user_choice():
    options = ['search films', 'get table description']
    user_request = input(f"What do you wanna do?\nOptions {options}: ").lower()
    if user_request not in options:
        raise ValueError(f"Invalid entered option '{user_request}'. Try again")
