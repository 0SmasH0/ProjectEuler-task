"""
https://projecteuler.net/problem=50
"""

import time

numbers = int(input('Введите число: '))


def eratosfen(num: int) -> list:
    lst = list(range(num))
    lst[1] = 0
    for i in lst[2:]:
        for j in range(2 * i, len(lst), i):
            lst[j] = 0

    lst = [i for i in lst if i != 0 and i > 1000]
    return lst


def check(temporary_list: list) -> str:
    res = ''
    for idx, el_1 in enumerate(temporary_list):
        for el_2 in temporary_list[idx + 1:]:

            dif = abs(el_2 - el_1)

            max_el = max(el_1, el_2)

            el_3 = max_el + dif

            if el_3 in temporary_list:
                res = str(el_1) + str(el_2) + str(el_3)
                return res
            else:
                continue
    return res


def solution(num: int) -> str:
    primes_numbers = eratosfen(num)

    for idx, i in enumerate(primes_numbers):

        if '0' in str(i):
            continue

        num_1 = sorted([el for el in str(i)])

        temporary_list = [i]

        for j in primes_numbers[idx + 1:]:

            if '0' in str(j):
                continue

            num_2 = sorted([el for el in str(j)])

            if num_1 == num_2:
                temporary_list.append(j)

        if len(temporary_list) > 2:
            res = check(temporary_list)
            if res and res != "148748178147":
                return res

    return 'Такого числа нет'


start = time.time()

print(f'Результат: {solution(numbers)}')

end = time.time()

print(f'Время выполнения программы: {end - start}')
