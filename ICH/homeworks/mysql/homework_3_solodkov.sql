-- 1. Не подглядывая в решение в классе, создать таблицу weather с тремя полями:
-- 		название города (city)
-- 		дата (forecast_date)
-- 		температура в эту даты (temperature) 
CREATE TABLE weather(
		city VARCHAR(128),
        forecast_date DATE,
        temperature INT
);

-- 2. Вывести содержимое таблицы
SELECT * FROM weather;

-- 3. Добавить данные в таблицу, используя запрос INSERT
-- 		“29 августа 2023 года в Берлине было 30 градусов”
INSERT INTO weather(city, forecast_date, temperature) VALUES("Berlin", "2023-08-29", 30);

-- 4. Добавить еще 3 записи в таблицу (произвольную погоду в разных городах в разные дни). 
INSERT INTO weather(city, forecast_date, temperature) VALUES("Cologne", "2023-07-21", 26);
INSERT INTO weather(city, forecast_date, temperature) VALUES("Kaiserslautern", "2023-01-14", -9);
INSERT INTO weather(city, forecast_date, temperature) VALUES("Ludwigshafen", "2023-11-05", 4);

-- 5. Написать запрос, который возвращает содержимое таблицы. 
SELECT * FROM weather;

-- 6. Изменить данные в таблице о температуре в Берлине с 30 на 26 градусов.
UPDATE weather
SET temperature = 26
WHERE city = "Berlin";

-- 7. Поменяйте во всей таблице название города на Paris для записей, где температура выше 25 градусов. 
UPDATE weather
SET city = "Paris"
WHERE temperature > 25;

-- 8. Добавить к таблице weather дополнительный столбец min_temp типа integer.
ALTER TABLE weather
ADD min_temp INTEGER;

-- 9. Используя команду update, установить значение поля min_temp в 0 для всех записей в таблице.
UPDATE weather
SET min_temp = 0;