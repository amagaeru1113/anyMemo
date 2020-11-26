# def insert_sort(n, ls):
#     pass



n = 6
a = [5,2,4,6,1,3] 


print(a)

for i in range(1, len(a)):
    v = a[i]
    j = i - 1

    while j >= 0 and  a[j] > v:# jが正かるそれまでの要素が今の値を超えていなければ続ける
        a[j+1] = a[j]
        j -= 1
    
    a[j+1] = v

    print(a)