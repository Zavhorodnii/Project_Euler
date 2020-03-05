from datetime import datetime


def start():
    var = int(input("Enter value: "))
    time = datetime.now()
    point_1 = int(var/2)
    while True:
        point_2 = point_1 - 1
        while True:
            point_3 = var - (point_2 + point_1)
            if point_3**2 + point_2**2 == point_1**2:
                print("{} + {} = {}".format(point_3, point_2, point_1))
                print(point_3 * point_2 * point_1)
                print("time: ", datetime.now()-time)
                return
            if point_2 == 1:
                break
            point_2 -= 1
        if point_1 == 2:
            break
        point_1 -= 1


if __name__ == '__main__':
    start()