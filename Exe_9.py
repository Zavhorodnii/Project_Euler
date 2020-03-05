import math
from multiprocessing import Process, Queue


def start():
    q = Queue()
    p_list = list()
    square_list = list()
    while True:
        try:
            var = int(input("Enter value: "))
            p = int(input("Enter value process: "))
            if p < var:
                break
        except Exception:
            pass
    for i in range(math.ceil(math.sqrt(var))):
        square_list.append(i ** 2)
    print(square_list)
    step = len(square_list)
    while True:
        if len(p_list) < p:
            run = p - len(p_list)
            for i in range(run):
                proc = Process(target=calculate, args=(q, step, square_list))
                p_list.append(proc.name)
                proc.start()
                proc.join()

            for i in range(run):
                print("p_list: ", p_list)
                print("len(p_list): {}, i: {}, p_list[len(p_list)-i]: ".format(len(p_list), i))
                p_list[len(p_list)-i-1].join('')
                #p_list[len(p_list)-i-1].join()
            if step == 0:
                break
            step -= 1
            #print("p_list: ", p_list)
            #p_list.pop()

        #print("++ p_list: ", p_list)
        if step == 0:
            break



def calculate(q, step, square_list):
    print("step: {}, square_list:".format(step))
    for i in range(len(square_list)):
        print(i)

    pass


if __name__ == '__main__':
    start()