#! /usr/bin/env python


import psycopg2
DBNAME = "news"

def get_query(query):
    """Connect ot the database."""
    try:
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
        c.execute(query)
        data = c.fetchall()
        db.close()
        return data
    except:
        print("Database not found! Check dbname")


#Queries
def query1():
    """ Run query1: What are the most popular 3 articles of all time?"""
    query = """
    select title, count(*) as views from articles, log
    where log.path like concat('%', articles.slug)
    and log.status like '%200%'
    group by articles.title
    order by views desc limit 3;
    """
    results = get_query(query)

    print("\nThe top 3 articles viewed are:")
    for i, r in enumerate(results):
        title = r[0]
        views = str(r[1]) + " views"
        print(str(i+1) + ": " + title + " -- " + views)


# Query2: Who are the most popular article authors of all time
# name from authors, count path from logs and match article.author with author.id to match path
def query2():
    """Run query2: Who are the most popular article authors of all time"""
    query = """
    select authors.name, count(*) as views
    from articles, authors, log
    where articles.author = authors.id
    and log.path like concat('%', articles.slug)
    and log.status like '%200%'
    group by authors.name
    order by views desc limit 3;
    """
    results = get_query(query)
    print("\nThe top 3 authors viewed are:")
    count = 1
    for r in results:
        print(str(count) + ": " + r[0] + " -- " + str(r[1]) + " views")
        count += 1
        #print(str(id) + author + view)


# Query 3: On which days did more than 1% or requests lead to errors
# log status code not equal to 200 or equal to 404
def query3():
    """Query 3: On which days did more than 1% or requests lead to errors"""

    query = """
    select date(time), round(100.0 * sum(case log.status when '200 OK'
    then 0 else 1 end)/count(log.status), 2) as pct_error from log
    group by date(time)
    HAVING round(100.0 * sum(case log.status when '200 OK'
    then 0 else 1 end)/count(log.status), 2) > 1
    order by pct_error desc;
    """
    results = get_query(query)
    print("\nDays with more than 1% errors:")
    for r in results:
        date = r[0].strftime("%B-%d-%Y")
        errors = str(round(r[1], 2)) + "%" + " error"
        print(date + " -- " + errors)

print("Query results:")
query1()
query2()
query3()
