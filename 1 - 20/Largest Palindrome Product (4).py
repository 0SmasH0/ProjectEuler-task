"""
https://projecteuler.net/problem=4
"""

import time


def lpp() -> int:

    maxi = 1

    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            num = str(i * j)
            if num == num[::-1] and maxi < int(num):
                maxi = int(num)

    return maxi


start = time.time()

print(f'Результат: {lpp()}')

end = time.time()

print(f'Время выполнения программы: {end - start}')
