--  Вывести текущую дату и время.
select now();

--  Вывести текущий год и месяц
select YEAR(now()), MONTH(now());
select extract(YEAR_MONTH from now());

--  Вывести текущее время
select TIME(now());

--  Вывести название текущего дня недели
select dayname(now());

--  Вывести номер текущего месяца
select month(now());

--  Вывести номер дня в дате “2020-03-18”
select day(now());

--  Подключиться к базе данных shop (которая находится на удаленном сервере).
use shop;

--  Определить какие из покупок были совершены апреле (4-й месяц)
select ORDER_ID, ODATE from ORDERS
where monthname(ODATE) = 'April';
-- where month(ODATE) = 4;

--  Определить количество покупок в 2022-м году
select count(ORDER_ID) from ORDERS
where year(ODATE) = 2022;

-- Определить, сколько покупок было совершено в каждый день. Отсортировать строки в порядке возрастания количества
-- покупок. Вывести два поля - дату и количество покупок
select ODATE, count(ORDER_ID) as order_count from ORDERS
group by ODATE
order by order_count;

--  Определить среднюю стоимость покупок в апреле
select avg(AMT) as avg_amt from ORDERS
where MONTH(ODATE) = 4;
