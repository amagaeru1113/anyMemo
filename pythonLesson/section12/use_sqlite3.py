import sqlite3


# conn = sqlite3.connect("test_sqlite.db")  # DB接続
conn = sqlite3.connect(":memory")  # メモリ上で試す場合

curs = conn.cursor()
curs.execute(
    "CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)"
)  # table作成


curs.execute('INSERT INTO persons(name) values("MIKE")')

curs.execute('INSERT INTO persons(name) values("NAncy")')
curs.execute('INSERT INTO persons(name) values("Jun")')

curs.execute('UPDATE persons set name="Michel" WHERE name="MIKE"')

curs.execute('DELETE FROM persons WHERE name = "Michel"')

curs.execute("SELECT * FROM persons")
print(curs.fetchall())

conn.commit()  # DBに書き込む

curs.close()
conn.close()
