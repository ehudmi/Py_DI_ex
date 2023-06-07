select * from film;

update film set language_id=2 where film_id in (1, 133);

-- store id and address id are the foreign keys in customer.
-- that means that when we insert into customer, the ids we insert in
-- store and address need to be included in the relevent tables.

drop table customer_review;
-- this does not need extra checks since nothing references it.

select count(*) from rental where return_date is null;

select film.title, payment.amount from film inner join
inventory on film.film_id= inventory.film_id inner join
rental on inventory.inventory_id=rental.inventory_id inner join
payment on rental.rental_id= payment.rental_id where
rental.return_date is null order by payment.amount desc limit 30;

select * from actor where first_name='Penelope' and last_name='Monroe';

select film.title from film inner join
film_actor on film.film_id=film_actor.film_id inner join
actor on film_actor.actor_id=actor.actor_id where
actor.actor_id=120 and film.description ilike '%sumo%';
-- first movie

select * from film where rating='R' and length<=60 and
description ilike '%documentary%';
-- second movie

select film.film_id,film.title,customer.first_name,customer.last_name,
rental.return_date from film inner join
inventory on film.film_id=inventory.film_id inner join
rental on inventory.inventory_id=rental.inventory_id inner join
customer on rental.customer_id=customer.customer_id inner join
 payment on customer.customer_id=payment.customer_id where
 film.rental_rate>=4 and customer.first_name='Matthew' and
 customer.last_name='Mahan' and rental.return_date>= '2005-07-28 00:00:00' and
 rental.return_date<= '2005-08-01 00:00:00';
--  sugar wonka is the 3rd film.
select * from film;
select film.film_id,film.title, film.description,
film.replacement_cost from film inner join
inventory on film.film_id=inventory.film_id inner join
rental on inventory.inventory_id=rental.inventory_id inner join
customer on rental.customer_id=customer.customer_id where
(film.title ilike '%boat%' or film.description ilike '%boat%')
and customer.first_name='Matthew' and customer.last_name='Mahan'
order by film.replacement_cost desc;
-- 4th movie is Stone Fire.