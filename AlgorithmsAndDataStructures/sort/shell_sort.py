import random

from tools import stop_watch

# 通常のインサートソートでは間隔g=1と考え、シェルソートではこの間隔gが可変になる
def _insert_sort(lst, g):
    n = len(lst)
    sorted_list = list(lst)
    for i in range(g, n):
        v = lst[i]
        j = i - g # 間隔g

        while j >= 0 and  sorted_list[j] > v:# jが正かるそれまでの要素が今の値を超えていなければ続ける
            sorted_list[j+g] = sorted_list[j]
            j -= g 
        
        sorted_list[j+g] = v

    return sorted_list

@stop_watch
def _shell_sort(lst):
    n = len(lst)
    h = 1 # h-sort 
    G = []

    # Gの選び方は g_{n+1} = 3g_{n}+1が良いとされているらしい
    while h <= len(lst):
        G.append(h)
        h = 3*h+1
    G.reverse()

    for g in G:
        sorted_list = _insert_sort(lst, g)
    # print(sorted_list)
    return sorted_list




lst = list(range(100))
goal = list(range(100))
random.shuffle(lst)

sorted_lst = _shell_sort(lst)
print(sorted_lst == goal)
# print(sorted_lst)