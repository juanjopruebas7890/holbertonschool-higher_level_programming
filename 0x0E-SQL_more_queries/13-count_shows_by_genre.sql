-- list all genres
SELECT tv_genres.name genre, COUNT(*) number_of_shows FROM tv_genres INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id GROUP BY tv_genres.name ORDER BY number_of_shows DESC;
