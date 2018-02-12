#!/usr/bin/env python

import psycopg2

DBNAME = "news"


def fetchFromDatabase(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


def top_posts():
    query = """
    SELECT articles.title, count(articles.title) as num
    FROM articles, log
    WHERE log.path = '/article/' || articles.slug
    GROUP BY articles.title
    ORDER BY num desc
    LIMIT 3;
  """
    return fetchFromDatabase(query)


def top_authors():
    query = """
    SELECT top_authors.author, top_authors.count, authors.name
    FROM top_authors, authors
    WHERE top_authors.author = authors.id;
  """
    return fetchFromDatabase(query)


def errors():
    query = """
    SELECT * from top_errors where percentage > 1;
  """
    return fetchFromDatabase(query)


print "Top Posts"
top_posts = top_posts()
for post in top_posts:
    print post[0] + " - " + str(post[1]) + " views"

print "\n"
print "Top Authors"
top_authors = top_authors()
for author in top_authors:
    print author[2] + " - " + str(author[1]) + " views"

print "\n"
print "Days with more than 1 percent errors"
errors = errors()
for error in errors:
    percentage = "{:.2f}".format(error[1]) + "%"
    print error[0].strftime("%d. %B %Y") + " - " + percentage
