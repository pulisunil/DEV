#Connecting to oracle  data base
#pip install cx_Oracle
import cx_Oracle
from cx_Oracle import DatabaseError

#variables

host='localhost'
port=1521   #default port
service_name='orcl'    #default orcl
user='source'
password='1234'

#db_query
# query="select * from emp"

#db Connection
dsn_tns = cx_Oracle.makedsn(host,port, service_name=service_name)
oracle_conn = cx_Oracle.connect(user=user, password=password, dsn=dsn_tns)
print("cx_Oracle version:", cx_Oracle.version)
print("Database version:", oracle_conn.version)
print("Client version:", cx_Oracle.clientversion())
oracle_cursor = oracle_conn.cursor()
oracle_cursor.execute("select * from emp")  # To execute the query
oracle_cursor.fetchall()
oracle_cursor.fetchone()   #TO Fetch the result  example: result=oracle_cursor.fetchall()



# db to csv
# import pandas as pd
#
# oracle_cursor = oracle_conn.cursor()
# oracle_cursor.execute(query)  # To execute the query
# result=oracle_cursor.fetchall()
# df = pd.DataFrame(result)
# df.to_csv(r'D:/employees.csv',index=False)

# sql_query = pd.read_sql_query('select * from employees',conn)
# df = pd.DataFrame(sql_query)
# df.to_csv(r'D:/employees.csv',index=False)

# oracle_cursor.close()
oracle_conn.close()













