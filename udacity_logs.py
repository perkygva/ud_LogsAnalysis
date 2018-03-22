# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 11:03:37 2018

@author: pc01
"""

import psycopg2

def connect(dbname = "news"):
    """Connect ot the database."""
    try:
        db = psycopg2.connect("dbanme={}" .format(dbname))
        c = db.cursor()
        return db, c
    except:
        print("Database not found! Checkn dbname")
    
    
#Queries
    
# Query1: What are the most popular 3 articles of all time?
query1 = """select title, count(*) as views from articles, log
where log.path like concat('%', articles.slug)
and log.status like '%200%'
group by articles.title
order by views desc limit 3;
"""

# Query2: Who are the most popular article authors of all time
# name from authors, count path from logs and match article.author with author.id to match path
query2 = """select authors.name, count(*) as views
from articles, authors, log
where articles.author = authors.id
and log.path like concat('%', articles.slug)
and log.status like '%200%' 
group by authors.name
order by views desc limit 3;
"""
# Query 3: On which days did more than 1% or requests lead to errors
# log status code not equal to 200 or equal to 404
query3 = """select date(time), round(100.0 * sum(case log.status when '200 OK'
then 0 else 1 end)/count(log.status), 2) as "pct_error" from log 
group by date(time) order by "pct_error" desc;
"""


def get_query(query):
    """Return results for each query"""
    db, c = connect()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results
    
def print_query(query):
    results = get_query(query)
    print(results["title"])
    ending = "%" if query == "errors" else "views
    for result in results:
        print('\t' + str(result[0]) + "==" + str(result[1]) + ending)
    
     
if name == "__main__":
    dbname = "news"
    queries = [query1, query2, query3]
    for query in queries:
        print_query(query)