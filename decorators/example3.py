import random
from math import pow


def power_of(arg):
    def decorator(fnc):
        def inner():
            return fnc() ** exponent

        return inner

    if callable(arg):
        exponent = 2
        return decorator(arg)
    else:
        exponent = arg
        return decorator


@power_of
def random_odd_number():
    return random.choice([1, 3, 5, 7, 9])


if __name__ == '__main__':
    print(random_odd_number())
