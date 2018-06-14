"""Основной файл - выдает примеры и проверяет ответы"""

import heapq
import time

from src.cases_generators import cases_all
from src.data_managment import load_data, save_data


class BabyMath:

    def __init__(self):
        self._counter = 0
        self._new_cases, self._old_cases = load_data()
        print('Начало игры')
        print(f'Новые примеры - {len(self._new_cases)}')
        print(f'Старые примеры - {len(self._old_cases)}')
        if len(self._old_cases) + len(self._new_cases) != len(list(cases_all())):
            raise ValueError('Не верное количество примеров.')

    def _add_case(self):
        new_case = self._new_cases.pop()
        heapq.heappush(self._old_cases, new_case)

    def test(self):
        print(f'\nСчет {self._counter} - ', end='')
        if (not self._old_cases) or (self._old_cases[0].next_time > time.time()):
            self._add_case()
            print('новый пример.')
        else:
            print('повторение.')
        test_case = heapq.heappop(self._old_cases)
        while True:
            result = float(input(f'{test_case.case} = '))
            if test_case.result == result:
                print('ПРАВИЛЬНО!!!')
                self._counter += 1
                test_case.right()
                heapq.heappush(self._old_cases, test_case)
                save_data(self._new_cases, self._old_cases)
                break
            else:
                print('НЕПРАВИЛЬНО - попробуй еще!!!')
                self._counter -= 1
                print(f'Счет {self._counter}.')
                test_case.wrong()


if __name__ == '__main__':
    math = BabyMath()
    while True:
        math.test()
