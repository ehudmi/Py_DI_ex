select get_film_count(40, 90)

-- Function
-- create [or replace] function function_name(param1, param2)
create function swap(inout x int,
					inout y int)
	language plpgsql
	as
$$
begin
	select x, y into y, x;
	end;
$$

create function get_film_count(in len_from int,
							   in len_to int,
							  out film_count integer)
	returns int--return_type
	language plpgsql
as
$$
declare
-- 	-- variable declaration
-- 	film_count integer;
begin
	--logic
	select count(1) into film_count
	from film
	where length between len_from and len_to;
	
	return film_count;
end;
$$