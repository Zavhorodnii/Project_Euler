import math
from subprocess import Popen, PIPE
from multiprocessing import Process, Queue

allProcesses = list()


def run(long, max, min, q, bool):
    while max >= min:
        try:
            if long % max == 0:
                if bool and max != 1:
                    print(max)
                    write = run(max, max-1, min, q, False)
                if not bool:
                    if max == 1:
                        return True
                    else:
                        return False
                if write:
                    q.put(max)
                    break
        except Exception:
            pass
        max -= 1
    if not bool:
        print("long = ", long)
        return True


def start():
    q = Queue()
    result = list()
    while True:
        try:
            long_var = int(input("Enter value: "))
            thread_var = int(input("Enter thread count: "))
            if thread_var > long_var or long_var < 2 or thread_var < 2:
                print("Error")
            else:
                break
        except Exception:
            pass
    var_1 = math.ceil(long_var / thread_var)
    var_2 = 1
    while True:
        if var_2 + var_1 >= long_var:
            create(long_var, long_var-1, var_2, q)
            break
        else:
            var_2 += var_1
            create(long_var, var_2, (var_2 - var_1), q)
            var_2 += 1


    for p in allProcesses:
        p.join()

    result.append(1)
    for i in range(q.qsize()):
        result.append(q.get())

    print("result: ", result)
    print("max: ", max(result))
    print("max_var: ", long_var % max(result))


def create(long, max, min, q):
    p = Process(target=run, args=(long, max, min, q, True))
    allProcesses.append(p)
    p.start()
    return p


if __name__ == '__main__':
    start()