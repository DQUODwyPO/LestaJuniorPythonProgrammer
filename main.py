from datetime import datetime

def main():
    t1 = datetime.now()
    for i in range(5000000):
        isEven(i)
    print "isEven: ", datetime.now() - t1

    t1 = datetime.now()
    for i in range(5000000):
        isEven2(i)
    print "isEven2: ", datetime.now() - t1

    t1 = datetime.now()
    for i in range(5000000):
        isEven3(i)
    print "isEven3: ", datetime.now() - t1

    t1 = datetime.now()
    for i in range(5000000):
        isEven4(i)
    print "isEven4: ", datetime.now() - t1

    t1 = datetime.now()
    for i in range(5000000):
        isEven5(i)
    print "isEven5: ", datetime.now() - t1


def isEven(value): return value % 2 == 0


def isEven2(value):
    return bin(value)[-1] == '0'


def isEven3(value):
    return not bool(value & 1)


def isEven4(value):
    return value & 1 == 0


def isEven5(value):
    if not isinstance(value, int):
        raise TypeError("Value is not int")
    return value & 1 == 0


if __name__ == "__main__":
    main()
