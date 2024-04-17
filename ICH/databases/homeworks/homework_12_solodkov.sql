USE world;

-- 1. Вывести количество городов для каждой страны. Результат должен содержать CountryCode, CityCount (количество
-- городов в стране). Поменяйте запрос с использованием джойнов так, чтобы выводилось название страны вместо CountryCode.
SELECT CountryCode, COUNT(Name) AS CityCount
FROM city
GROUP BY CountryCode;

SELECT country.Name, COUNT(city.Name) AS CityCount
FROM city
         INNER JOIN country ON city.CountryCode = country.Code
GROUP BY CountryCode;

-- 2. Используя оконные функции, вывести список стран с продолжительностью жизнью и средней продолжительностью жизни.
SELECT Name,
       LifeExpectancy,
       ROUND(AVG(LifeExpectancy) OVER (), 2) AS avg_life_expectancy
FROM country;

-- 3. Используя ранжирующие функции, вывести страны по убыванию продолжительности жизни.
SELECT Name,
       LifeExpectancy,
       DENSE_RANK() OVER (ORDER BY LifeExpectancy DESC) AS life_rank
FROM country;

-- 4. Используя ранжирующие функции, вывести третью страну с самой высокой продолжительностью жизни.
SELECT *
FROM (SELECT Name,
             LifeExpectancy,
             DENSE_RANK() OVER (ORDER BY LifeExpectancy DESC) AS life_rank
      FROM country) AS t1
WHERE life_rank = 3;