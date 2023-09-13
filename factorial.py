def factorial(index):
    if index > 2:
        result = index
        for i in range(1, index):
            result = result * (index-i)
        return result
    else:
        return 1


def factorial_func(index):
    if index < 2:
        return 1
    return index * factorial_func(index-1)

