"""
https://projecteuler.net/problem=10
"""

import time

number = int(input('Введите число: '))


# Решето Эратосфена
def suma_prime(num: int) -> int:

    lst = list(range(num))

    lst[1] = 0

    for i in lst[2:]:
        for j in range(2*i, len(lst), i):
            lst[j] = 0

    return sum(lst)


start = time.time()

print(f'Результат: {suma_prime(number)}')

end = time.time()

print(f'Время выполнения программы: {end - start}')
