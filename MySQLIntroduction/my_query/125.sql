# 125 特定の条件に合致するデータを更新

# 商品id=3の商品名をSQL入門に変えて


update products set name = 'SQL入門', price = 1000 where id = 3;

select * from products where id = 3;
