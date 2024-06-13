"""
https://projecteuler.net/problem=56
"""

import time


def solution() -> int:

    maxi = 0

    k = 1

    for a in range(2, 100):

        if k * 10 == a:
            k += 1
            continue

        for b in range(2, 100):

            num = a ** b
            suma = sum(map(int, str(num)))

            if maxi < suma:
                maxi = suma

    return maxi


start = time.time()

print(f'Результат: {solution()}')

end = time.time()

print(f'Время выполнения программы: {end - start}')
