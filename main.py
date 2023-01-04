import psycopg2

username = 'postgres'
password = '****'
database = 'Dasha_DB'
host = 'localhost'
port = '5432'

query_1 = '''
select genre_name, count(movies.id_genre) as count_g from movies
join genre using(id_genre)
group by genre_name
'''

query_2 = '''
select movies.m_name, runtime from movies
join runtime using(id_runtime)
where runtime <= (select avg(runtime) from movies join  runtime using(id_runtime))
'''

query_3 = '''
select movies.m_name, m_rating from movies
join rating using(id_rating)
where m_rating >=(select avg(m_rating) from movies join rating using(id_rating))
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:

    print ("\nDatabase opened successfully\n")
    cur = conn.cursor()

    print('1.The number of films of a certain genre\n')
    cur.execute(query_1)
    for row in cur:
        print(row)

    print('\n2.Films time, which is the longest\n')
    cur.execute(query_2)
    for row in cur:
        print(row)

    print('\n3.Movies with a rating higher than the average value (i.e. more popular)\n')
    cur.execute(query_3)
    for row in cur:
        print(row)