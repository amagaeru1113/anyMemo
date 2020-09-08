# print("c0")
# # import mysql.connector as mydb
# import MySQLdb

print("c1")
# host_name = "sample-db"
# conn = MySQLdb.connect(
#     host="sample-mysql", port=3306, password="", user="root", db="sample-db"
# )
# cur = conn.cursor()

# # cursor = conn.cursor()
# # cursor.execute("CREATE DATABASE test_mysql_database")

# # cursor.close()
# # conn.close()

import mysql.connector as mydb

# コネクションの作成
conn = mydb.connect(
    host="sample-mysql", port="3306", user="root", password="", database="test-db",
)

conn.ping(reconnect=True)
print(conn.is_connected())
