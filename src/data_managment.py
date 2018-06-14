"""Загрузка сохранение данных"""

import json
import time
from pathlib import Path

from src.cases_generators import cases_all

DATA_PATH = Path(__file__).parent / 'data' / 'results.json'
INDENT = 0
NEW = 'new_case'
OLD = 'old_case'
RIGHT_MULTIPLIER = 1.5
MIN_DELTA = 10.0


class Case:
    def __init__(self, case, last_time):
        self._case = case
        self._last_time = last_time

    def __repr__(self):
        return f'\nCase(case={self._case}, last_time={self._last_time})'

    def __lt__(self, other):
        return self.last_time < other.last_time

    @property
    def case(self):
        return self._case

    @property
    def last_time(self):
        return self._last_time

    def setup_time(self):
        self._last_time = time.time()

    def right(self):
        if time.time() > self._last_time:
            self._last_time = (time.time() - self._last_time) * RIGHT_MULTIPLIER + time.time()
        else:
            raise ValueError

    def wrong(self):
        self._last_time = time.time() - MIN_DELTA

    @property
    def result(self):
        return eval(self._case)


def load_data():
    if DATA_PATH.exists():
        with open(DATA_PATH, mode='r') as file:
            raw_cases = json.load(file)
    else:
        DATA_PATH.parent.mkdir(parents=True)
        new_cases = [[case, None] for case in cases_all()]
        raw_cases = {NEW: new_cases,
                     OLD: []}
        with open(DATA_PATH, mode='w') as file:
            json.dump(raw_cases, file, indent=INDENT)
    new_cases = [Case(case, last_time) for case, last_time in raw_cases[NEW]]
    old_cases = [Case(case, last_time) for case, last_time in raw_cases[OLD]]
    return new_cases, old_cases


def save_data(new_cases, old_cases):
    new_cases = [[case.case, case.last_time] for case in new_cases]
    old_cases = [[case.case, case.last_time] for case in old_cases]
    raw_cases = {NEW: new_cases,
                 OLD: old_cases}
    with open(DATA_PATH, mode='w') as file:
        json.dump(raw_cases, file, indent=INDENT)


if __name__ == '__main__':
    print(load_data())
