"""
https://projecteuler.net/problem=48
"""

import time

number = int(input('Введите число: '))


def solutions(num: int) -> str:
    suma = 1
    for i in range(2, num + 1):
        suma += i ** i

    return str(suma)[-10:]


start = time.time()

print(f'Результат: {solutions(number)}')

end = time.time()

print(f'Время выполнения программы: {end - start}')