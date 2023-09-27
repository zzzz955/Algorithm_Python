def fibonacci(index):
    if not isinstance(index, int) or index < 1:
        print('자연수를 입력해 주세요')
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


def fibonacci_recursive(index):
    if not isinstance(index, int) or index < 1:
        print('자연수를 입력해 주세요')
        return
    if index <= 2:
        return 1
    return fibonacci_recursive(index-1) + fibonacci_recursive(index-2)


def fibonacci_dynamic(index):
    if not isinstance(index, int) or index < 1:
        print('자연수를 입력해 주세요')
        return
    dp = [0, 1]
    for i in range(2, index+1):
        dp.append(dp[i-1] + dp[i-2])
    print(max(dp))


def fibonacci_dynamic2(index):
    if not isinstance(index, int) or index < 1:
        print('자연수를 입력해 주세요')
        return
    dp = [[0] * index]
    dp[0][0] = 1
    dp[0][1] = 1

    for i in range(2, index):
        dp[0][i] = dp[0][i-2] + dp[0][i-1]
    print(max(max(dp)))

