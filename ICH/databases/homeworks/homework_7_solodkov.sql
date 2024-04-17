-- 1. Подключитесь к базе данных hr (которая находится на удаленном сервере).
use hr;

-- 2. Выведите количество сотрудников в базе
select count(*) from employees;


-- 3. Выведите количество департаментов (отделов) в базе
select count(*) from departments;

-- 4. Подключитесь к базе данных World (которая находится на удаленном сервере).
use world;

-- 5. Выведите среднее население в городах Индии (таблица City, код Индии - IND)
select
    avg(Population) as average_population,
    CountryCode
from city
where CountryCode = 'IND';

-- 6. Выведите минимальное население в индийском городе и максимальное.
select
    min(Population) as min_population,
    max(Population) as max_population,
    CountryCode
from city
where CountryCode = 'IND';

-- 7. Выведите самую большую площадь территории.
select max(country.SurfaceArea) from country;

-- 8. Выведите среднюю продолжительность жизни по странам.
select avg(country.LifeExpectancy) as average_life_expectancy from country;

-- 9. Найдите самый населенный город (подсказка: использовать подзапросы)
select Name from city where Population = (select max(Population) from city)