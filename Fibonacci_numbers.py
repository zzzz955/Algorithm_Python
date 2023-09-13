def fibonacci(index):
    if not isinstance(index, int):
        print('정수 값을 입력해 주세요')
        return
    if 0 < index <= 2:
        return index
    default_nums = [1, 1]
    while index > 2:
        index = len(default_nums)
        result_num = default_nums[index-1] + default_nums[index-2]
        default_nums.append(result_num)
        index -= 1
    return sum(default_nums)


def fibonacci_recursive_func(index):
    if not isinstance(index, int):
        print('정수 값을 입력해 주세요')
        return
    if index <= 2:
        return 1
    return fibonacci_recursive_func(index-1) + fibonacci_recursive_func(index-2)

