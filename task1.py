# coding=utf-8
from datetime import datetime

"""
На основе первой реализации isEven было создано 4 функции.
isEven2 использует бинарное представление числа и сравнивает последнюю цифру с '0'
isEven3 использует побитовое AND с последним цифрой числа, а затем явно преобразует в тип bool
isEven4 использует побитовое AND с последней цифрой числа, а затем сравнивает с 0, вместо преобразования в тип bool
isEven5 в отличие от isEven4 и остальных проверяет входные данные на тип int

Тест скорости на 5000000 числах показал, что быстрее всего работает isEven4:
isEven:  0:00:00.560000
isEven2:  0:00:01.320000
isEven3:  0:00:00.840000
isEven4:  0:00:00.450000
isEven5:  0:00:00.812000
"""

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
