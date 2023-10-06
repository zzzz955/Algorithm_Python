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
    dp = [0] * index
    dp[0] = 1
    dp[1] = 1

    for i in range(2, index):
        dp[i] = dp[i-2] + dp[i-1]

    print(max(dp))

