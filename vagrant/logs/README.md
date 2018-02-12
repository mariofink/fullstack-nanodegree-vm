# Logs Analysis project

This program analyses the logs of a fictive news page. It answers the following questions:

* What are the top 3 posts?
* Who are the top authors?
* On which days did the log contain more than 1% of errors?


## Database setup

* Bring up the Vagrant-based virtual machine by running
    
        cd vagrant
        vagrant up
        
* Download & unzip the test data from: [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
* Put the newsdata.sql file inside the vagrant shared folder
* SSH into the virtual machine

        vagrant ssh

* Unzip and import the newsdata.sql file

        cd /vagrant
        psql -d news -f newsdata.sql

The database is now ready. Continue to create the views listed below.

## Create database views

To answer the questions, I added these views to the database:

    CREATE VIEW top_posts_authors AS
    SELECT articles.id, articles.author, count(articles.id) as num
    FROM articles, log
    WHERE log.path = '/article/' || articles.slug
    GROUP BY articles.id
    ORDER BY num desc;

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

## Running the log analyser
Now you can finally run the log analyser:

    python loganalyser.py

## Expected result

    Top Posts
    Candidate is jerk, alleges rival - 338647 views
    Bears love berries, alleges bear - 253801 views
    Bad things gone, say good people - 170098 views


    Top Authors
    Ursula La Multa - 507594 views
    Rudolf von Treppenwitz - 423457 views
    Anonymous Contributor - 170098 views
    Markoff Chaney - 84557 views


    Days with more than 1 percent errors
    17. July 2016 - 2.26%
