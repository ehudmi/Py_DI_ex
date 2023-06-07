create table customer(
	customer_id serial primary key,
	first_name varchar(55) not null,
	last_name varchar(55) not null
);

create table customer_profile(
	profile_id serial primary key,
	isLoggedIn boolean default false,
	customer_id integer not null,
	constraint fk_customerId foreign key(customer_id)
	references customer(customer_id)
);

insert into customer(first_name,last_name) values
('John','Doe'),('Jerome','Lalu'),('Lea','Rive');

insert into customer_profile(isloggedin, customer_id) values
(true, (select customer_id from customer where first_name='John')),
(false, (select customer_id from customer where first_name='Jerome'));

select customer.first_name from customer inner join customer_profile on
customer.customer_id=customer_profile.customer_id;

select customer.first_name, customer_profile.isloggedin
from customer left join customer_profile on
customer.customer_id=customer_profile.customer_id;

select count(isloggedin) from customer_profile where
isloggedin!=true;

-- Part II
create table book(
book_id serial primary key,
title varchar(255) not null,
author varchar(255) not null);

insert into book(title, author) values
('Alice In Wonderland', 'Lewis Carroll'),('Harry Potter','J.K Rowling'),
('To Kill a Mockingbird','Harper Lee');

create table student(
student_id serial primary key,
name varchar(255) not null unique,
age integer check(age<=15));

insert into student(name,age) values
('John', 12),('Lera', 11), ('Patrick', 10),('Bob', 14);

create table library(
book_id integer not null,
student_id integer not null,
borrowed_date date not null,
foreign key (book_id) references book(book_id)
on delete cascade on update cascade,
foreign key (student_id) references student(student_id)
on delete cascade on update cascade);

select * from book;

insert into library values
((select book_id from book where title ilike 'Alice%'),
 (select student_id from student where name='John'),'15-02-2022'),
 ((select book_id from book where title ilike 'To Kill%'),
 (select student_id from student where name='Bob'),'03-03-2021'),
 ((select book_id from book where title ilike 'Alice%'),
 (select student_id from student where name='Lera'),'23-05-2021'),
 ((select book_id from book where title ilike 'Harry%'),
 (select student_id from student where name='Bob'),'12-08-2021');
 
 select * from library;
 
 select student.name, book.title from library inner join student on
 library.student_id=student.student_id inner join book on
 library.book_id=book.book_id;
 
 select avg(student.age) from library inner join student on
 library.student_id=student.student_id inner join book on
 library.book_id=book.book_id where book.title ilike 'Alice%';
 
 delete from student where name ilike 'John';
 
 select * from library;
--  the library table updated itself.