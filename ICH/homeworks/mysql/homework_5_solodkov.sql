show databases;
use world;
-- 2. Посмотреть на таблицы city, country из базы world. В каждой таблице есть поле название (Name) и население (Population).
-- Поле Name в одной таблице означает название города, а в другой - название страны.
describe city;
describe country;
-- Написать запрос с помощью UNION, который выводит список названий всех городов и стран с их населением.
-- Итоговая выборка должна содержать два столбца: Name, Population.
select Name, Population from city
union
select Name, Population from country;

-- 3. Посмотреть на таблицы в базе world и объяснить ограничения нескольких столбцов - ответить 1 предложением.
show create table country;
-- поля Code, Name, Region имеют ограничения: not null - поле не может быть пустым.
-- поле Continent может принять только значения из специального списка, определенного в enum. так же не может быть пустым


-- 4. Далее работаем на локальном сервере. Создать новую таблицу citizen, которая содержит следующие поля:
-- уникальное автоинкрементное, номер соц страхования, имя, фамилию и емейл.
create table citizen(
    id int auto_increment primary key,
    insurance_id int unique not null,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    email varchar(50)
);

-- 5. На вашем локальном сервере в любой базе создать таблицу без ограничений (любую, можно взять с урока).
create table neighbors(
    id int,
    first_name varchar(50),
    last_name varchar(50),
    flat_number int
);

-- 6. Добавить в таблицу 5 значений. Добавить 3 человека с одинаковыми именами и 2 человека без lastname
insert into neighbors(id, first_name, last_name, flat_number) values
(1, 'John', 'Smith', 203),
(2, 'John', 'Johnson', 105),
(3, 'John', 'Williams', 401);
insert into neighbors(id, first_name, flat_number) values
(4, 'Emma',  302),
(5, 'Daniel',  201);

-- 7. Использовать оператор alter table … modify , чтобы добавить ограничение not null на поле firstname и lastname.
alter table neighbors
modify first_name varchar(50) not null;
alter table neighbors
modify last_name varchar(50) not null;

-- 8. Добавить ограничение unique для пары firstname\lastname.
alter table neighbors
add constraint unique(first_name, last_name);

-- 9. Удалить таблицу из базы и пересоздать ее, модифицировав запрос add table так, чтобы он учитывал ограничения (см примеры из класса).
drop table neighbors;
create table neighbors(
    id int,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    flat_number int,
    unique (first_name, last_name)
);

-- 10. Добавить правильные и неправильные данные (нарушающие и не нарушающие ограничения).
insert into neighbors(id, first_name, last_name, flat_number) values
-- правильные данные
(1, 'John', 'Smith', 203),
(2, 'John', 'Johnson', 105),
(3, 'John', 'Williams', 401);
insert into neighbors(id, first_name, flat_number) values
-- неправильные данные
(4, 'Emma',  302),
(5, 'Daniel',  201);