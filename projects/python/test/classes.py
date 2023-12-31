def func(val, test=[]):
    test.append(val)
    return test


def func_better(val, test: list = None):
    if test is None:
        test = []
    test.append(val)
    return test


if __name__ == "__main__":
    t = func(10)

    print(t)

    func(20)
    func(30)

    print(func(10))
