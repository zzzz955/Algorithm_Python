# 동적 계획법1
# https://www.acmicpc.net/step/16


class q24416:
    # 피보나치 수 1
    def __init__(self):
        self.search1 = 0
        self.search2 = 0
        n = int(input())
        result1 = self.fibonacci_recursive(n)
        result2 = self.fibonacci_dp(n)
        print(f'{result1} {result2}')

    def fibonacci_recursive(self, index):
        dp = [0, 1]
        for i in range(2, index + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return max(dp)

    def fibonacci_dp(self, index):
        for i in range(2, index):
            self.search2 += 1
        return self.search2


class q9184:
    # 신나는 함수 실행
    def __init__(self):
        self.dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]
        result = []
        while 1:
            a, b, c = map(int, input().split())
            if a == -1 and b == -1 and c == -1:
                for string in result:
                    print(string)
                break
            result.append(f'w({a}, {b}, {c}) = {self.w(a, b, c)}')

    def w(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return 1
        elif a > 20 or b > 20 or c > 20:
            return self.w(20, 20, 20)
        elif self.dp[a][b][c]:
            return self.dp[a][b][c]
        elif a < b < c:
            self.dp[a][b][c] = self.w(a, b, c - 1) + self.w(a, b - 1, c - 1) - self.w(a, b - 1, c)
            return self.dp[a][b][c]
        else:
            self.dp[a][b][c] = self.w(a - 1, b, c) + self.w(a - 1, b - 1, c)\
                               + self.w(a - 1, b, c - 1) - self.w(a - 1, b - 1, c - 1)
            return self.dp[a][b][c]


def q1904():
    # 01타일
    n = int(input())
    dp = [0] * 1000001
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 15746
    print(dp[n - 1])


def q9461():
    # 파도반 수열
    t = int(input())
    result = []
    for _ in range(t):
        n = int(input())
        dp = [1, 1, 1, 2, 2]
        if n <= 3:
            result.append(1)
        elif n <= 5:
            result.append(2)
        else:
            for i in range(5, n):
                dp.append(dp[i - 1] + dp[i - 5])
            result.append(dp[n - 1])
    for ans in result:
        print(ans)


def q1912():
    # 연속합
    n = int(input())
    lst = list(map(int, input().split()))
    length = len(lst)
    dp = [0] * (length + 1)
    dp[1] = lst[0]
    for i in range(1, length + 1):
        dp[i] = max(dp[i - 1] + lst[i - 1], lst[i - 1])
    print(max(dp[1:]))

