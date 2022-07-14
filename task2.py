# coding=utf-8
from datetime import datetime


"""
В задании сказано реализовать циклический буфер FIFO, что подразумевается как фиксированный кольцевой буфер
со способом организации FIFO.
"""


def main():
    fifo1 = FIFO1(5, int)
    fifo2 = FIFO2(7, "asdf")
    for i in range(24):
        fifo1.put(i)
        fifo2.put(i)
    print "FIFO1: ", fifo1
    print "FIFO2: ", fifo2
    print repr(fifo1)
    print repr(fifo2)

    print "-" * 50
    for _ in range(3):
        print "FIFO1: ", fifo1.get()
        print "FIFO2: ", fifo2.get()
    print "FIFO1: ", fifo1
    print "FIFO2: ", fifo2

    print "-" * 50
    try:
        fifo1.put("4")
    except TypeError:
        print "Вызвана ошибка TypeError (FIFO1)"
    try:
        fifo2.put("4")
    except TypeError:
        print "Вызвана ошибка TypeError (FIFO2)"

    print "-" * 50
    for _ in range(10):
        fifo1.get()
        fifo2.get()
    print "FIFO1: ", fifo1
    print "FIFO2: ", fifo2

    print "-" * 50
    fifo1.put(1)
    fifo2.put(1)
    print "FIFO1: ", fifo1
    print "FIFO2: ", fifo2

    print "-" * 50
    t1 = datetime.now()
    fif1 = FIFO1(10000, int)
    for i in range(1500000):
        fif1.put(i)
    for i in range(3000):
        fif1.get()
    t2 = datetime.now() - t1

    t1_2 = datetime.now()
    fif2 = FIFO2(10000, int)
    for i in range(1500000):
        fif2.put(i)
    for i in range(3000):
        fif2.get()
    t2_2 = datetime.now() - t1_2

    print "FIFO1: ", t2
    print "FIFO2: ", t2_2

    """
    Показатели колеблются в пределах погрешности и фактически равны.
    Примеры:
    FIFO1:  0:00:00.820000
    FIFO2:  0:00:00.890000
    FIFO1:  0:00:00.830000
    FIFO2:  0:00:00.860000
    FIFO1:  0:00:00.870000
    FIFO2:  0:00:00.850000
    FIFO1:  0:00:00.860000
    FIFO2:  0:00:00.860000
    """


class FIFO1:
    """
    Первая реализация использует список размера size (мин. 10) задаваемого пользователем типа (по умолчанию int).
    Элементы списка заполняются None. При заполнении списка, идет заполнение с его начала (при этом может сдвигаться индекс
    первого элемента, что проверяется через булевую переменную circle)
    """
    def __init__(self, size=10, type_=int):
        if type_ not in (int, float, str, list, dict, tuple, set):
            type_ = int
        self.__type = type_
        if size < 10:
            size = 10
        self.__size = size
        self.__line = [None for _ in range(size)]
        self.__idx = 0
        self.__first = 0
        self.__circle = False

    def put(self, elem):
        if not self.__type is type(elem):
            raise TypeError("Type of query is not equal")

        if self.__idx == self.__size:
            self.__circle = True
            self.__idx = 0
        if self.__circle and self.__idx == self.__first:
            self.__first = (self.__first + 1) % self.__size

        self.__line[self.__idx] = elem
        self.__idx += 1

    def get(self):
        if self.__line[self.__first] is None:
            return None
        ret = self.__line[self.__first]
        self.__line[self.__first] = None
        self.__first += 1
        if self.__first == self.__size:
            self.__circle = False
            self.__first = 0
        return ret

    def __str__(self):
        return str([elem for elem in self.__line])

    def __repr__(self):
        return "FIFO1({0}, {1})".format(self.__size, self.__type.__name__)


class Node:

    def __init__(self, value_, next_):
        self.__value = value_
        self.__next = next_

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __str__(self):
        return "{0}".format(self.__value)


class FIFO2:
    """
        Вторая реализация использует зацикленный список размера size (мин. 10), использующий класс Node в качестве
        элемента списка. Тип значение элемента задавается пользователем (по умолчанию int).
        Создается size элементов класса Node, где каждый указывает на следующий, а последний на начало.

        В отличие от первой реализации, вывод списка всегда начинается с первого элемента очереди.
        Также здесь использовано меньше переменных (отсутствует size, circle), так как нет вычислений
        с индексом (хоть они так и называются). Проверка того, что idx и first указывают на один и тот же
        Node происходит через id.
    """
    def __init__(self, size, type_=int):
        if type_ not in (int, float, str, list, dict, tuple, set):
            type_ = int
        self.__type = type_

        if size < 10:
            size = 10
        self.__idx = Node(None, None)
        self.__first = self.__idx
        cur = self.__idx
        for _ in range(size - 1):
            new = Node(None, None)
            cur.next = new
            cur = new
        cur.next = self.__idx

    def put(self, elem):
        if not self.__type is type(elem):
            raise TypeError("Type of query is not equal")

        if id(self.__idx) == id(self.__first) and self.__idx.value is not None:
            self.__first = self.__first.next
        self.__idx.value = elem
        self.__idx = self.__idx.next

    def get(self):
        if self.__first.value is None:
            return None
        ret = self.__first.value
        self.__first.value = None
        self.__first = self.__first.next
        return ret

    def __str__(self):
        cur = self.__first
        l = [cur.value]
        cur = cur.next
        while id(cur) != id(self.__first):
            l.append(cur.value)
            cur = cur.next
        return "{0}".format(l)

    def __repr__(self):
        cur = self.__first
        cur = cur.next
        num = 1
        while id(cur) != id(self.__first):
            num += 1
            cur = cur.next
        return "FIFO2({0}, {1})".format(num, self.__type.__name__)

if __name__ == "__main__":
    main()
