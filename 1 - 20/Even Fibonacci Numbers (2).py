"""
https://projecteuler.net/problem=2
"""

import time

trigger = 4_000_000


def fib_algo(num: int) -> int:
    suma = 0

    first, second = 1, 1

    while first <= num:
        first, second = second, first + second

        """
        val = first
        first += second
        second = val
        """

        if first % 2 == 0:
            suma += first

    return suma


start = time.time()

print(f'Результат: {fib_algo(trigger)}')

end = time.time()

print(f'Время выполнения программы: {end - start}')
