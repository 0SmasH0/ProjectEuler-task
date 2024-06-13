"""
https://projecteuler.net/problem=12
"""

import time

length = int(input('Введите число делителей > : '))


def solution(length: int) -> int:
    nums = 4
    t_num = 6

    while True:
        div = 2
        t_num += nums

        end_point = int(t_num ** (1/2))

        for i in range(2, end_point + 1):

            res = t_num / i
            if res == int(res):

                if res == end_point:
                    div += 1
                    if div > length:
                        return t_num
                    else:
                        break

                div += 2

                if div > length:
                    return t_num

        nums += 1


start = time.time()

print(f'Результат: {solution(length)}')

end = time.time()

print(f'Время выполнения программы: {end - start}')

