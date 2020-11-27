from tools import stop_watch

class Stack(object):
    def __init__(self, MAXLENGTH=10):
        self.MAXLENGTH = MAXLENGTH
        self.S = [0] * self.MAXLENGTH
        self.top = 0

    def _isEmpty(self):
        return len(self.S) == 0
    
    def _isFull(self):
        return self.top >= self.MAXLENGTH - 1

    def _push(self, x):
        if self._isFull():
            print('overflow')
            exit
        self.top += 1
        self.S[self.top] = x

    def _pop(self):
        if self._isEmpty():
            print('underflow')
            exit
        self.top -= 1
        tmp = self.S[self.top+1]
        self.S[self.top+1] = 0
        # return self.S[self.top+1]
        return tmp

def test_1():
    s = Stack()
    print(s.S)

    s._push(1)
    print(s.S)

    s._push(2)
    print(s.S)

    b = s._pop()
    print(b)
    print(s.S)


@stop_watch
def test_2(inputs):
    s = Stack()

    for x in inputs:
        if str(x).isdecimal():
            s._push(x)
        else:
            b = s._pop()
            a = s._pop()

            if x == '+':
                s._push(a+b)
            elif x == '-':
                s._push(a-b)
            elif x == '*':
                s._push(a*b)

    print(s._pop())


inputs = [1, 2, "+", 3, 4, "-", "*"]
_test_2(inputs)
        

