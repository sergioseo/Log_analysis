#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2


def general():
    # Conectar ao banco de dados
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor()

    # Quais são os três artigos mais populares de todos os tempos?
    top_articles = """
      select * from articleSum limit 3;
      """
    cur.execute(top_articles)
    print("Quais são os três artigos mais populares de todos os tempos?")
    for (titulo, view) in cur.fetchall():
        print("    {} - {} views".format(titulo, view))
    print("\n")

    # Quem são os autores de artigos mais populares de todos os tempos?
    top_authors = """
    select name, sum(articleSum.views) as views
    from authorId, articleSum
    where articleSum.title = authorId.title 
    group by name order by views desc;"""
    """
    cur.execute(top_authors)
    print("Quem são os autores de artigos mais populares de todos os tempos?")
    for (name, view) in cur.fetchall():
        print("    {} - {} views".format(name, view))
    print("\n")

    # Em quais dias mais de 1% das requisições resultaram em erros?
    percentual_erros = """
    select time, (CASE WHEN percent > 1.0 THEN 'Mais do que 1%' 
    when percent <= 1.0 then 'none' else null END) as situation
    from status;
    """
    cur.execute(percentual_erros)
    print("Em quais dias mais de 1% das requisições resultaram em erros?")
    for (date, perc) in cur.fetchall():
        print("    {} - {}".format(date, perc))
    print("\n")

    cur.close()
    conn.close()

if __name__ == "__main__":
    general()
