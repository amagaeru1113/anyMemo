# 127 行の削除

/*
商品に割り振られている商品カテゴリを使うのをやめるので
商品とカテゴリの紐付きを削除して欲しい

productsとcategoriesを紐づけている、中間テーブルのproduct_categoriesのデータを全て削除

*/

select * from products_categories;

delete from products_categories;

select * from products_categories;
