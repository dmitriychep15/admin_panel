CREATE SCHEMA IF NOT EXISTS content;

CREATE TABLE IF NOT EXISTS content.film_work (
    id uuid PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    creation_date DATE,
    rating FLOAT,
    type VARCHAR NOT NULL,
    created timestamp with time zone,
    modified timestamp with time zone
); 

CREATE TABLE IF NOT EXISTS content.genre(
    id uuid PRIMARY KEY, 
    name VARCHAR(255) NOT NULL, 
    description TEXT, 
    created timestamp with time zone, 
    modified timestamp with time zone
); 

CREATE TABLE IF NOT EXISTS content.person(
    id uuid PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL, 
    created timestamp with time zone,
    modified timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.genre_film_work(
    id uuid PRIMARY KEY, 
    genre_id uuid NOT NULL,
    film_work_id uuid NOT NULL,
    created timestamp with time zone, 
    FOREIGN KEY (genre_id) REFERENCES content.genre (id) ON DELETE CASCADE, 
    FOREIGN KEY (film_work_id) REFERENCES content.film_work (id) ON DELETE CASCADE
); 

CREATE TABLE IF NOT EXISTS content.person_film_work(
    id uuid PRIMARY KEY, 
    person_id uuid NOT NULL, 
    film_work_id uuid NOT NULL, 
    role TEXT, 
    created timestamp with time zone, 
    FOREIGN KEY (person_id) REFERENCES content.person (id) ON DELETE CASCADE, 
    FOREIGN KEY (film_work_id) REFERENCES content.film_work (id) ON DELETE CASCADE
); 

CREATE INDEX IF NOT EXISTS film_work_creation_date_idx ON content.film_work(creation_date); 

CREATE UNIQUE INDEX IF NOT EXISTS film_work_person_idx ON content.person_film_work (film_work_id, person_id, role);

CREATE UNIQUE INDEX IF NOT EXISTS film_work_genre_idx ON content.genre_film_work (film_work_id, genre_id);
