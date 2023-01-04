CREATE TABLE runtime(
  id_runtime INT NOT NULL,
  runtime INT NOT NULL
);

CREATE TABLE genre(
  id_genre INT NOT NULL,
  genre_name varchar(50) NOT NULL
);

CREATE TABLE rating(
  id_rating INT NOT NULL,
  m_rating numeric NOT NULL
);

CREATE TABLE movies(
  m_name char(100) NOT NULL,
  id_genre INT NOT NULL,
  id_rating INT NOT NULL,
  id_runtime INT NOT NULL
);

ALTER TABLE movies ADD PRIMARY KEY (m_name); 
ALTER TABLE rating ADD PRIMARY KEY (id_rating); 
ALTER TABLE runtime ADD PRIMARY KEY (id_runtime); 
ALTER TABLE genre ADD PRIMARY KEY (id_genre); 
 
 
ALTER TABLE movies ADD CONSTRAINT FK_movies_rating FOREIGN KEY (id_rating) REFERENCES rating (id_rating);
ALTER TABLE movies ADD CONSTRAINT FK_movies_runtime FOREIGN KEY (id_runtime) REFERENCES runtime (id_runtime);
ALTER TABLE movies ADD CONSTRAINT FK_movies_genre FOREIGN KEY (id_genre) REFERENCES genre (id_genre);