-- 1. Подключитесь к базе данных Students (которая находится на удаленном сервере).
use Students;

-- 2. Найдите самого старшего студента
select name, age
from Students
where age = (select max(age) from Students);

-- 3. Найдите самого старшего преподавателя
select name, age
from Teachers
where age = (select max(age) from Teachers);

-- 4. Выведите список преподавателей с количеством компетенций у каждого
select Teachers.name, count(Teachers2Competencies.competencies_id) as competencies_amount
from Teachers
         left join Teachers2Competencies
                   on Teachers.id = Teachers2Competencies.teacher_id
group by Teachers.id;

-- 5. Выведите список курсов с количеством студентов в каждом
select Courses.Title, count(Students2Courses.student_id) as students_amount
from Courses
         left join Students2Courses
                   on Courses.id = Students2Courses.course_id
group by Courses.id;

-- 6. Выведите список студентов, с количеством курсов, посещаемых каждым студентом.
select Students.name, count(Students2Courses.course_id) as courses_amount
from Students
         left join Students2Courses
                   on Students.id = Students2Courses.student_id
group by Students.id;