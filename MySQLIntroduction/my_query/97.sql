# 97 多対多の結合

/*
商品iD=3に紐づく商品カテゴリ名を全て教えて欲しい

必要な情報は商品iD、商品名、カテゴリ名
*/

select
	p.id 商品ID,
    p.name 商品名,
    c.name カテゴリ名
from 
	products p
inner join
	products_categories pc
    on p.id = pc.product_id
inner join
	categories c
    on pc.category_id = c.id
where
	p.id = 3
;
	