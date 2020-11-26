def selection_sort(lst):
    n = len(lst)
    for i in range(n-1):
        minj = i
        for j in range(i+1, n):
            if lst[j][1] < lst[minj][1]:
                minj = j
        lst[i], lst[minj] = lst[minj], lst[i]

        # print(lst)
    return lst

def bubble_sort_2(lst):
    """未ソート部分の先頭から次のソートを行う"""
    n = len(lst)
    flag = lst
    idx = 0 # 未ソート 部分の先頭インデックス
    while flag:
        flag = 0
        for j in range(n-1, idx, -1):
            # print('target ' + str(lst[j]), lst)
            if lst[j][1] < lst[j-1][1]:
                tmp = lst[j] 
                lst[j] = lst[j-1]
                lst[j-1] = tmp
                flag = 1
        idx += 1

    return lst

lst = ['H4','C9','S4', 'D2', 'C3']

print(bubble_sort_2(lst))
print(selection_sort(lst))