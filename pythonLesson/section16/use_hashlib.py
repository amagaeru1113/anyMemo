import base64
import os
import hashlib


# 事例
# - ユーザーのログイン時のパスワード一致判定
# - ファイル内容の一致判定

# print(hashlib.sha256(b"password").hexdigest())  # 表示された内容のみから復元することはできない


user_name = "user1"
user_pass = "password"
db = {}

# base64を使って単純なハッシュ化を複雑にすることで突破を防ぐ
salt = base64.b64encode(os.urandom(32))


def get_digest(password):
    password = bytes(password, "utf-8")
    digest = hashlib.sha256(salt + password).hexdigest()

    # ストレッチ：複数回ハッシュ化を行い、辿れなくする
    for _ in range(100):
        digest = hashlib.sha256(bytes(digest, "utf-8")).hexdigest()

    print(digest)
    return digest


db[user_name] = get_digest(user_pass)


# 上記のストレッチ＋saltを行う関数
# digest = hashlib.pbkdf2_hmac("sha256", byte(user_pass, "utf-8"), salt, 100)
# db[user_name] = digest
# print(db)


def is_login(user_name, passowrd):
    return get_digest(passowrd) == db[user_name]


print(is_login(user_name, user_pass))

