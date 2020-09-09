# sqlalchemy -> mysqlに切替が可能

import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

# engine = sqlalchemy.create_engine(
#     "sqlite:///:memory:", echo=True
# )  # メモリ上で作成、echoで処理をログ出力

# engine = sqlalchemy.create_engine("sqlite:///test_sqlite2", echo=True)  # ファイル出力


# https://qiita.com/mink0212/items/d7f31f6e2903c5f0b837
DATABASE = "mysql"
USER = "root"
PASSWORD = ""
HOST = "sample-mysql"
PORT = "3306"
DB_NAME = "test_mysql_database2"

CONNECT_STR = "{}://{}:{}@{}:{}/{}".format(
    DATABASE, USER, PASSWORD, HOST, PORT, DB_NAME
)

# engineを帰ればpostgressとかも使える
engine = sqlalchemy.create_engine(CONNECT_STR, echo=True)  # mysqlに出力


Base = sqlalchemy.ext.declarative.declarative_base()


class Person(Base):  # クラスでテーブルを作る テーブルのオブジェクト1つ
    __tablename__ = "persons"  # 人名が複数入る
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))


Base.metadata.create_all(engine)  # テーブル情報をsqllikeに書き込む

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

# insert
p1 = Person(name="MIKE")
session.add(p1)
p2 = Person(name="Nancy")
session.add(p2)
p3 = Person(name="Jun")
session.add(p3)
session.commit()


# update
p4 = session.query(Person).filter_by(name="MIKE").first()
p4.name = "Michael"
session.add(p4)
session.commit()

# delete
p5 = session.query(Person).filter_by(name="Nancy").first()
session.delete(p5)
session.commit()


persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)
