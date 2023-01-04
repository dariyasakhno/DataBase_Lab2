select * from movies
select * from genre
select * from rating
select * from runtime
--Кількість фільмів певного жанру
select genre_name, count(movies.id_genre) as count_g from movies
join genre using(id_genre)
group by genre_name

--Фільми час, яких є найдовшим
select movies.m_name, runtime from movies
join runtime using(id_runtime)
where runtime <= (select avg(runtime) from movies join  runtime using(id_runtime))

--Фільми у яких рейтинг більше середнього значення(тобто більш популярні)
select movies.m_name, m_rating from movies
join rating using(id_rating)
where m_rating >=(select avg(m_rating) from movies join rating using(id_rating))