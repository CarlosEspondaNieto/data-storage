import psycopg2
#connect to an existing database
conn = psycopg2.connect("dbname=beeva_test user=administradorcito password=beeva2014 port=5432")
#open a cursor to perform database operations
cur = conn.cursor()

#Execute a command: this creates a new table
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

#pass data to fill a query placeholders and let Psycopg perform
#the correct conversion (no more SQL injections)
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",
 (100, "abc'def")) 

#Query the database and obtain data as python objects
cur.execute("SELECT * FROM  test;")
cur.fetchone()
(1,100, "abc'def")

#Make the changes to the database persistent
conn.commit();

#Close.comunications with the database
cur.close()
conn.close()
