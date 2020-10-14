# 71 複数条件で並び替え

# 商品一覧は高い順、　価格が同じ時は登録順で並び替えして表示
# 登録順はproduct.idが小さい準

select
	*
from
	products
order by
	price desc,
    id asc
;