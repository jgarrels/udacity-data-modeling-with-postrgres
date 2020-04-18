# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

# query to create the central table 'songplays'
# table will reference column X of the same name in table Y:
#   start_time in time
#   user_id in users
#   song_id in songs
#   artist_id in artists
songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays 
                            (songplay_id bigserial PRIMARY KEY, 
                            start_time timestamp NOT NULL REFERENCES time (start_time), 
                            user_id text NOT NULL REFERENCES users (user_id), 
                            level text NOT NULL, 
                            song_id text REFERENCES songs (song_id), 
                            artist_id text REFERENCES artists (artist_id), 
                            session_id int NOT NULL, 
                            location text, 
                            user_agent text);""")

# query to create the table 'users'
user_table_create = ("""CREATE TABLE IF NOT EXISTS users 
                            (user_id text PRIMARY KEY, 
                            first_name text, 
                            last_name text, 
                            gender text, 
                            level text NOT NULL);""")

# query to create the table 'songs'
# column 'artist_id' will reference the column of the same name in the 'artists' table
song_table_create = ("""CREATE TABLE IF NOT EXISTS songs 
                            (song_id text PRIMARY KEY, 
                            title text NOT NULL, 
                            artist_id text NOT NULL REFERENCES artists (artist_id), 
                            year int, 
                            duration decimal);""")

# query to create the table 'artists'
artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists 
                            (artist_id text PRIMARY KEY, 
                            name text NOT NULL, 
                            location text, 
                            latitude decimal, 
                            longitude decimal 
                            );""")
### CHECK ((latitude BETWEEN -90 AND 90) OR (latitude = NaN)),
### CHECK (longitude BETWEEN -180 AND 180)
# query to create the table 'time'
time_table_create = ("""CREATE TABLE IF NOT EXISTS time 
                            (start_time timestamp PRIMARY KEY,  
                            hour int, 
                            CHECK (hour BETWEEN 0 AND 23), 
                            day int, 
                            CHECK (day BETWEEN 1 AND 31), 
                            week int, 
                            CHECK (week BETWEEN 1 AND 53), 
                            month int, 
                            CHECK (month BETWEEN 1 AND 12), 
                            year int, 
                            weekday int,
                            CHECK (weekday BETWEEN 0 AND 6));""")

# INSERT RECORDS

# auto-insert a unique bigserial songplay_id by omitting it from the INSERT statement
songplay_table_insert = ("""INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (user_id) DO 
                        UPDATE SET (first_name, last_name, gender, level) = 
                        (EXCLUDED.first_name, EXCLUDED.last_name, EXCLUDED.gender, EXCLUDED.level);""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (song_id) DO NOTHING;""")

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (artist_id) DO NOTHING;""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (start_time) DO NOTHING;""")

# FIND SONGS

song_select = ("""SELECT s.song_id, s.artist_id
                    FROM songs s
                    JOIN artists a
                    ON s.artist_id = a.artist_id
                    WHERE s.title = %s AND a.name = %s AND s.duration = %s;""")

# Find a user through their first and last name
# returns a table with their id, first and last name, and level
user_play_select = ("""SELECT user_id, first_name, last_name, level
                        FROM users
                        WHERE first_name = %s AND last_name = %s""")

# QUERY LISTS

# changed order of queries to allow for REFERENCES: tables that reference other tables will be created last
create_table_queries = [time_table_create, artist_table_create, user_table_create, song_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, song_table_drop, user_table_drop, artist_table_drop, time_table_drop]