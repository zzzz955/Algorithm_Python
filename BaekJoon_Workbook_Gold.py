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
    char_map = {chr(i): chr(i) for i in range(65, 123)}
    for _ in range(int(n)):
        order = sys.stdin.readline().split()
        if order[0] == '1':
            for char in char_map:
                if char_map[char] == order[1]:
                    char_map[char] = order[2]
        else:
            transformed_s = ''.join(char_map[char] for char in s)
            print(transformed_s)
q27396()


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


def q12904():
    # 백준 12904번 파이썬 A와 B
    s = input()
    t = input()
    for i in range(len(t) - len(s)):
        if t[-1] == 'A':
            t = t[:-1]
        else:
            t = t[:-1][::-1]
    print(1 if s == t else 0)


def q5430():
    # 백준 5430번 파이썬 AC
    import collections

    t = int(input())
    for _ in range(t):
        p = input()
        n = int(input())
        s = input()[1:-1]
        deq = collections.deque(s.split(','))
        chk = True
        rev = False
        for char in p:
            if char == 'R':
                if rev:
                    rev = False
                else:
                    rev = True
            else:
                if len(deq) >= 1 and not (len(deq) == 1 and deq[0] == ''):
                    if rev:
                        deq.pop()
                    else:
                        deq.popleft()
                else:
                    chk = False
                    break
        if rev:
            deq.reverse()
        print('[' + ','.join(deq) + ']' if chk else 'error')


def q1107():
    # 백준 1107번 파이썬 리모컨
    n = int(input())
    m = int(input())
    if m:
        broken = set(map(int, input().split()))
    else:
        broken = {}
    min_val = abs(100 - n)
    for i in range(1000000):
        s = str(i)
        for j in s:
            if int(j) in broken:
                break
        else:
            min_val = min(min_val, abs(n - i) + len(s))
    print(min_val)


def q1727():
    # 백준 1727번 파이썬 커플 만들기
    n, m = map(int, input().split())
    lst1 = sorted(list(map(int, input().split())))
    lst2 = sorted(list(map(int, input().split())))
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i - 1][j - 1] + abs(lst1[i - 1] - lst2[j - 1])
            if i > j:
                dp[i][j] = min(dp[i][j], dp[i - 1][j])
            if i < j:
                dp[i][j] = min(dp[i][j], dp[i][j - 1])
    print(dp[n][m])


def q1781():
    # 백준 1781번 파이썬 컵라면
    import sys, heapq

    n = int(sys.stdin.readline())
    lst = []
    for _ in range(n):
        d, c = map(int, sys.stdin.readline().split())
        lst.append([d, c])
    lst.sort(key=lambda x: (x[0], -x[1]))

    stack = []
    for i in lst:
        heapq.heappush(stack, i[1])
        if len(stack) > i[0]:
            heapq.heappop(stack)
    print(sum(stack))


def q14503():
    # 백준 14503번 로봇 청소기 파이썬
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    dist = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    result = 0
    cleaned = [[False] * m for _ in range(n)]

    while 1:
        if not cleaned[r][c]:
            cleaned[r][c] = True
            result += 1
        cleaned_or_moved = False
        for _ in range(4):
            d = (d + 3) % 4
            nr, nc = r + dist[d][0], c + dist[d][1]
            if 0 <= nr < n and 0 <= nc < m and not cleaned[nr][nc] and lst[nr][nc] == 0:
                r, c = nr, nc
                cleaned_or_moved = True
                break
        if not cleaned_or_moved:
            back = (d + 2) % 4
            br, bc = r + dist[back][0], c + dist[back][1]
            if 0 <= br < n and 0 <= bc < m and lst[br][bc] == 0:
                r, c = br, bc
            else:
                break
    print(result)


def q3190():
    # 백준 3190번 뱀 파이썬
    import collections

    n = int(input())
    dp = [[0] * n for _ in range(n)]
    k = int(input())
    for _ in range(k):
        x, y = map(int, input().split())
        dp[x - 1][y - 1] = 1
    l = int(input())
    dist_change = [tuple(input().split()) for _ in range(l)]
    dist_change_index = 0
    dist = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dist_index = 0
    time = 0
    snake = collections.deque([(0, 0)])
    while 1:
        time += 1
        head = snake[-1]
        nr, nc = head[0] + dist[dist_index][0], head[1] + dist[dist_index][1]
        if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in snake:
            snake.append((nr, nc))
        else:
            break
        if dp[nr][nc] == 1:
            dp[nr][nc] = 0
        else:
            snake.popleft()
        if dist_change_index < l and time == int(dist_change[dist_change_index][0]):
            if dist_change[dist_change_index][1] == 'D':
                dist_index = (dist_index + 1) % 4
            else:
                dist_index = (dist_index + 3) % 4
            dist_change_index += 1
    print(time)
q3190()