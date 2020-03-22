

import math
from datetime import datetime



def func():
    m = int(input("Enter value: "))
    time_1 = datetime.now()
    x = 3
    n = 2
    s = sum([c for c in range(1, x + 1)])
    while n <= m:
        n = 2
        print('s = ', s)
        print('n = ', n)
        print('x = ', x)
        for i in range(2, math.ceil(s ** 0.5)):
            print("s = {}, i = {}, n = {}".format(math.ceil(s ** 0.5), i, n))
            if s % i == 0:
                n += 2
        print('proverka n = ', n)
        x += 1
        s += x
        # input()
    print('value: {} \ntime: {}'.format(s-x, datetime.now() - time_1))


if __name__ == '__main__':
    while True:
        func()