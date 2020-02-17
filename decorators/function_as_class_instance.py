import random


class Memento:
    def __init__(self, fnc):
        self._fnc = fnc
        self._memory = []

    def __call__(self, *args, **kwargs):
        result = self._fnc()
        self._memory.append(result)
        return result

    def memory(self):
        return self._memory


@Memento
def random_number():
    return random.choice([i for i in range(0, 99)])


if __name__ == '__main__':
    print(random_number)
    print(random_number())
    print(random_number)
    print(random_number.memory())
    print(random_number)
    print(random_number())
    print(random_number.memory())
