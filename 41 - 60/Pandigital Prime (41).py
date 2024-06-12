"""
https://projecteuler.net/problem=41
"""

import time


def is_prime(num: int) -> int:
    d = 2
    while d ** 2 <= num and num % d != 0:
        d += 1

    return d ** 2 > num


def pan_prime() -> int:
    lst_sum_of_digits = [1, 3, 6, 10, 15, 21, 28, 36, 45]

    for i in range(1_000_000_0, 1, -1):
        suma = 0

        our_num = str(i)
        unique = set(our_num)

        if len(our_num) == len(unique) and '0' not in unique:
            for j in our_num:
                suma += int(j)

            if suma in lst_sum_of_digits and is_prime(i):
                return i


start = time.time()

print(f'Результат: {pan_prime()}')

end = time.time()

print(f'Время выполнения программы: {end - start}')
