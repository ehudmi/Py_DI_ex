select * from items;

select * from customers;

select * from items order by item_price;

select * from items where item_price>=80
order by item_price desc;

select cust_first, cust_last from customers 
where user_id<=3 order by cust_first;

select cust_last from customers order by cust_last desc;