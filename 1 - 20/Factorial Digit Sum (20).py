"""
https://projecteuler.net/problem=20
"""

import time

number = int(input('Введите число: '))


def factorial(num: int) -> int:
    if num == 1:
        return 1

    return num * factorial(num - 1)


def suma_factorial(num: int) -> int:

    res, suma = str(factorial(num)), 0

    for i in res:
        suma += int(i)

    return suma


start = time.time()

print(f'Результат: {suma_factorial(number)}')

end = time.time()

print(f'Время выполнения программы: {end - start}')
