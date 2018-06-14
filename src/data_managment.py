"""Загрузка сохранение данных"""

import json
from pathlib import Path

from src.cases_generators import cases_all

DATA_PATH = Path(__file__).parent / 'data' / 'results.json'


def load_data():
    if DATA_PATH.exists():
        with open(DATA_PATH, mode='r') as file:
            return json.load(file)
    else:
        DATA_PATH.parent.mkdir(parents=True)
        cases = [[case, None] for case in cases_all()]
        with open(DATA_PATH, mode='w') as file:
            json.dump(cases, file, indent=4)
        return cases


if __name__ == '__main__':
    print(load_data())
