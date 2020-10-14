# 46 比較演算しの種類

-- proructsテーブルから全券取得 
select * from products;


-- id が1の行を取得 
select * from products where id = 1;

-- 名前が「商品0003」の行を取得 
select * from products where name = "商品0003";

-- priceが1000より大きい行を取得 
select * from products where price > 1000;

-- priceが1000より小さい行を取得 
select * from products where price < 1000;

-- priceが100出ない行を取得1 
select * from products where price <> 100;

-- priceが100出ない行を取得2
select * from products where price != 100;

-- idが1or2or3行を取得 
select * from products where id in (1,2,3);

-- idが1or2or3出ない行を取得 
select * from products where id not in (1,2,3);

-- priceがnullない行を取得 
select * from products where price is not null;
 
-- priceがnullの行を取得 
select * from products where price is null;

-- priceが1000から1900の行を取得 
select * from products where price BETWEEN 1000 AND 1900;
select * from products where price >= 1000 AND price <= 1900;
select * from products where price >= 1000 AND price <= 1900;

-- priceが1000または2000の行を取得 
select * from products where price = 1000 or price = 2000;
