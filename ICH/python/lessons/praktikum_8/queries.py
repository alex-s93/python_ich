categories_query = "SELECT category_id, name FROM category"
film_by_category_query = """
SELECT 
film.title, film.release_year, film.description 
FROM film
INNER JOIN film_category ON film_category.film_id = film.film_id
WHERE film_category.category_id = {id}
LIMIT {amount}
"""