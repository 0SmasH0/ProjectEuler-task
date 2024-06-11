"""
https://projecteuler.net/problem=7
"""

import time

index = int(input('Введите индекс: '))


def is_prime(num: int) -> bool:
    d = 2
    while d**2 <= num and num % d != 0:
        d += 1

    return d ** 2 > num


def index_prime(index: int) -> int:

    idx, num = 0, 1

    while idx != index:
        num += 1
        if is_prime(num):
            idx += 1

    return num


start = time.time()

print(f'Результат: {index_prime(index)}')

end = time.time()

print(f'Время выполнения программы: {end - start}')
