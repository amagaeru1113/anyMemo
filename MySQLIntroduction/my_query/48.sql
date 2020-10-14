# 48 取得件数を制限するlimit

# 商品一覧を最大10券表示して欲しい
select * from products limit 10; 

# 商品一覧を最大10券表示して欲しい
select * from products limit 0, 10;# 0から10券取得する 
select * from products limit 10, 10;# 10から10券取得する 