# 129 条件を指定して行を削除

# 商品ID 1001は間違えて登録したため削除して

select * from products;

delete from products where id = 1001;

select * from products;
