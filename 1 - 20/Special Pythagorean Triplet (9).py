"""
https://projecteuler.net/problem=9
"""

import time

number = 1000


def spt_algo(num: int) -> int | str:
    for a in range(100, num):

        b = (num * (500 - a)) // (num - a)

        if a < b:
            c = num - a - b
            if b < c and a ** 2 + b ** 2 == c ** 2:
                return a * b * c

    return 'Нет таких чисел'


start = time.time()

print(f'Результат: {spt_algo(number)}')

end = time.time()

print(f'Время выполнения программы: {end - start}')
