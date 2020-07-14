-- list all the cities
-- list all the cities
SELECT id, name FROM cities where state_id = (
       SELECT id FROM states WHERE name = "California")
ORDER BY id ASC;
