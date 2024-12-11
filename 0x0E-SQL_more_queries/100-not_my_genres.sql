-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
-- lists all rows of a table linked to another table
SELECT 
    tv_genres.name
FROM 
    tv_genres
WHERE 
    tv_genres.id NOT IN (
        SELECT 
            tv_show_genres.genre_id
        FROM 
            tv_show_genres
        INNER JOIN 
            tv_shows ON tv_show_genres.show_id = tv_shows.id
        WHERE 
            tv_shows.title = 'Dexter'
    )
ORDER BY 
    tv_genres.name ASC;
