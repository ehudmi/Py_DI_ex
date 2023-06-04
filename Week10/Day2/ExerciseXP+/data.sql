drop table students;

create table students(
id serial primary key,
last_name varchar(50) not null,
first_name varchar(50) not null,
birth_date date not null);

insert into students(last_name, first_name, birth_date)
values
('Benichou','Marc','02-11-1998'),
('Cohen','Yoan','03-12-2010'),
('Benichou','Lea','27-07-1987'),
('Dux','Amelia','07-04-1996'),
('Grez','David','14-06-2003'),
('Simpson','Omer','03-10-1980'),
('Miron','Ehud','03-12-1965');

select * from students;

select first_name, last_name from students where id=2;

select first_name, last_name from students where last_name='Benichou' and first_name='Marc';

select first_name, last_name from students where last_name='Benichou' or first_name='Marc';

select first_name, last_name from students where first_name ilike '%a%';

select first_name, last_name from students where first_name ilike 'a%';

select first_name, last_name from students where first_name ilike '%a';

select first_name, last_name from students where first_name ilike '%a_';

select first_name, last_name from students where id=1 and id=3;

select * from students where birth_date >= '01/01/2000';