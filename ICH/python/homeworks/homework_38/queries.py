categories_query = "SELECT category_id, name FROM category"

film_by_category_query = """
SELECT 
film.title, film.release_year, film.description 
FROM film
INNER JOIN film_category ON film_category.film_id = film.film_id
WHERE film_category.category_id = {id}
LIMIT {amount}
"""

film_by_year_query = """
SELECT 
title, release_year, description 
FROM film
where release_year {operator} {year}
LIMIT {amount}
"""

tables_query = "show tables"

table_description_query = "show columns FROM {table}"
