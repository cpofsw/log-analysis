#!/usr/bin/env python3
import psycopg2

DBNAME = "news"


'''
 Questions:
 1: What are the most popular three articles of all time?
 2: Who are the most popular article authors of all time?
 3: On which days did more than 1% of requests lead to errors?

'''

first_query = '''select articles.title, count(*) as views from articles
 inner join log on log.path = concat('/article/', articles.slug)
 group by log.path, articles.title order by views desc limit 3;'''

second_query = '''select authors.name, count(*) as views from articles
inner join authors on authors.id=articles.author inner join
log on log.path = concat('/article/', articles.slug)
group by authors.name order by views desc;'''


third_query = '''select * from (select date,
CAST((CAST(errorRequest AS float) * 100.0 ) /
CAST(totalRequest AS float) as DECIMAL(16,2))
 as errorpercentage from (select T.date, totalRequest, errorRequest
  from (select date(time) as date, count(*) as errorRequest from log
   where log.status like '%404%' group by date) as T inner join
    (select date(time) as date, count(*) as totalRequest  from
    log group by date) as E on T.date=E.date) as logtable) as
    errorRequest where errorpercentage >1.0;'''

first_question = 'What are the most popular three articles of all time?'
second_question = 'Who are the most popular article authors of all time?'
third_question = 'On which days did more than 1% of requests lead to errors?'


if __name__ == '__main__':
    conn = psycopg2.connect(database=DBNAME)
    curr = conn.cursor()
    curr.execute(first_query)
    res = curr.fetchall()
    print(first_question)
    for i in range(len(res)):
        print(i+1, ')', res[i][0], '--', res[i][1])
    print('')

    curr.execute(second_query)
    res = curr.fetchall()
    print(second_question)
    for i in range(len(res)):
        print(i+1, ')', res[i][0], '--', res[i][1])
    print('')

    curr.execute(third_query)
    res = curr.fetchall()
    print(third_question)
    for i in range(len(res)):
        print(i+1, ')', res[i][0], '--', res[i][1])
    print('')

    conn.close()
