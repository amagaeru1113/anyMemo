# 94 外部結合

 -- usersテーブルとordersテーブルを結合
 
 select
	u.last_name,
    u.id,
    o.user_id,
    o.id
from
	users u
-- inner join
left outer join -- u.idの2,3などが出力される
	orders o
	on u.id = o.user_id
order by
	u.id
;