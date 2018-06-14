"""Генераторы примеров"""

RANGE = range(9, 0, -1)


def cases_div():
    return (f'{x * y} / {x}' for x in RANGE for y in RANGE)


def cases_mul():
    return (f'{x} * {y}' for x in RANGE for y in RANGE)


def cases_sub():
    return (f'{x + y} - {x}' for x in RANGE for y in RANGE)


def cases_add():
    return (f'{x} + {y}' for x in RANGE for y in RANGE)


def cases_all():
    all_generators = [cases_add(),
                      cases_sub(),
                      cases_mul(),
                      cases_div()]
    for cases in all_generators:
        for case in cases:
            yield case


if __name__ == '__main__':
    print(list(cases_all()))
