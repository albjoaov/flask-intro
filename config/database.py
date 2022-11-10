import psycopg2

connection = psycopg2.connect(dbname="sandbox", user="postgres", password="postgres", host="localhost")
cursor = connection.cursor()
