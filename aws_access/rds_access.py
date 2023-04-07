import psycopg2
from sqlalchemy import create_engine as ce
import os

# rds_connection = ce("postgresql://postgres:Tweak#123@tweaktalent.cpojujlhrdvz.us-east-2.rds.amazonaws.com:5432/database-1")
#
# print(rds_connection)
conn = psycopg2.connect(
    host="tweaktalent.cpojujlhrdvz.us-east-2.rds.amazonaws.com",
    port=5432,
    dbname="postgres",
    user="postgres",
    password="Tweak#123")


# conn = psycopg2.connect(
#     dbname=os.environ.get("POSTGRES_DB"),
#     user=os.environ.get("POSTGRES_USER"),
#     password=os.environ.get("POSTGRES_PASS"),
#     host=os.environ.get("POSTGRES_HOST"),
#     port=os.environ.get("POSTGRES_PORT")
# )

with conn.cursor() as cursor:
    cursor.execute('SELECT VERSION()')
    print(cursor.fetchone())
    print("connected")
    # rds_connection.close()

