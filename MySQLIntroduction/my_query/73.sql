# 73 演習

# ユーザー一覧を出力
# 生年月日が古い順に並べる
# 生年月日が一緒の場合には、都道府県順（昇順）に並べる

select
	*
from
	users
order by
	birthday asc,
    prefecture_id asc
;	