from datetime import datetime


def start():
    var = int(input("Enter value: "))
    time = datetime.now()
    my_list = [2, ]
    j = 2
    result = 2
    while True:
        if go(j, my_list):
            result += j
            my_list.append(j)
        if j == var:
            print("{}".format(result))
            print("time: {}".format(datetime.now()-time))
            return
        j += 1


def go(j, my_list):
    #print(my_list)
    for i in my_list:
        if j % i == 0:
            #print(j)
            return False
    return True



if __name__ == '__main__':
    start()