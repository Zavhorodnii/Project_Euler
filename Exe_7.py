def start():
    var = int(input("Enter value: "))
    i = 0
    j = 1
    while True:
        j += 1
        if check(j):
            i += 1
            if i == var:
                print("{} = {}".format(var, j))
                return


def check(j):
    for i in range(j):
        try:
            if j % i == 0:
                if i != 1:
                    return False

        except Exception:
            pass
    return True


if __name__ == '__main__':
    start()