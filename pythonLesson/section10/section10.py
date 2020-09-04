# ----------------------------------
# 113.スタイルルール

# x=1; # セミコロン無くていい

# x = "----------------------------------------------"  # 一行の長さは80文字以下

# def test_func(a,s,d,f,g,h,w,j,t,y,u,i, #改行で揃える
#               adfaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa='test')
#     """
#     see url sdvaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa # urlは超えてもいい

#     """
#     print('test')


# if x and y: # 無駄な丸括弧を付けない
#     print('extits')


# if x:
#     print("exist")  # 空白が4つ入っている -> tabではスペース4つ分で設定すること
#     x = {"test": "sss"} # :の後ろはスペース1つ

# 変数宣言の時はイコールの前後にスペース一つ、関数の変数宣言ではイコールの前後にスペース空けない
# x = 1
# yyyyyy = 1
# zzzzzzzzzzz = 1  # イコールは揃えなくていい

# グローバルでのdefの間は1行、クラス内でのdefの間は一行

# word = 'hello'
# word2 = '!'
# new_word = '{}  aaa {}'.format(word, word2) # 文字列を間に入れるならこっち
# new_word = word + word2 # そのまま直列に繋ぐならこっち

# long_word = ""
# for word in ["aaa", "bbbb", "ccc"]:
#     long_word += word

# シングルとダブルクオートの使い分けは場合による
# print('aaaa')
# print("aaaaa")
# print("aaa'aa") # ダブルクオートが外側にあると中の文字列にシングルクオートがあると推測できる

# if x: print("exit"):の以降が一行であればつなげられるが、二行にした方がわかりやすい

# クラス名 -> キャメルケース ReataurantRobot
# 関数名、ユーザー名 -> スネークケース recommend_restaunrant, your_name

# 何か値を返すことが明白ならgetを関数名に入れない

# グローバル変数は大文字で繋ぐ GLOOBAL_VAR

# ------------------------------------------------------------------------------------------------------
# 114.Pythonの書き方


# for k, v in ranking.items():
#     print(k, v)
# 練習用では変数名一時でも良いが、実際のコードではだめ

# def other_func(f):
#     print(f(10))

# def test_func(x):
#     return x * 2

# lambda x: x + 2

# other_func(test_func)
# other_func(lambda x: x+2)

# y = None
# x = 1 if y else 2 # y=None -> False判定
# print(x)

# ククロージャ
# def base(x):
#     def plus(y):
#         return x + y

#     return plus


# plus = base(10)
# print(plus(10))
# print(plus(30))

# i = 0
# def add_num():
#     def plu(y):
#         return i + y
#     return plus

# i = 10 #クロージャを使う時はグローバル変数を使わない
# plus = add_num()
# print(plus(10))

# ------------------------------------------------------------------------------------------------------
# 115.ドキュメントとpylint

# ドキュメントは英語で

# ファイルの一番最初にファイルでどんなことをしているのかをかく
# 関数の説明 -> docString argsとreturnでかく
# クラスもinitの前にクラスの説明をかく
