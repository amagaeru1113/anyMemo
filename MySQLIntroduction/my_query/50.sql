# 49 演習 と回答

# 男性ユーザーの一覧を取得して欲しい
# 取得する件数は10件を設定
# 取得する列はid, last_name, gender

select 
	id, last_name, gender 
from 
	users 
where
	gender = 1
limit 10;