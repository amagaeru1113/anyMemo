def bubble_sort(n, ls):
    flag = 1
    while flag:
        flag = 0
        for j in range(len(a)-1, 0, -1):
            print('target ' + str(a[j]), a)
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j] 
                flag = 1

    return a


def bubble_sort_2(n,ls):
    """未ソート部分の先頭から次のソートを行う"""

    flag = 1
    idx = 0 # 未ソート 部分の先頭インデックス
    while flag:
        flag = 0
        for j in range(len(a)-1, idx, -1):
            print('target ' + str(a[j]), a)
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j] 
                flag = 1
        idx += 1

    return a



n = 5
a = [5,3,2,4, 1]


# print(bubble_sort(n, a))
print(bubble_sort_2(n, a))


