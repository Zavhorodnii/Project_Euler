def start():
    s = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    print(s)


if __name__ == '__main__':
    start()
