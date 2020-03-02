import math
from datetime import datetime
from multiprocessing import Process, Queue
from threading import Thread


def start():
    q = Queue()
    var = int(input("Enter value: "))
    time_1 = datetime.now()
    if var != 1:
        var_del = math.ceil(var/2)
        p_1 = Process(target=sum_of_squares, args=(q, var_del, var,))
        p_2 = Process(target=squared_amount, args=(q, var_del, var,))
        p_1.start()
        p_2.start()
        p_1.join()
        p_2.join()

        result_1 = q.get()
        result_2 = q.get()
    else:
        result_1 = 1
        result_2 = 1
    if result_1 > result_2:
        print("{} - {} = {}\nTime: {}".format(result_1, result_2, result_1-result_2, datetime.now() - time_1))
    else:
        print("{} - {} = {}\nTime: {}".format(result_2, result_1, result_2-result_1, datetime.now() - time_1))

    pass


def sum_of_squares(q, var_del, var):
    qu = Queue()
    thread_1 = Thread(target=from_sum_of_squares, args=(qu, 0, var_del, ))
    thread_2 = Thread(target=from_sum_of_squares, args=(qu, var_del, var, ))
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()
    result = qu.get()
    result += qu.get()
    q.put(result)


def from_sum_of_squares(qu, min, max):
    min += 1
    max += 1
    result = 0
    for i in range(max - min):
        result += min ** 2
        min += 1
    qu.put(result)


def squared_amount(q, var_del, var):
    qu = Queue()
    thread_1 = Thread(target=from_squared_amount, args=(qu, 0, var_del, ))
    thread_2 = Thread(target=from_squared_amount, args=(qu, var_del, var, ))
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()
    result = qu.get()
    result += qu.get()
    q.put(result ** 2)


def from_squared_amount(qu, min, max):
    min += 1
    max += 1
    result = 0
    for i in range(max - min):
        result += min
        min += 1
    qu.put(result)



if __name__ == '__main__':
    start()