import psycopg2
import matplotlib.pyplot as plt
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
x = []
y = []


with conn:
    print("Database opened successfully")
    cur = conn.cursor()
    cur.execute(query_1)
    for row in cur:
        x.append(row[0])
        y.append(row[1])
    plt.bar(x, y, width=0.1, alpha=0.6, color='blue', edgecolor="k", linewidth=2)
    plt.ylabel('Number of films')
    plt.title('The number of films of a certain genre')
    plt.show()

    x.clear()
    y.clear()
    cur.execute(query_2)
    for row in cur:
        x.append(row[0].strip())
        y.append(row[1])
    plt.pie(y, labels=x, shadow=True, autopct='%1.1f%%', startangle=180)
    plt.title('Films time, which is the longest')
    plt.show()

    x.clear()
    y.clear()
    cur.execute(query_3)
    for row in cur:
        y.append(row[1])
        x.append(row[0].strip())
    plt.bar(x, y, color='blue', edgecolor="k")
    plt.ylabel('Number of rating')
    plt.title('Movies with a rating higher than the average value (i.e. more popular)')
    plt.show()