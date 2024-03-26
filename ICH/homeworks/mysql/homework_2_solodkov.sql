# 1
USE hr;
SELECT * FROM employees;

# 2
SELECT salary FROM employees;

# 3
SELECT
	CASE
		WHEN salary > 10000 THEN 1
		WHEN salary < 10000 THEN 0
	END    
	AS salary_group
FROM employees;

# 4
# после оператора SELECT вместо знака * стоит конструкция CASE-WHEN и так же прописано имя для нашего кастомного столбика (AS column_name)

# 5
SELECT
	first_name,
	CASE
		WHEN salary > 10000 THEN 1
		WHEN salary < 10000 THEN 0
	END    
	AS salary_group
FROM employees;

# 6
SELECT 
	avg(salary)
    AS avg_salary_dp60_90_100
FROM employees
WHERE department_id in (60, 90, 100);

# 7
SELECT
	first_name, last_name,
    CASE
		WHEN salary < 10000 THEN "Junior"
        WHEN salary < 15000 and salary > 10000 THEN "Middle"
        WHEN salary > 15000 THEN "Senior"
	END
    AS level
FROM employees;

# 8
SELECT 
	job_id,
    CASE
		WHEN max_salary > 10000 THEN "high_payer"
        WHEN max_salary < 10000 THEN "low_payer"
	END
    AS payer_rank
FROM jobs;    

# 9
SELECT 
	job_id,
    IF(max_salary > 10000, "high_payer", if(max_salary < 10000, "low_payer", null))
    AS payer_rank
FROM jobs;    

# 10
SELECT 
	job_id,
    IF(max_salary > 10000, "high_payer", if(max_salary < 10000, "low_payer", null))
    AS payer_rank,
    max_salary
FROM jobs
ORDER BY max_salary DESC; 