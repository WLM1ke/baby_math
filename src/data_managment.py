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
MIN_REPEAT = 3
MIN_DELTA = 10.0
DAY_IN_SECONDS = 60 * 60 * 24


class Case:
    def __init__(self, case, next_time=0, right_count=0):
        self._case = case
        self._next_time = next_time
        self._right_count = right_count

    def __repr__(self):
        return f'\nCase(case={self._case}, next_time={self._next_time}, right_count={self._right_count})'

    def __lt__(self, other):
        return self.next_time < other.next_time

    @property
    def case(self):
        return self._case

    @property
    def next_time(self):
        return self._next_time

    @property
    def right_count(self):
        return self._right_count

    def _right(self):
        self._right_count += 1
        now = time.time()
        if now > self._next_time:
            if self._right_count < MIN_REPEAT:
                self._next_time = now + MIN_DELTA
            else:
                self._next_time = now + DAY_IN_SECONDS * RIGHT_MULTIPLIER ** (self._right_count - MIN_REPEAT)
        else:
            raise ValueError

    def _wrong(self):
        self._right_count = 0

    def test_result(self, result):
        if eval(self._case) == float(result):
            self._right()
            return True
        else:
            self._wrong()
            return False


def load_data():
    if DATA_PATH.exists():
        with open(DATA_PATH, mode='r') as file:
            raw_cases = json.load(file)
    else:
        DATA_PATH.parent.mkdir(parents=True)
        new_cases = [case for case in cases_all()]
        raw_cases = {NEW: new_cases,
                     OLD: []}
        with open(DATA_PATH, mode='w') as file:
            json.dump(raw_cases, file, indent=INDENT)
    new_cases = [Case(case) for case in raw_cases[NEW]]
    old_cases = [Case(case, last_time, right_count) for case, last_time, right_count in raw_cases[OLD]]
    return new_cases, old_cases


def save_data(new_cases, old_cases):
    new_cases = [case.case for case in new_cases]
    old_cases = [[case.case, case.next_time, case.right_count] for case in old_cases]
    raw_cases = {NEW: new_cases,
                 OLD: old_cases}
    with open(DATA_PATH, mode='w') as file:
        json.dump(raw_cases, file, indent=INDENT)


if __name__ == '__main__':
    print(load_data())
