# 119 都道府県別月別平均客単価

# 118 都道府県別平均客単価

select
	u.prefecture_id 都道府県ID,
    p.name 都道府県名,
    date_format(order_time, '%Y%m') 年月,
    round(avg(amount), 0) 都道府県別月別平均客単価
from
	orders o
inner join
	users u
    on u.id = o.user_id
inner join
	prefectures p
	on u.prefecture_id = p.id 
group by
	u.prefecture_id asc,
    date_format(order_time, '%Y%m') asc
order by
	p.id asc
;