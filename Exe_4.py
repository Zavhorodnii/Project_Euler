
dict_pal = dict()


def start():
    var_1 = int(input("Enter value 1: "))
    var_2 = int(input("Enter value 2: "))
    step = int(input("Enter step: "))
    i = 1
    while True:
        for askew in range(step * i):
            for move in range(step):
                a = (var_1 - move) * (var_2 - askew)
                if check(str(a)):
                    dict_pal[a] = "{} * {}".format((var_1 - move), (var_2 - askew))
                if a == 1:
                    print("Palindrome not found")
                    return
        var_1 -= step
        i += 1
        if len(dict_pal) > 0:
            var_1 = max(dict_pal.keys())
            print(dict_pal[var_1], " = ", var_1)
            return


def check(var):
    pal = True
    for j in range(len(var) // 2):
        if var[j] != var[-1 - j]:
            pal = False
    return pal


if __name__ == '__main__':
    start()