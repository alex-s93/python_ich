
-- 1. Подключитесь к базе данных world (которая находится на удаленном сервере).
use world;

-- 2. Выведите список стран с языками, на которых в них говорят.
SELECT country.Name, countrylanguage.Language
FROM country
         INNER JOIN countrylanguage
                    ON country.Code = countrylanguage.CountryCode;


-- 3. Выведите список городов с их населением и названием стран
SELECT city.Name, city.Population, country.Name
FROM city
         INNER JOIN country
                    ON city.CountryCode = country.Code;


-- 4. Выведите список городов в South Africa
SELECT city.Name
FROM city
         INNER JOIN country
                    ON city.CountryCode = country.Code
WHERE country.Region = 'Southern Africa';

-- 5. Выведите список стран с названиями столиц. Подсказка: в таблице country есть поле Capital, которое содержит номер города из таблицы City.
SELECT country.Name, city.Name
FROM country
         INNER JOIN city
                    ON country.Capital = city.ID;

-- 6. Измените запрос 4 таким образом, чтобы выводилось население в столице.
SELECT country.Name, city.Name, city.Population
FROM country
         INNER JOIN city
                    ON country.Capital = city.ID;

-- 7. Напишите запрос, который возвращает название столицы United States
SELECT city.Name
FROM country
         INNER JOIN city
                    ON country.Capital = city.ID
WHERE country.Name = 'United States';

-- 8. Используя базу hr_data.sql, вывести имя, фамилию и город сотрудника.
use hr;
SELECT emp.first_name, emp.last_name, loc.city
FROM employees AS emp
         INNER JOIN departments AS dep
                    ON emp.department_id = dep.department_id
         INNER JOIN locations AS loc
                    ON dep.location_id = loc.location_id;

-- 9. Используя базу hr_data.sql, вывести города и соответствующие городам страны.
SELECT loc.city, countries.country_name
FROM locations AS loc
         INNER JOIN countries
                    ON loc.country_id = countries.country_id;