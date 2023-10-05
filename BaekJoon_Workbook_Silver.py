def q1010():
    # 다리 놓기
    t = int(input())
    result = []
    for _ in range(t):
        n, m = map(int, input().split())
        over = 1
        under1 = 1
        under2 = 1
        for i in range(1, m + 1):
            over *= i
        for j in range(1, m - n + 1):
            under1 *= j
        for k in range(1, n + 1):
            under2 *= k
        result.append(over // (under1 * under2))
    for data in result:
        print(data)


def q1002():
    # 터렛
    import math
    t = int(input())
    for _ in range(t):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if distance == 0 and r1 == r2:
            print(-1)
        elif abs(r1 - r2) == distance or r1 + r2 == distance:
            print(1)
        elif abs(r1 - r2) < distance < (r1 + r2):
            print(2)
        else:
            print(0)


def q1769():
    # 3의 배수
    x = input()
    changes = 0
    length = len(x)
    temp = 0
    while length != 1:
        temp = 0
        for char in x:
            temp += int(char)
        x = str(temp)
        length = len(x)
        changes += 1
    print(changes)
    if changes == 0:
        if int(x) % 3 == 0:
            print('YES')
        else:
            print('NO')
    else:
        if temp % 3 == 0:
            print('YES')
        else:
            print('NO')


def q1417():
    # 국회의원 선거
    t = int(input())
    lst = []
    buy = 0
    for _ in range(t):
        lst.append(int(input()))
    dasom = lst.pop(0)
    if lst:
        while dasom <= max(lst):
            lst[lst.index(max(lst))] -= 1
            dasom += 1
            buy += 1
    print(buy)


def q2828():
    # 사과 담기 게임
    n, m = map(int, input().split())
    j = int(input())
    location = []
    current = 1
    result = 0
    for _ in range(j):
        location.append(int(input()))
    for num in location:
        if num < current:
            result += abs(num - current)
            current = num
        elif num >= current + m:
            result += abs(num - current - m + 1)
            current = num - m + 1
    print(result)


def q1713():
    # 후보 추천하기
    n = int(input())
    v = int(input())
    s = list(map(int, input().split()))
    frame = []
    count = []
    for i in range(v):
        if s[i] in frame:
            for j in range(len(frame)):
                if s[i] == frame[j]:
                    count[j] += 1
        else:
            if len(frame) >= n:
                for j in range(n):
                    if count[j] == min(count):
                        del frame[j]
                        del count[j]
                        break
            frame.append(s[i])
            count.append(1)
    frame.sort()
    print(' '.join(map(str, frame)))


def q1251():
    # 단어 나누기
    s = list(input())
    temp = []
    result = []

    for i in range(1, len(s) - 1):
        for j in range(i + 1, len(s)):
            w1 = s[:i]
            w2 = s[i:j]
            w3 = s[j:]
            w1.reverse()
            w2.reverse()
            w3.reverse()
            temp.append(w1 + w2 + w3)

    for data in temp:
        result.append(''.join(data))
    print(min(result))


def q2564():
    # 경비원
    x, y = map(int, input().split())
    c = int(input())
    shop_pos = []
    distance = 0
    for _ in range(c):
        shop_pos.append(list(map(int, input().split())))
    l, d = map(int, input().split())
    for loc, dist in shop_pos:
        if l <= 2:
            if (loc == 1 and l == 1) or (loc == 2 and l == 2):
                distance += abs(d - dist)
            elif (loc == 1 and l == 2) or (loc == 2 and l == 1):
                distance += min(d + dist + y, abs(d - x) + abs(dist - x) + y)
            else:
                if l == 1:
                    if loc == 3:
                        distance += d + dist
                    if loc == 4:
                        distance += abs(d - x) + dist
                elif l == 2:
                    if loc == 3:
                        distance += d + abs(dist - y)
                    if loc == 4:
                        distance += abs(d - x) + abs(dist - y)
        elif l >= 3:
            if (loc == 3 and l == 3) or (loc == 4 and l == 4):
                distance += abs(d - dist)
            elif (loc == 3 and l == 4) or (loc == 4 and l == 3):
                distance += min(d + dist + x, abs(d - y) + abs(dist - y) + x)
            else:
                if l == 3:
                    if loc == 1:
                        distance += d + dist
                    if loc == 2:
                        distance += abs(d - y) + dist
                elif l == 4:
                    if loc == 1:
                        distance += d + abs(dist - x)
                    if loc == 2:
                        distance += abs(d - y) + abs(dist - x)
    print(distance)
q2564()