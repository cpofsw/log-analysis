# Log Analysis Project

The goal of this project is to create a reporting tool to answer some questions.
Check the questions below, noting that the answers are just examples and not the correct ones.

## 1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

Example:

"Princess Shellfish Marries Prince Handsome" — 1201 views
"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
"Political Scandal Ends In Political Scandal" — 553 views

## 2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

Example:

Ursula La Multa — 2304 views
Rudolf von Treppenwitz — 1985 views
Markoff Chaney — 1723 views
Anonymous Contributor — 1023 views

## 3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

### The original news database can be checked by dropping all the tables and importing the database again, as explained below:

In psql:

```
drop table log;
drop table articles;
drop table authors;
```

Then in the shell, to import the data: [Download newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

`psql -d news -f newsdata.sql`

Run the script:

`python main.py`

The answers that the reporting tool provides can be viewed in this file : `answers.txt`.
