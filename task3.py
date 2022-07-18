# coding=utf-8
from time import time
from random import randint

"""
Необходимо реализовать функцию, которая быстрее всего (по процессорным тикам) отсортирует массив.
В таком случае принято решение реализовать алгоритм 'быстрой сортировки'.
"""


def main():
    l = [randint(1, 10**9) for _ in range(1000000)]
    l2 = l[:]
    my_arr = MyArray(l2)

    t1 = time()
    l.sort()
    t2 = time() - t1
    print "Python sort:", t2

    t3 = time()
    my_arr.quick_sort(0, my_arr.__len__() - 1)
    t4 = time() - t3
    print "My sort:", t4

    """
    Python sort: 0.579999923706
    My sort: 5.3140001297
    Получили разницу на один порядок, что вероятно связано с реализацией Python sort (C).
    """


class MyArray:

    """
    Класс создан из удобства, чтобы не создавать лишние переменные и работать над одной переменной.
    Так как оценивается по "процессорным тикам", было решено не добавлять параллельные вычисления.
    """

    def __init__(self, data):
        self.__array = data
        self.__len = len(data)

    def swap(self, a, b):
        temp = self.__array[a]
        self.__array[a] = self.__array[b]
        self.__array[b] = temp

    def partition(self, start, end):
        q = (start + end) // 2
        t = self.__array[q]
        while start <= end:
            while self.__array[start] < t:
                start += 1
            while self.__array[end] > t:
                end -= 1
            if start >= end:
                break
            self.swap(start, end)
            start += 1
            end -= 1
        return end

    def quick_sort(self, start, end):
        if start < end:
            q = self.partition(start, end)
            self.quick_sort(start, q)
            self.quick_sort(q + 1, end)

    def __len__(self):
        return self.__len

    def __str__(self):
        return self.__array


if __name__ == "__main__":
    main()
