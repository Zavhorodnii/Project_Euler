

def start():
    var = int(input("Enter var: "))
    i = 0
    while True:
        i += 1
        for j in range(var):
            j += 1
            if i % j != 0:
                break
            elif j == var:
                print(i)
                return




if __name__ == '__main__':
    start()