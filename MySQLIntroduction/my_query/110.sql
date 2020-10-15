# 109 条件分岐

/*
- ユーザーのアクティビティ度合いによって施策を変えたい

- ユーザーの累計注文回数でランクわけ
	- A: 5回以上
    - B: 2回以上
    - C: 1回
    注文回数0回は出力不要

- 必要情報
	- ユーザーid
    - 累計注文回数
    - ユーザーランク
*/

select
	u.id user_id,
    count(*) order_num,
    case
		when count(*) >= 5 then 'A'
        when count(*) >= 2 then 'B'
        else 'C'
    end user_rank
from 
	users u
inner join
	orders o
	on u.id = o.user_id
group by
	u.id
order by
	user_rank asc
;