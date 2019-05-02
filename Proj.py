#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import psycopg2


dbname = "news"
conn = psycopg2.connect(dbname)
c = conn.cursor()
query = """
select substring(articles,10) as articles, count(*) as views 
from geral 
group by articles 
order by views desc 
limit 3;
"""

c.execute(query)
geral = c.fetchall()
print(geral)

""" 
### Quais sao os top 3 artigos ####

select substring(articles,10) as articles, count(*) as views 
from geral 
group by articles 
order by views desc 
limit 3;

### Quais autores mais populares? ####

select authors,count(*) as views 
from geral 
group by authors 
order by views desc 
limit 3;

### Em quais dias mais de 1% das requisições resultaram em erro? ###

create view status as 
	select time::date, (count(case when status != '200 OK' and then 1 else null end)::float/count(status)::float)*100 as percent 
FROM log 
GROUP BY time::date 
ORDER BY percent DESC;

select time, (CASE WHEN percent > 1.0 THEN 'MORE THEN 1%' when percent <= 1.0 then 'none' else null END) as situation 
from status;
"""




























