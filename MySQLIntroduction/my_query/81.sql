# 80 文字列の演算

# ユーザー一覧を　苗字　+ スペース　+ 名前　+ さんのフォーマットで出力する

select
	id,
    email,
    concat(last_name, ' ', first_name, 'さん')
from
	users
;