"""Основной файл - выдает примеры и проверяет ответы"""

import heapq
import time

from cases_generators import cases_all
from data_managment import load_data, save_data

END_SCORE = 30
END_NEW = 3
TIME_TO_SOLVE = 7


class BabyMath:

    def __init__(self):
        self._counter = 0
        self._new_counter = 0
        self._new_cases, self._old_cases = load_data()
        print('Начало игры')
        print(f'Новые примеры - {len(self._new_cases)}')
        print(f'Старые примеры - {len(self._old_cases)}')
        if len(self._old_cases) + len(self._new_cases) != len(list(cases_all())):
            raise ValueError('Не верное количество примеров.')

    @property
    def counter(self):
        return self._counter

    @property
    def new_counter(self):
        return self._new_counter

    def _add_case(self):
        try:
            new_case = self._new_cases.pop()
            heapq.heappush(self._old_cases, new_case)
        except IndexError:
            print('новых примеров нет - ', end='')
        self._new_counter += 1

    def test(self):
        print(f'\nСчет {self.counter} - ', end='')
        if (not self._old_cases) or (self._old_cases[0].next_time > time.time()):
            self._add_case()
            print(f'новый пример {self.new_counter}.')
        else:
            print('повторение.')
        test_case = heapq.heappop(self._old_cases)
        while True:
            now = time.time()
            result = input(f'{test_case.case} = ')
            score = 1 - (time.time() - now) / TIME_TO_SOLVE
            if not test_case.check_result(result, score):
                print('НЕПРАВИЛЬНО - попробуй еще!!!')
                self._counter -= 1
                print(f'\nСчет {self._counter}.')
            elif score > 0:
                print('ПРАВИЛЬНО!!!')
                self._counter += 1
                heapq.heappush(self._old_cases, test_case)
                save_data(self._new_cases, self._old_cases)
                break
            else:
                print('ПРАВИЛЬНО, НО МЕДЛЕННО!!!')
                self._counter -= 1
                heapq.heappush(self._old_cases, test_case)
                save_data(self._new_cases, self._old_cases)
                break


if __name__ == '__main__':
    math = BabyMath()
    print(f'\nИГРА ДО {END_SCORE} ОЧКОВ И {END_NEW} НОВЫХ ПРИМЕРОВ.')
    while (math.counter < END_SCORE) or (math.new_counter < END_NEW):
        math.test()
    print('\n*** ТЫ ВЫЙГРАЛ!!! ***')
    print(f'\nИзучено {math.new_counter} новых примеров.')
