--  Вывести текущую дату и время.
SELECT NOW();

--  Вывести текущий год и месяц
SELECT YEAR(NOW()), MONTH(NOW());
SELECT EXTRACT(YEAR_MONTH FROM NOW());
# месяц в виде названия
SELECT DATE_FORMAT(NOW(), '%Y-%M');
# месяц в виде номера
SELECT DATE_FORMAT(NOW(), '%Y-%m');

--  Вывести текущее время
SELECT TIME(NOW());

--  Вывести название текущего дня недели
SELECT DAYNAME(NOW());

--  Вывести номер текущего месяца
SELECT MONTH(NOW());

--  Вывести номер дня в дате “2020-03-18”
SELECT DAY(NOW());

--  Подключиться к базе данных shop (которая находится на удаленном сервере).
USE shop;

--  Определить какие из покупок были совершены апреле (4-й месяц)
SELECT ORDER_ID, ODATE
FROM ORDERS
WHERE MONTHNAME(ODATE) = 'April';
-- where month(ODATE) = 4;

--  Определить количество покупок в 2022-м году
SELECT COUNT(ORDER_ID)
FROM ORDERS
WHERE YEAR(ODATE) = 2022;

-- Определить, сколько покупок было совершено в каждый день. Отсортировать строки в порядке возрастания количества
-- покупок. Вывести два поля - дату и количество покупок
SELECT ODATE, COUNT(ORDER_ID) AS order_count
FROM ORDERS
GROUP BY ODATE
ORDER BY order_count;

--  Определить среднюю стоимость покупок в апреле
SELECT AVG(AMT) AS avg_amt
FROM ORDERS
WHERE MONTH(ODATE) = 4;
