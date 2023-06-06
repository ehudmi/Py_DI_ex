select * from address;

select 	first_name || ' ' || last_name as full_name from customer;

select distinct create_date from customer;

select * from customer order by first_name desc;

select film_id, title, description, release_year, rental_rate from film
order by rental_rate;

select address, phone from address where district='Texas';

select * from film where film_id=15 or film_id=150;

select * from film where title='The Spiderwick Chronicles';

select * from film where title ilike 'Th%';

select * from film order by rental_rate ;

select * from film order by rental_rate offset 10 rows
fetch next 10 rows only;

select * from payment;

select customer.first_name, customer.last_name, payment.amount, payment.payment_date
from customer inner join payment on
customer.customer_id=payment.customer_id;

select film.title from film inner join inventory on film.film_id!=inventory.film_id;

select city.city, country.country from city inner join country on
city.country_id=country.country_id;

select customer.customer_id, customer.first_name, customer.last_name,payment.amount,
payment.payment_date, staff.first_name, staff.last_name from
((customer inner join payment on customer.customer_id=payment.customer_id)
 inner join staff on payment.staff_id=staff.staff_id) order by staff.staff_id;