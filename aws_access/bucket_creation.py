import sqlalchemy
import psycopg2
from sqlalchemy import create_engine as ce,text

# def table_creation():
#     a = ce("postgresql://postgres:ravichandra0906@database-1.c1kqzkru0hqs.us-east-1.rds.amazonaws.com:5432/database-1")
#     conn = a.connect()
#     create_table = text("create table log_in_details (customer_id int,name varchar(30),user_name varchar(15),"
#                         "password varchar(15),log_in_time timestamp with time zone default now())")
#     conn.execute(create_table)
#     conn.close()
#     # print(a)
#     return "ok"
#
# print(table_creation())

rds_connection = ce("postgresql://postgres:ravichandra0906@database-1.c1kqzkru0hqs.us-east-1.rds.amazonaws.com:5432/database-1")

print(rds_connection)
