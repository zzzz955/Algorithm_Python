def q12348():
    # 백준 12348번 파이썬 분해합2
    n = int(input())
    if n in [2, 4, 6, 8]:
        print(n // 2)
        return
    if n > 19:
        length = len(str(n)) * 9
    else:
        length = (len(str(n)) - 1) * 9
    result = 0
    for i in range(n - length, n):
        temps = []
        for j in str(i):
            temps.append(int(j))
        if i + sum(temps) == n:
            result = i
            break
    print(result)


def q10986():
    # 백준 10986번 파이썬 나머지 합
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    sum_val = 0
    remainder = [0] * m
    for i in range(n):
        sum_val += lst[i]
        remainder[sum_val % m] += 1
    result = remainder[0]
    for i in remainder:
        result += i * (i - 1) // 2
    print(result)


def q27396():
    # 백준 27396번 파이썬 문자열 변환과 쿼리
    import sys

    s, n = sys.stdin.readline().split()
    s = list(s)
    dic = {}
    for _ in range(int(n)):
        order = sys.stdin.readline().split()
        if order[0] == '1':
            dic[order[1]] = order[2]
            for key, val in dic.items():
                if val == order[1]:
                    dic[key] = order[2]
        else:
            for i in range(len(s)):
                if s[i] in dic:
                    s[i] = dic[s[i]]
            dic.clear()
            print(''.join(s))


def q1715():
    # 백준 1715번 파이썬 카드 정렬하기
    import sys, heapq

    n = int(sys.stdin.readline())
    lst = []
    for _ in range(n):
        heapq.heappush(lst, int(sys.stdin.readline()))
    if len(lst) == 1:
        print(0)
        return
    else:
        result = 0
        while len(lst) > 1:
            a = heapq.heappop(lst)
            b = heapq.heappop(lst)
            result += a + b
            heapq.heappush(lst, a + b)
        print(result)


def q13904():
    # 백준 13904번 파이썬 과제
    import sys, heapq

    n = int(sys.stdin.readline())
    lst = []
    day = 0
    for _ in range(n):
        d, w = map(int, sys.stdin.readline().split())
        lst.append((-w, d))
        if d > day:
            day = d
    heapq.heapify(lst)
    chk = [0] * (day + 1)
    result = 0
    while lst:
        w, d = heapq.heappop(lst)
        for i in range(d, 0, -1):
            if chk[i]:
                continue
            chk[i] = 1
            result += -w
            break
    print(result)


def q2879():
    # 백준 2879번 파이썬 코딩은 예쁘게
    n = int(input())
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    temp = []
    for i in range(n):
        temp.append(lst1[i] - lst2[i])
    dp = [0] * n
    dp[0] = abs(temp[0])
    for i in range(1, n):
        if temp[i] * temp[i - 1] > 0:
            dp[i] = dp[i - 1] + max(0, abs(temp[i]) - abs(temp[i - 1]))
        else:
            dp[i] = dp[i - 1] + abs(temp[i])
    print(dp[n - 1])


def q8980():
    # 백준 8980번 파이썬 택배
    import sys

    n, c = map(int, sys.stdin.readline().split())
    m = int(sys.stdin.readline())
    lst = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    lst.sort(key=lambda x: x[1])
    result = 0
    limit = [c] * (n + 1)
    for i in range(m):
        temp = c
        for j in range(lst[i][0], lst[i][1]):
            temp = min(temp, limit[j])
        temp = min(temp, lst[i][2])
        for k in range(lst[i][0], lst[i][1]):
            limit[k] -= temp
        result += temp
    print(result)
q8980()
