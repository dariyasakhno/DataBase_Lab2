
insert into runtime(id_runtime, runtime) VALUES
(1, 142),
(2, 152),
(3, 145),
(4, 156),
(5, 146);


insert into genre(id_genre, genre_name) values
(1, 'Crime'),
(2, 'Action'),
(3, 'Biography'),
(4, 'Adventure'),
(5, 'Western');

insert into rating(id_rating, m_rating) VALUES
(1, 9.2),
(2, 9.1),
(3, 8),
(4, 8.9),
(5, 8.7);


insert into movies(m_name, id_genre, id_rating, id_runtime) VALUES
('The Godfather', 1 ,2, 1),
('The Dark Knight',2 ,1,1),
('Pulp Fiction', 2 ,3, 3),
('Inception', 1,4,5),
('Forrest Gump', 3, 1, 2),
('Fight Club', 4, 2, 2);