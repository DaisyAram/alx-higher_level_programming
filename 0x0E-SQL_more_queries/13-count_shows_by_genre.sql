-- lists all shows contained in hbtn_0d_tvshows tnd displays the number of shows linked to each.
SELECT tv_genres.name AS 'genre', 
FROM tv_genres RIGHT JOIN tv_shows_genres
ON tv_genres.id = tv_shows.genres_id
GROUP BY genre
ORDER BY number_of_shows DESC;
