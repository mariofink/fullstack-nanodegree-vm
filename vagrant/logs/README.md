## Database views

To answer the questions, I added 4 views to the database:

    CREATE VIEW top_authors AS 
    SELECT author, sum(num) AS count 
    FROM top_posts_authors 
    GROUP BY author 
    ORDER BY count desc;

    CREATE VIEW total_requests AS 
    SELECT date(time), count(status) AS c 
    FROM log 
    GROUP BY date(time);

    CREATE VIEW total_errors AS 
    SELECT date(time), count(status) AS c 
    FROM log 
    WHERE status = '404 NOT FOUND' 
    GROUP BY date(time);

    CREATE VIEW top_errors AS 
    SELECT total_requests.date, sum(total_errors.c * (100 / total_requests.c::float)) AS percentage
    FROM total_requests, total_errors
    WHERE total_requests.date = total_errors.date
    GROUP BY total_requests.date
    ORDER BY percentage desc;
