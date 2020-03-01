def start():
    i = 2
    summ = 2
    my_list = [1, 2]
    while True:
        s = my_list[0] + my_list[1]
        if s % 2 == 0:
            if summ + s > 4000000:
                break
            summ += s
        my_list.insert(0, my_list[1])
        my_list.insert(1, s)
        i += 1

    print("summ ",summ)


if __name__ == '__main__':
    start()
