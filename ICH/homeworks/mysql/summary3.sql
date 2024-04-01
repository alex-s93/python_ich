-- получить репорт по department_id с минимальной и максимальной зарплатой, с ранней и поздней датой прихода на работу
-- и с количествов сотрудников. Сортировать по количеству сотрудников (по убыванию)
USE hr;

SELECT department_id, MIN(salary), MAX(salary), MIN(hire_date), MAX(hire_date), COUNT(employee_id) AS emp_count
FROM employees
GROUP BY department_id
ORDER BY emp_count DESC;

-- Сколько сотрудников которые работают в одном и том же отделе и получают одинаковую зарплату?
SELECT department_id, salary, COUNT(employee_id) AS emp_count
FROM employees
GROUP BY department_id, salary
HAVING emp_count > 1;

-- 3. Получить количество департаментов в котором есть сотрудники
SELECT COUNT(DISTINCT (department_id))
FROM employees
WHERE department_id IS NOT NULL;

-- Получить количество сотрудников с одинаковым количеством букв в имени. При этом показать только тех у кого длина
-- имени больше 5 и количество сотрудников с таким именем больше 20. Сортировать по длине имени
SELECT COUNT(first_name) AS emp_count, LENGTH(first_name) AS f_length
FROM employees
WHERE LENGTH(first_name) > 5
GROUP BY f_length
HAVING emp_count > 20
ORDER BY f_length DESC;

