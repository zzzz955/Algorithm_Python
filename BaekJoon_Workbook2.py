# 단기간 성장
# https://www.acmicpc.net/workbook/view/4349


def q12865():
    # 평범한 배낭
    n, k = map(int, input().split())
    weights = []
    values = []
    for i in range(n):
        w, v = map(int, input().split())
        weights.append(w)
        values.append(v)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp[n][k])


def q1655():
    # 가운데를 말해요
    import sys
    import heapq
    n = int(sys.stdin.readline())
    result = []

    max_heap = []
    min_heap = []

    for _ in range(n):
        x = int(sys.stdin.readline())

        if len(max_heap) == len(min_heap):
            heapq.heappush(max_heap, (-x, x))
        else:
            heapq.heappush(min_heap, (x, x))

        if min_heap and max_heap[0][1] > min_heap[0][0]:
            min = heapq.heappop(min_heap)[0]
            max = heapq.heappop(max_heap)[1]
            heapq.heappush(max_heap, (-min, min))
            heapq.heappush(min_heap, (max, max))
        result.append(max_heap[0][1])
    for data in result:
        print(data)


def q1463():
    # 1로 만들기
    x = int(input())
    dp = [0] * (x + 1)
    for i in range(2, x + 1):
        dp[i] = dp[i - 1] + 1
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
    print(dp[x])

