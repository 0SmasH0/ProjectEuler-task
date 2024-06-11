"""
https://projecteuler.net/problem=25
"""

import time

len_digit = 1000


def digit_fib_num(ld: int) -> int:
    first, second = 1, 1

    idx = 2

    while len(str(second)) != len_digit:
        first, second = second, first + second
        idx += 1

    return idx


start = time.time()

print(f'Результат: {digit_fib_num(len_digit)}')

end = time.time()

print(f'Время выполнения программы: {end - start}')
