# 84 日付と時刻の演算

-- 現在の日付
select current_date();

-- 現在時刻
select current_timestamp();

-- n日後の日付
select current_date() +  interval 3 day;

-- n日前の日付
select current_date() -  interval 3 day;

-- n時間前の時刻
select current_timestamp() - interval 6 hour;

-- 日付や時刻の特定の部分までを取り出す

-- orderテーブルから注文日時が2017年10月nレコード取得
select * from orders where extract(year_month from order_time) = 201710;

-- ordersテーブルから注文日時が2017年のレコードを取得
select * from orders where extract(year from order_time) = 2017;

-- ordersテーブルから注文日時が1月のレコードを取得
select * from orders where extract(month from order_time) = 1;
