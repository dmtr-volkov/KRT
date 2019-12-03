import psycopg2, sys
con = None
try:
    con = psycopg2.connect(
        database="postgres",
        user="posgres"
        password="",
        host="127.0.0.1",
        port="5432"
    )

    print("Database opened successfully")

