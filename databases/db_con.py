# connect to databases

# connect to mssql
# apt-get install -y libltdl7 libkrb5-3 libgssapi-krb5-2
pip install mssql-python
# pip install pyodbc


from mssql_python import connect

conn_str = "Server=<your_server_name>,<port>;Database=<your_db_name>;Trusted_Connection=yes;"
conn = connect(conn_str)

cursor = conn.cursor()
cursor.execute("SELECT * FROM T1")
rows = cursor.fetchall()
from mssql_python import connect

# with connect(connection_string) as conn:
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
#     # If no exception → commit happens automatically
#     # If exception → rollback happens automatically
# # Connection is closed automatically here


# import pyodbc
# # Connection string
# server = 'your_server_name'
# database = 'your_database_name'
# username = 'your_username'
# password = 'your_password'
# conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# # Establish the connection
# conn = pyodbc.connect(conn_str)


# import pymssql
# # Connect to the database
# conn = pymssql.connect(server='your_server_name',
#                        user='your_username',
#                        password='your_password',
#                        database='your_database_name')

# # for both
# cursor = conn.cursor()
# query = "SELECT * FROM your_table_name"
# cursor.execute(query)