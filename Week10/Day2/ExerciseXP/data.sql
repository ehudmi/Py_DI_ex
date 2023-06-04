drop table customers;

create table items(
item_id serial primary key,
item_name varchar(255) not null,
item_price integer not null
);

create table customers(
user_id serial primary key,
cust_first varchar(255) not null,
cust_last varchar(255) not null
);

insert into items(item_name, item_price)
values
	('Small Desk',100),
	('Large Desk',300),
	('Fan',80);

insert into customers(cust_first, cust_last)
values
	('Greg', 'Jones'),
	('Sandra','Jones'),
	('Scott','Scott'),
	('Trevor','Green'),
	('Melanie','Johnson');
	
select * from items;

select * from items where item_price>80;

select * from items where item_price<300;

select * from customers where cust_last='Smith';

select * from customers where cust_last='Jones';

select * from customers where cust_first!= 'Scott';