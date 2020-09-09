import MySQLdb  # mac用

# ---------
# 接続
# host="sample-mysql",
# port="3306", user="root", password="", database="test-db",
# ---------
# cnct = pymysql.connect( #Raspberry Pi用
cnct = MySQLdb.connect(  # Win,mac用
    host="sample-mysql",  # ホスト名
    user="root",  # MySQLユーザ名
    password="",  # MySQLユーザパスワード
    db="test-db",  # データベース名
    charset="utf8",  # 文字コード
)

cur = cnct.cursor()

# Table作成
cur.execute(
    "CREATE TABLE persons (id int NOT NULL AUTO_INCREMENT,name varchar(14) NOT NULL,PRIMARY KEY(id))"
)

# log
# MySQL [test-db]> show create table persons;
# +---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
# | Table   | Create Table                                                                                                                                                |
# +---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
# | persons | CREATE TABLE `persons` (
#   `id` int(11) NOT NULL AUTO_INCREMENT,
#   `name` varchar(14) NOT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
# +---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
# 1 row in set (0.000 sec)


# INSERT
cur.execute("INSERT INTO persons(name) values('MIKE')")
cnct.commit()

cur.execute("SELECT * FROM persons")
for row in cur:
    print(row)  # (1, 'MIKE')

cur.close()
cnct.close()
