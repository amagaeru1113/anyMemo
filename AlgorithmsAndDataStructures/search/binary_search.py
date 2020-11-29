import random
from typing import List

from tools import stop_watch

@stop_watch
def test_1(inputs1: List, inputs2: List) -> int:
    """二重ループで合致するか判定"""
    count = 0
    for i in inputs1:
        for j in inputs2:
            if i == j:
                count += 1
    return count

@stop_watch
def test_2(inputs1: List, inputs2: List) -> int:
    """リストに含まれるか判定"""
    count = 0
    for i in inputs2:
        if i in inputs1:
            count += 1
    return count

@stop_watch
def test_3(inputs1: List, inputs2: List) -> int:
    """番兵法:リストの最後に指定した値をおき、これに到達したら見つからなかったと判定"""
    count = 0
    n = len(inputs1)

    for j in inputs2:
        i = 0
        a = inputs1.copy()
        a.append(j)
        while inputs1[i] != j:
            i += 1
        if i == n + 1:
            return 0
        # print(i)
        count += 1
    return count
        
inputs1 = list(range(50))
inputs2 = random.choices(inputs1, k=20)

test_1(inputs1, inputs2)
test_2(inputs1, inputs2)
test_3(inputs1, inputs2)


