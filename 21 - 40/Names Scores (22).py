"""
https://projecteuler.net/problem=22
"""

import time

with open('names.txt', 'r') as f:
    data = sorted(f.read().replace('"', '').split(','))


def solutions(data: list) -> int:

    alphabet = {chr(i): i - 64 for i in range(65, 91)}
    end_suma = 0

    for idx, el in enumerate(data):

        idx += 1
        suma = 0

        for i in el:
            suma += alphabet[i]

        end_suma += suma * idx

    return end_suma


start = time.time()

print(f'Результат: {solutions(data)}')

end = time.time()

print(f'Время выполнения программы: {end - start}')
