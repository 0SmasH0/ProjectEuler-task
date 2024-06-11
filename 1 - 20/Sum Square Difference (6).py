"""
https://projecteuler.net/problem=6
"""

import time

trigger = 100


def ssd_algo(num: int) -> int:
    sum_of_sq = 0
    sq_of_sum = 0

    for i in range(1, num+1):
        sum_of_sq += i**2
        sq_of_sum += i

    return sq_of_sum**2 - sum_of_sq


start = time.time()

print(f'Результат: {ssd_algo(trigger)}')

end = time.time()

print(f'Время выполнения программы: {end - start}')
