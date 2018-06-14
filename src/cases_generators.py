"""Генераторы примеров"""


def cases_div():
    return (f'{x * y} / {x}' for x in range(1, 10) for y in range(1, 10))


def cases_mul():
    return (f'{x} * {y}' for x in range(1, 10) for y in range(1, 10))


def cases_sub():
    return (f'{x + y} - {x}' for x in range(1, 10) for y in range(1, 10))


def cases_add():
    return (f'{x} + {y}' for x in range(1, 10) for y in range(1, 10))


def cases_all():
    all_generators = [cases_div(),
                      cases_mul(),
                      cases_sub(),
                      cases_add()]
    for cases in all_generators:
        for case in cases:
            yield case


if __name__ == '__main__':
    generator = cases_all()
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
