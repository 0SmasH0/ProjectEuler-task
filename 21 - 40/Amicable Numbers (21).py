"""
https://projecteuler.net/problem=21
"""

import time

number = int(input('Введите число: '))


def transformation(num: int) -> int:
    suma = 1

    for i in range(2, num // 2 + 1):

        res = num / i
        if res == int(res):
            suma += i

    return suma


def amicable_nums(num: int) -> int:
    lst = []
    res_suma = 0

    for i in range(2, num):
        if i in lst:
            continue

        res_1 = transformation(i)

        res_2 = transformation(res_1)

        res_3 = res_1 + i

        if res_1 + res_2 == res_3 and i != res_1:
            lst.extend([i, res_1])
            res_suma += res_3

    return res_suma


start = time.time()

print(f'Результат: {amicable_nums(number)}')

end = time.time()

print(f'Время выполнения программы: {end - start}')
