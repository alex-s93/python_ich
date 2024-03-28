-- 1. Подключиться к базе данных world
USE world;

-- 2. Вывести население в каждой стране. Результат содержит два поля: CountryCode,
-- sum(Population). Запрос по таблице city.
SELECT CountryCode, SUM(Population) AS country_population
FROM city
GROUP BY CountryCode;

-- 3. Изменить запрос выше так, чтобы выводились только страны с населением более 3 млн
-- человек.
SELECT CountryCode, SUM(Population) AS country_population
FROM city
GROUP BY CountryCode
HAVING country_population > 3000000;

-- 4. Сколько всего записей в результате?
-- ОТВЕТ: 59

-- 5. Поменять запрос выше так, чтобы в результате вместо кода страны выводилось ее название.
SELECT country.Name, SUM(city.Population) AS country_population
FROM city
         LEFT JOIN country
                   ON city.CountryCode = country.Code
GROUP BY CountryCode
HAVING country_population > 3000000;

-- 6. Вывести количество городов в каждой стране (CountryCode, amount of cities).
SELECT CountryCode, COUNT(Name) AS amount_of_cities
FROM city
GROUP BY CountryCode;

-- 7. Поменять запрос так, чтобы вместо кодов стран, было названия стран.
SELECT country.Name, COUNT(city.Name) AS amount_of_cities
FROM city
         LEFT JOIN country
                   ON city.CountryCode = country.Code
GROUP BY CountryCode;

-- 8. Поменять запрос так, чтобы выводилось среднее количество городов в стране.
SELECT AVG(amount_of_cities) AS avg_city_amount
FROM city
         INNER JOIN (SELECT CountryCode, COUNT(Name) AS amount_of_cities
                     FROM city
                     GROUP BY CountryCode) AS t2
                    ON city.CountryCode = t2.CountryCode;