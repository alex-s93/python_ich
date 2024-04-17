# task 1
SELECT * FROM employees WHERE job_id = "IT_PROG";

# task 2
SELECT * FROM employees WHERE job_id = "AD_VP";

# task 4/a 
SELECT * FROM employees WHERE salary between 10000 and 20000;

# task 4/b 
SELECT * FROM employees WHERE department_id not in(30,60,100);

# task 4/c
SELECT * FROM employees WHERE first_name like "%_ll_%";

# task 4/d
SELECT * FROM employees WHERE last_name like "%a";

# task 5
SELECT * FROM employees WHERE salary > 10000;

# task 6
SELECT * FROM employees WHERE salary > 10000 and last_name like "L%";

# task 7
# при выполнении запроса `select *  from employees where salary > 10000 or salary <= 10000;` вернется выборка со всеми работниками

# task 8
# `select *  from employees where salary > 10000 or salary < 10000` - этот запрос должен вывести значения, без работников, чья зарплата == 10000

# task 9
# `select *  from employees where salary > 10000 and salary < 5000;` - этот запрос вернет пустую выборку так как не может быть одновременно зарплата и больше 10к и меньше 5к