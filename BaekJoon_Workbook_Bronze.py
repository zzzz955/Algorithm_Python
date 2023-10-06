def q14563():
    # 완전수
    n = int(input())
    nums = list(map(int, input().split()))
    result = []
    for num in nums:
        div = 1
        sum_val = 0
        while div != (num // 2) + 1:
            if num % div == 0:
                sum_val += div
            div += 1
        if sum_val == num:
            result.append('Perfect')
        elif sum_val > num:
            result.append('Abundant')
        else:
            result.append('Deficient')
    for answer in result:
        print(answer)


def q1773():
    # 폭죽쇼
    n, c = map(int, (input().split()))
    dp = [0] * 2000001
    for _ in range(n):
        time = int(input())
        for i in range(time, c + 1, time):
            dp[i] = 1
    print(sum(dp))


def q2775():
    # 부녀회장이 될테야
    t = int(input())
    result = []
    for _ in range(t):
        k = int(input())
        n = int(input())
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        for i in range(1, n + 1):
            dp[0][i] = i
        for i in range(1, k + 1):
            for j in range(1, n + 1):
                dp[i][j] = sum(dp[i - 1][:j + 1])
        result.append(dp[k][n])
    for answer in result:
        print(answer)
q2775()