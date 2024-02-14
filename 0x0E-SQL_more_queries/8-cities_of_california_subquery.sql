-- lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT  STATES AS name;
FROM hbtn_0d_usa;
WHERE name = California
ORDER BY score ASC;
