-- list all the cities
SELECT id, name FROM cities where state_id = (
       SELECT id FROM STATES WHERE name = "California")
ORDER BY id ASC;
