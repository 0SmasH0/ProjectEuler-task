"""
https://projecteuler.net/problem=14
"""

import time

number = int(input('Введите число: '))


def Longest_Collatz_Sequence(num: int) -> int:

    maxi = 1

    for el in range(1, num, 2):

        copy_el = el
        seq = 1

        while copy_el != 1:
            if copy_el % 2 == 0:
                copy_el //= 2
            else:
                copy_el = copy_el * 3 + 1

            seq += 1

        if maxi < seq:
            maxi = seq
            our_num = el

    return our_num


start = time.time()

print(f'Результат: {Longest_Collatz_Sequence(number)}')

end = time.time()

print(f'Время выполнения программы: {end - start}')
