# Data Modeling with PostgreSQL - Discussion

## Project files and instructions

### Get started

To get started, first run create_tables.py with one of
        python create_tables.py
        !python create_tables.py

This will create the tables so data can be added to them.

Next, run etl.py to load the data into the tables. If you want to do this more interactively, you might want to check out etl.ipynb, which uses a very small subset of the data.

Finally, check out the tables with the data loaded by running test.ipynb. Please make sure to restart or shutdown the kernel for this notebook afterwards to close the database connection, otherwise you might encounter errors when trying to run other scripts.

### Example queries

Two example queries are given in the script sql_queries.py.

##    Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.

The music streaming startup Sparkify would like to analyze the data they have collected about songs and user activity through their music streaming app. The log files and song metadata are given in JSON format.

The analytics team is interested in understanding which songs users are listening to the most. They wanted me as a data engineer to create a Postgres database designed to optimize their song play analysis queries. This will help the analytics team with their goal to get the most popular songs as well as aid Sparkify to get licenses for more songs by the most popular artists.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

##    State and justify your database schema design and ETL pipeline.

For this database, I have chosen a star schema with a central fact table, songplays, which contains the central information about a song being played. This table is surrounded by the dimension tables songs, artists, users, and time, which contain additional information related to that contained in the songplays table. The central songplays tables relates to all these dimension tables through foreign keys.

For the ETL pipeline (ETL = Extract, Transform, Load), I have chosen to work with a Python wrapper library for SQL queries, psycopg2. This allows for more abstraction including loops and function abstraction in order to have more concise and clean code.
After the initial table creation with create_tables.py the data is extracted from the JSON log and song data files, and loaded into the tables. The Jupyter notebook test.ipynb allows for me to quickly verify the correct execution, and for the analytics team to get a first glance at the tables and the data they contain.
