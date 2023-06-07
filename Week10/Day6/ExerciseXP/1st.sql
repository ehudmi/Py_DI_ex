select * from language;

select * from film where language_id!=1;

select film.title, film.description, language.name from film
left join language on film.language_id=language.language_id;

select film.title, film.description, language.name from film
right join language on film.language_id=language.language_id;

create table new_film(
	id serial primary key,
	name varchar(255) not null
)

insert into new_film (name)
values
('The Spiderwick Chronicles'),
('2012'),
('The Shining'),
('Avengers: Endgame');

drop table customer_review;

create table customer_review(
	review_id serial primary key,
	film_id int ,
	language_id int,
	title varchar(255) not null,
	score int check(10>=score and score>=1),
	review_text text not null,
	last_update timestamp,
	constraint fk_film foreign key(film_id)  references new_film(id) on delete cascade,
	constraint fk_language foreign key(language_id) references language(language_id)
)

select * from new_film;

insert into customer_review(film_id, language_id, title, score,
review_text, last_update) values
(2, 1, 'Great!',7,'The movie is about the apocalypse and it is kinda great',
current_timestamp)

insert into customer_review(film_id, language_id, title, score,
review_text, last_update) values
(1, 1, 'Reminds me of my childhood',8,'I really love this movie and the game that came
 after it!',current_timestamp)
 
 select * from customer_review;
 
 delete from new_film where id=2;