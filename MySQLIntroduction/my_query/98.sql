# 98 テーブルの足し算

/*
ユーザーとアドミンユーザーを足し合わせたいちらんが欲しい

出力して欲しいのは
	email
	名字
    名前
    性別
*/

select
	email,
    last_name,
    first_name,
    gender
from
	users
where gender = 1

union
-- union all 重複行を削除しない場合

select
	email,
    last_name,
    first_name,
    gender
from
	admin_users
where gender = 2
order by -- unionでは最後につける
	gender


;