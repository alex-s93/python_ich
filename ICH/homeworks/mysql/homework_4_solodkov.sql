use 190224_solodkov;

-- 1. Вывести все заказы, отсортированные по убыванию по стоимости 
SELECT * FROM orders ORDER BY price DESC;

-- 2. Вывести всех заказчиков, у которых почта зарегистриварована на gmail.com
SELECT * FROM customer where email like "%@gmail.com";

-- 3. Вывести заказы, добавив дополнительный вычисляемый столбец status, который вычисляется по стоимости заказа и имеет три значения: low, middle, high. 
SELECT *,
	CASE
		WHEN price > 50000 THEN "high"
        WHEN price between 20000 and 50000 THEN "middle"
        WHEN price < 20000 THEN "low"
	END 
    AS status
FROM orders;

-- 4. Вывести заказчиков по убыванию рейтинга.
SELECT customer_id,
	CASE
		WHEN price > 50000 THEN "high"
        WHEN price between 20000 and 50000 THEN "middle"
        WHEN price < 20000 THEN "low"
	END 
    AS status
FROM orders
ORDER BY status DESC;

-- 5. Вывести всех заказчиков из города на ваш выбор. 
SELECT * FROM customer  WHERE city = "Archiemouth";

-- 6. Написать запрос, который вернет самый часто продаваемый товар. 
SELECT item_name, count(*) AS qt 
FROM orders 
GROUP BY item_name 
ORDER BY qt DESC 
LIMIT 1;

-- 7. Вывести список заказов с максимальной скидкой. 
SELECT *, 
	(price - discount_price) AS discount_value 
FROM orders 
WHERE (price - discount_price) = (select max(price - discount_price) from orders);

-- ORDER BY discount_value DESC 
-- LIMIT 3; -- так как в задании сказано что нужен список заказов (подразумевается несколько)

-- 8. Ответьте в 1 предложении: как вы определите скидку? 
-- путем вычитания из изначальной цены скидочной цены. таким образом мы получаем размер скидки в сумме а не в процентах

-- 9. Ответьте в 1 предложении: может ли это быть разница между нормальной ценой и скидочной ценой? 
-- да, может, согласно ответу в задании 8

-- 10. Написать запрос, который выведет все заказы с дополнительным столбцом процент_скидки, который содержит разницу в процентах между нормальной и скидочной ценой?
SELECT *,
	round((price - discount_price)/price * 100, 2) as discount_percent
FROM orders;