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
    for (titulo, views) in cur.fetchall():
        print("    {} - {} ".format(titulo, views))
    print("\n")

    # Quem são os autores de artigos mais populares de todos os tempos?
    top_authors = """
    select name, sum(articleSum.views) as views
    from authorId, articleSum
    where articleSum.title = authorId.title 
    group by name order by views desc;
    """
    cur.execute(top_authors)
    print("Quem são os autores de artigos mais populares de todos os tempos?")
    for (name, view) in cur.fetchall():
        print("    {} - {} views".format(name, view))
    print("\n")

    # Em quais dias mais de 1% das requisições resultaram em erros?
    erros = """
    select time as Date, percent as Errors from status where percent > 1.0;
    """
    cur.execute(erros)
    print("Em quais dias mais de 1% das requisições resultaram em erros?")
    for (date, perc) in cur.fetchall():
        print("    {} : {:.2f}% erro".format(date, perc))
    print("\n")

    cur.close()
    conn.close()

if __name__ == "__main__":
    general()
