"""
https://projecteuler.net/problem=16
"""

import time

number = int(input('Введите число: '))
power = int(input('Введите степень: '))

def num_power(num: int, pow: int) -> int:

    suma = 0

    res = str(num ** pow)

    for i in res:
        suma += int(i)

    return suma


start = time.time()

print(f'Результат: {num_power(number, power)}')

end = time.time()

print(f'Время выполнения программы: {end - start}')
