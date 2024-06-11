"""
https://projecteuler.net/problem=3
"""

import time

number = int(input('Введите число: '))


def lpf(num: int) -> int:
    maxi = 1
    prod = 1
    for i in range(2, int(num ** (1 / 2))):
        if num % i == 0 and prod * i <= num:
            maxi = i
            prod *= i

    return maxi


start = time.time()

print(f'Результат: {lpf(number)}')

end = time.time()

print(f'Время выполнения программы: {end - start}')
