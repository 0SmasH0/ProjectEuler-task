"""
https://projecteuler.net/problem=5
"""

import time

number = 20


def is_prime(n: int) -> bool:
    d = 2
    while d ** 2 <= n and n % d != 0:
        d += 1
    return d ** 2 > n


def smallest_mul(num: int) -> int:

    our_num = [1]
    prod = 1

    for i in range(2, num + 1):
        if is_prime(i):
            our_num.append(i)
        else:
            val = i
            for el in our_num:
                val /= el
                if val == 1:
                    break
                elif val != int(val):
                    val *= el

            if val != 1:
                our_num.append(int(val))

    for k in our_num:
        prod *= k

    return prod


start = time.time()

print(f'Результат: {smallest_mul(number)}')

end = time.time()

print(f'Время выполнения программы: {end - start}')
