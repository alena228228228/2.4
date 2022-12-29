#l/usr/bin/env python3
#-*- coding: utf-8 -*-

#Ввести список А из 10 элементов. Определить количество элементов, кратных 3 и индекс
#последнего такого элемента.

import sys

if __name__ == '__main__':
    # Ввести список одной строкой.
    A = list(map(int, input().split()))
    # Проверить количество элементов списка.
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    counter = 0
    last = 0
    for i, x in enumerate(A):
        if x % 3 == 0:
            counter += 1
            last = i
    print("количество элементов, кратных 3:", counter, ", последний элемент:", last)
