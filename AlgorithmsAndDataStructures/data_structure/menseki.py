# https://mtdtx9.hatenablog.com/entry/2017/04/24/230941

from tools import stop_watch

def test_1(intputs):

    S1, S2 = [], []
    area = 0

    for i,v in enumerate(inputs):
        # print(i,v)

        if v == '\\':
            S1.append(i)
        
        if v == '/' and S1:
            i_p = S1.pop()
            a = i - i_p
            area += a
            while S2 and S2[-1][0] > i_p:
                a += S2.pop()[1]
            S2.append([i_p, a])

    print(sum([i[1] for i in S2]))
    print(len(S2), *(a for i, a in S2))


inputs = '\\\\//'
test_1(inputs)



