select * from actor;
-- 200 actors

insert into actor(first_name)
values('John');

-- it fails because there is a not null constraint on first and last name