
def start():
    var = int(input("Enter value: "))
    point_1 = var
    while True:
        point_2 = point_1 - 1
        while True:
            point_3 = point_2 - 1
            while True:
                if point_3 + point_2 + point_1 == var:
                    if point_3**2 + point_2**2 == point_1**2:
                        print(point_3 * point_2 * point_1)
                        return
                if point_3 == 0:
                    break
                point_3 -= 1
            if point_2 == 1:
                break
            point_2 -= 1

        if point_1 == 2:
            break
        point_1 -= 1


if __name__ == '__main__':
    start()