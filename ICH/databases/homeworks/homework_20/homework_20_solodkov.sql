USE sakila;

# 1. Вывести названия фильмов с расшифровкой рейтинга для каждого. Рейтинги описаны здесь. В таблице film хранятся годы
# рейтингов. Нужно воспользоваться оператором case чтобы определить для каждого кода условие, по которому будет
# выводится его развернутое описание (1 предложение).
SELECT title,
       rating,
       CASE
           WHEN rating = "PG" THEN "Some material may not be suitable for children."
           WHEN rating = "G" THEN "All ages admitted."
           WHEN rating = "NC-17" THEN "No one 17 and under admitted."
           WHEN rating = "PG-13" THEN "Some material may be inappropriate for children under 13."
           WHEN rating = "R" THEN "Under 17 requires accompanying parent or adult guardian."
           ELSE "unknown MPA rating"
           END AS rating_description
FROM film;

# 2. Выведите количество фильмов в каждой категории рейтинга. Используем group by.
SELECT rating,
       COUNT(film_id) AS film_amount
FROM film
GROUP BY rating;

# 3. Используя оконные функции и partition by, выведите список названий фильмов, рейтинг и количество фильмов в каждом
# рейтинге. Объясните, чем отличаются результаты предыдущего запроса и запроса в этой задаче.
SELECT title,
       rating,
       COUNT(film_id) OVER (PARTITION BY rating) AS rating_film_amount
FROM film;
# Отличие от предыдущего запроса в том, что у нас отображается результат агрегирующей функции для каждой строки.
# В то время, как группировка убирает дубликаты


# 4. Изучите таблицы payment и customer. Выведите список всех платежей с указанием имени и фамилии каждого заказчика,
# датой платежа и суммой.
SELECT
    c.first_name,
    c.last_name,
    p.payment_date,
    p.amount
FROM payment AS p
         INNER JOIN customer AS c
             ON p.customer_id = c.customer_id;

# 5. Поменяйте предыдущий запрос так, чтобы дата выводилась в формате “число, название месяца, год” (без времени).
SELECT
    c.first_name,
    c.last_name,
    DATE_FORMAT(p.payment_date, '%Y-%m-%d') as payment_date,
    p.amount
FROM payment AS p
         INNER JOIN customer AS c
             ON p.customer_id = c.customer_id;