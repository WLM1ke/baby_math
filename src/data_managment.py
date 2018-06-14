"""Загрузка сохранение данных"""

import json
from pathlib import Path

from src.cases_generators import cases_all

DATA_PATH = Path(__file__).parent / 'data' / 'results.json'
INDENT = 0


class Case:
    def __init__(self, case, last_time):
        self._case = case
        self._last_time = last_time

    def __repr__(self):
        return f'\nCase(case={self._case}, last_time={self._last_time})'

    @property
    def case(self):
        return self._case

    @property
    def last_time(self):
        return self._last_time

    def check(self, result):
        return eval(self._case) == eval(result)


def load_data():
    if DATA_PATH.exists():
        with open(DATA_PATH, mode='r') as file:
            raw_cases = json.load(file)
    else:
        DATA_PATH.parent.mkdir(parents=True)
        raw_cases = [[case, None] for case in cases_all()]
        with open(DATA_PATH, mode='w') as file:
            json.dump(raw_cases, file, indent=INDENT)
    return [Case(case, last_time) for case, last_time in raw_cases]


def save_data(cases):
    with open(DATA_PATH, mode='w') as file:
        raw_cases = [[case.case, case.last_time] for case in cases]
        json.dump(raw_cases, file, indent=INDENT)


if __name__ == '__main__':
    print(load_data())
