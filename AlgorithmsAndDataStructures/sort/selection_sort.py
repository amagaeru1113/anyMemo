# 各計算ステップで1つの最小値を選択していく

def selection_sort(lst):
    n = len(lst)
    for i in range(n-1):
        minj = i
        for j in range(i+1, n):
            if lst[j] < lst[minj]:
                minj = j
        lst[i], lst[minj] = lst[minj], lst[i]

        print(lst)
    return lst

lst = [5,4,8,7,9,3,1]

print(selection_sort(lst))
