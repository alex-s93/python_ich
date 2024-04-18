import constants


def get_category_from_user(categories):
    usr_input = input("Enter Id of category: ")
    if int(usr_input) not in [category_id for category_id, _ in categories]:
        raise ValueError(constants.INVALID_VALUE_MSG.format("category ID", usr_input))

    return int(usr_input)


def get_production_year_from_user():
    usr_input = input("Enter production year: ")
    if len(usr_input) != 4:
        raise ValueError(constants.INVALID_VALUE_MSG.format("year", usr_input))

    return int(usr_input)


def get_amount_of_films_from_user():
    usr_input = input("Enter amount of films you wanna get: ")
    if not usr_input.isdigit():
        raise ValueError(constants.INVALID_VALUE_MSG.format("amount", usr_input))

    return int(usr_input)


def get_search_operator_from_user():
    options = ['<', ">", '<=', '>=', '=', '!=']
    usr_input = input(f"Enter an operator for search. Options {options}: ")
    if usr_input not in options:
        raise ValueError(constants.INVALID_VALUE_MSG.format("operator", usr_input))

    return usr_input


def get_table_name_from_user(tables):
    usr_input = input("Which table description do you wanna see? ")
    if usr_input not in tables:
        raise ValueError(constants.INVALID_VALUE_MSG.format("table name", usr_input))

    return usr_input


def get_search_criteria_from_user():
    options = ['category', 'production year']
    usr_input = input(f"You can search by: {options}. What do you prefer? ").lower()
    if usr_input not in options:
        raise ValueError(constants.INVALID_VALUE_MSG.format("search criteria", usr_input))

    return usr_input


def get_user_choice():
    options = ['search films', 'get table description']
    user_request = input(f"What do you wanna do?\nOptions {options}: ").lower()
    if user_request not in options:
        raise ValueError(constants.INVALID_VALUE_MSG.format("entered option", user_request))

    return user_request
