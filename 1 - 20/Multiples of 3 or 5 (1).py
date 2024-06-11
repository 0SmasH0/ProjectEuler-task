"""
https://projecteuler.net/problem=1
"""

import time

number = int(input('Введите число: '))


def multiplicity(num: int) -> int:
    suma = 0

    for i in range(3, num):
        if i % 3 == 0 or i % 5 == 0:
            suma += i

    return suma


start = time.time()

print(f'Результат: {multiplicity(number)}')

end = time.time()

print(f'Время выполнения программы: {end - start}')
