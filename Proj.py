#!/usr/bin/env python3

import psycopg2


def general():
    # Conectar ao banco de dados
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor()

    # Quais são os três artigos mais populares de todos os tempos?
    top_articles = """
      select substring(articles,10) as articles, count(*) as views 
      from geral 
      group by articles 
      order by views desc 
      limit 3;
      """
    cur.execute(top_articles)
    print("Artigos mais populares:")
    for (titulo, view) in cur.fetchall():
        print("    {} - {} views".format(titulo, view))
    print("\n")

    # Quem são os autores de artigos mais populares de todos os tempos?
    top_authors = """
    select authors,count(*) as views 
    from geral 
    group by authors 
    order by views desc 
    limit 3;
    """
    cur.execute(top_authors)
    print("Autores mais populares:")
    for (name, view) in cur.fetchall():
        print("    {} - {} views".format(name, view))
    print("\n")

    # Em quais dias mais de 1% das requisições resultaram em erros?
    percentual_erros = """
    select time, (CASE WHEN percent > 1.0 THEN 'MORE THEN 1%' 
    when percent <= 1.0 then 'none' else null END) as situation 
    from status;
    """
    cur.execute(percentual_erros)
    print("Dia com mais de 1% de erro")
    for (date, perc) in cur.fetchall():
        print("    {} - {}% errors".format(date, perc))
    print("\n")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
