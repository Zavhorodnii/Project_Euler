from datetime import datetime


def start():
    var = int(input("Enter value: "))
    start_time = datetime.now()
    i = 0
    result = 0
    while True:
        result += i
        if result % 2 != 0:
            i += 1
            continue
        list_answer = list()
        result_1 = int(result/2)
        for j in range(result_1+1):
            try:
                if result % j == 0:
                    list_answer.append(j)
            except Exception as exe:
                pass
        # print("\nres = ", result)
        # print("result_1 = ", result_1)
        # print("var = ", var)
        print("i: {} result: {} len: {} list: {}".format(i, result, len(list_answer), list_answer))
        if len(list_answer) >= var-1:
            list_answer.append(result)
            print("i: {} result: {} len: {} \ntime: {}".format(i, result, len(list_answer),
                                                               datetime.now() - start_time))
            break
        i += 1





if __name__ == '__main__':
    start()
