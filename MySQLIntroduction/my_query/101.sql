# 101 ビューの作成

# 都道府県別のユーザー数を出力する
/*
create view prefecture_user_counts(name, count)
as
select
	p.name name,
    count(*) count
from
	users u
inner join
	prefectures p
    on u.prefecture_id = p.id
group by
	u.prefecture_id
;
*/

select 
	name,
    count
from
	prefecture_user_counts
;