CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
);

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar');

SELECT * FROM FirstTab;

CREATE TABLE SecondTab (
    id integer 
);

INSERT INTO SecondTab VALUES
(5),
(NULL);


SELECT * FROM SecondTab;

SELECT COUNT(*)
   FROM FirstTab AS ft WHERE ft.id not IN ( SELECT id FROM SecondTab WHERE id IS NULL)
-- the answer is 4, there are 4 not null values in firsttab id.
--I was mistaken, null makes the value basically unreachable, therefore
-- it doesn't matter' it will see what is not everything, so the count is nothing.

SELECT COUNT(*) 
 FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
--  the answer is 2, there are 2 values where the id is not 5, null is not inside the values
-- we can reach.

SELECT COUNT(*) 
 FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
--  the answer will be 2 again, for the same reasons in the last question.
-- I was mistaken. according to these 3 examples, null is basically
-- an unknown value. therefore, you don't know what is in it and what
-- is not in it. because of that, the count returns 0, you don't know
-- if 7 or 6 are in it.

SELECT COUNT(*) 
 FROM FirstTab AS ft WHERE ft.id NOT IN
 ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
-- 	here it will return 2. the condition returns 5, therefore
-- the 5 id will not be counted. because we don't know if null will be
-- 5, it won't be counted either. therefore, only 6 and 7 will be counted.