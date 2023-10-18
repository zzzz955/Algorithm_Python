import sys


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


def q4659():
    # 비밀번호 발음하기
    test_case = []
    result = []
    moeum = ['a', 'e', 'i', 'o', 'u']
    excepts = ['ee', 'oo']
    while 1:
        case = input()
        if case == 'end':
            break
        else:
            test_case.append(case)
    for password in test_case:
        test = False
        for i in moeum:
            if i in password:
                test = True
                break
        for i in range(len(password) - 2):
            if password[i] in moeum and password[i + 1] in moeum and password[i + 2] in moeum:
                test = False
                break
            if not (password[i] in moeum) and not (password[i + 1] in moeum) and not (password[i + 2] in moeum):
                test = False
                break
        for i in range(len(password) - 1):
            if password[i] == password[i + 1] and password[i] + password[i + 1] not in excepts:
                test = False
                break
        if test:
            result.append(f'<{password}> is acceptable.')
        else:
            result.append(f'<{password}> is not acceptable.')
    for answer in result:
        print(answer)


def q1205():
    # 등수 구하기
    n, new_point, p = map(int, input().split())
    if n > 0:
        current_rank = list(map(int, input().split()))
        current_rank.append(new_point)
        sorted_current_rank = sorted(current_rank, reverse=True)
        if sorted_current_rank.index(new_point) + 1 > p:
            print(-1)
        else:
            if current_rank[n - 1] >= new_point and n < p:
                print(sorted_current_rank.index(new_point) + 1)
            elif current_rank[n - 1] >= new_point and len(current_rank) >= p:
                print(-1)
            else:
                print(sorted_current_rank.index(new_point) + 1)
    else:
        print(1)


def q5671():
    # 호텔 방 번호
    while 1:
        try:
            s, l = map(int, input().split())
            count = 0
            for num in range(s, l + 1):
                string = str(num)
                lst = []
                for char in string:
                    lst.append(char)
                if len(set(lst)) == len(lst):
                    count += 1
            print(count)
        except:
            break


def q2839():
    # 설탕 배달
    n = int(input())
    d5 = n // 5
    if n == 3:
        print(1)
    elif n == 4 or n == 7:
        print(-1)
    elif n == 5 or n == 10:
        print(n // 5)
    elif n == 6 or n == 9:
        print(n // 3)
    elif n == 8:
        print(2)
    elif n > 10:
        if n % 5 == 1:
            print(d5 + 1)
        elif n % 5 == 2:
            print(d5 + 2)
        elif n % 5 == 3:
            print(d5 + 1)
        elif n % 5 == 4:
            print(d5 + 2)
        elif n % 5 == 0:
            print(d5)
        else:
            print(-1)


def q9095():
    # 1, 2, 3 더하기
    t = int(input())
    result = []
    dp = [0] * 11
    dp[1:4] = [1, 2, 4]
    for i in range(4, 11):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    for _ in range(t):
        n = int(input())
        result.append(dp[n])
    for answer in result:
        print(answer)


def q1003():
    # 피보나치 함수
    t = int(input())
    result = []
    for _ in range(t):
        n = int(input())
        dp = [0] * n
        dp[0:2] = [1, 1]
        if n == 0:
            result.append('1 0')
        elif n == 1:
            result.append('0 1')
        else:
            for i in range(2, n):
                dp[i] = dp[i - 1] + dp[i - 2]
            result.append(f'{dp[n - 2]} {dp[n - 1]}')
    for answer in result:
        print(answer)


def q1929():
    # 소수 구하기
    import sys
    m, n = map(int, sys.stdin.readline().split())
    dp = [1] * (n + 1)
    dp[0] = 0
    dp[1] = 0
    index = 2
    while index <= n // 2:
        if dp[index] == 0:
            index += 1
            continue
        else:
            index2 = 2
            while index * index2 < n + 1:
                dp[index * index2] = 0
                index2 += 1
            index += 1
    for i in range(m, n + 1):
        if dp[i]:
            sys.stdout.write(str(i) + '\n')


def q11723():
    # 집합
    import sys
    m = int(sys.stdin.readline())
    dp = [0] * 21
    for _ in range(m):
        val = sys.stdin.readline().strip()
        if val == 'all':
            dp = [1] * 21
        elif val == 'empty':
            dp = [0] * 21
        else:
            op, n = val.split()
            n = int(n)
            if op == 'add':
                dp[n] = 1
            elif op == 'remove':
                dp[n] = 0
            elif op == 'toggle':
                if dp[n]:
                    dp[n] = 0
                else:
                    dp[n] = 1
            else:
                if dp[n]:
                    print(1)
                else:
                    print(0)


def q9655():
    # 돌 게임
    n = int(input())
    if n % 2 == 0:
        print('CY')
    else:
        print('SK')


def q10431():
    # 줄세우기
    p = int(input())
    result = []
    for _ in range(p):
        lst = list(map(int, input().split()))
        lst.pop(0)
        count = 0
        for i in range(19):
            for j in range(i + 1, 20):
                if lst[i] > lst[j]:
                    lst[i], lst[j] = lst[j], lst[i]
                    count += 1
        result.append(count)
    for i, j in enumerate(result):
        print(f'{i + 1} {j}')


def q8979():
    # 올림픽
    n, k = map(int, input().split())
    dic = {}
    val = []
    for _ in range(n):
        countries = list(map(int, input().split()))
        val.append(countries[1:])
        dic[countries[0]] = countries[1:]
    rank_val = sorted(val, reverse=True)
    print(rank_val.index(dic[k]) + 1)


def q7568():
    # 덩치
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(list(map(int, input().split())))
    for i in lst:
        rank = 1
        for j in lst:
            if i[0] < j[0] and i[1] < j[1]:
                rank += 1
        print(rank, end=' ')


def q25757():
    # 임스와 함께하는 미니게임
    n, y = input().split()
    players = []
    for _ in range(int(n)):
        players.append(input())
    play = len(set(players))
    if y == 'Y':
        print(play)
    elif y == 'F':
        print(play // 2)
    else:
        print(play // 3)


def q20125():
    #쿠키의 신체 측정
    n = int(input())
    lst = []
    heart = []
    bodies = []
    for i in range(n):
        lst.append(input())
    for i in range(len(lst)):
        if lst[i].count('*') == 1:
            heart.append(i + 1)
            heart.append(lst[i].index('*'))
            break
    count = 0
    for char in lst[heart[0]][:heart[1]]:
        if char == '*':
            count += 1
    bodies.append(count)
    count = 0
    for char in lst[heart[0]][heart[1] + 1:]:
        if char == '*':
            count += 1
    bodies.append(count)
    count = 0
    for i in range(heart[0] + 1, n):
        if lst[i][heart[1]] == '*':
            count += 1
    bodies.append(count)
    count = 0
    for i in range(heart[0] + bodies[2], n):
        if lst[i][heart[1] - 1] == '*':
            count += 1
    bodies.append(count)
    count = 0
    for i in range(heart[0] + bodies[2], n):
        if lst[i][heart[1] + 1] == '*':
            count += 1
    bodies.append(count)
    heart = [i + 1 for i in heart]
    print(' '.join(map(str, heart)))
    print(' '.join(map(str, bodies)))


def q1244():
    # 스위치 켜고 끄기
    n = int(input())
    s = list(map(int, input().split()))
    dp = [0] * (n + 1)
    students = []
    for i in range(1, n + 1):
        dp[i] = s[i - 1]
    student = int(input())
    for _ in range(student):
        students.append(list(map(int, input().split())))
    while students:
        if students[0][0] == 1:
            index2 = 1
            while index2 * students[0][1] <= n:
                if dp[index2 * students[0][1]] == 0:
                    dp[index2 * students[0][1]] = 1
                else:
                    dp[index2 * students[0][1]] = 0
                index2 += 1
        if students[0][0] == 2:
            index3 = 0
            while 1:
                if index3 == 0:
                    if dp[students[0][1]] == 0:
                        dp[students[0][1]] = 1
                    else:
                        dp[students[0][1]] = 0
                try:
                    if dp[students[0][1] + index3] == dp[students[0][1] - index3] and (students[0][1] - index3) != 0:
                        if dp[students[0][1] + index3] == 0:
                            dp[students[0][1] + index3] = 1
                        else:
                            dp[students[0][1] + index3] = 0
                        if dp[students[0][1] - index3] == 0:
                            dp[students[0][1] - index3] = 1
                        else:
                            dp[students[0][1] - index3] = 0
                    else:
                        break
                except:
                    break
                index3 += 1
        students.pop(0)
    dp.pop(0)
    for i in range(1, n + 1):
        print(dp[i - 1], end=' ')
        if i % 20 == 0:
            print()


def q9017():
    # 크로스 컨트리(재채점 필요)
    t = int(input())
    case = []
    result = []
    for _ in range(t):
        n = int(input())
        temp = list(map(int, input().split()))
        for data in sorted(set(temp)):
            if temp.count(data) < 6:
                while temp.count(data) > 0:
                    temp.remove(data)
        case.append(temp)
    for data in case:
        team = {}
        count_u = []
        for i in set(data):
            team[i] = 0
        temp_team = team.copy()
        first = 0
        for i in data:
            temp_team[i] += 1
            if temp_team[i] == 5:
                first = i
                break
        point = 1
        for i in data:
            count_u.append(i)
            if count_u.count(i) <= 4:
                team[i] += point
            point += 1
        count = 0
        for p in team.values():
            if min(team.values()) == p:
                count += 1
        for t, p in team.items():
            if count >= 2:
                if p == min(team.values()) and t == first:
                    result.append(first)
                    break
            else:
                if p == min(team.values()):
                    result.append(t)
    for answer in result:
        print(answer)


def q17266():
    # 어두운 굴다리
    import math
    n = int(input())
    m = int(input())
    x = list(map(int, input().split()))
    minus = []
    if m > 1:
        for i in range(1, m):
            minus.append(math.ceil((x[i] - x[i - 1]) / 2))
        print(max(min(x), n - max(x), max(minus)))
    else:
        print(max(min(x), n - max(x)))


def q2164():
    # 카드2
    import sys
    n = int(sys.stdin.readline())
    index = 0
    while 2 ** index < n:
        index += 1
    result = 0
    for i in range(2**index - n + 1):
        result = 2**index - (2 * i)
    print(result)


def q13305():
    # 주유소
    n = int(input())
    dis = list(map(int, input().split()))
    pri = list(map(int, input().split()))
    pri[-1] = 10001
    dp = [0] * n
    dp[1] = dis[0] * pri[0]
    for i in range(1, n - 1):
        dp[i + 1] = min(dp[i] + (dis[i] * pri[i]), dp[i] + (dis[i] * pri[i - 1]))
        if dp[i] + (dis[i] * pri[i]) > dp[i] + (dis[i] * pri[i - 1]):
            pri[i] = pri[i - 1]
    print(dp[n - 1])


def q20920():
    # 영단어 암기는 괴로워
    import sys
    from collections import Counter
    n, m = map(int, sys.stdin.readline().split())
    count = Counter()

    for _ in range(n):
        sentence = sys.stdin.readline().strip()
        if len(sentence) >= m:
            count[sentence] += 1

    sorted_words = sorted(count.keys(), key=lambda x: (-count[x], -len(x), x))

    for word in sorted_words:
        sys.stdout.write(word + '\n')


def q2512():
    # 예산
    n = int(input())
    lst = list(map(int, input().split()))
    m = int(input())
    if sum(lst) <= m:
        print(max(lst))
    else:
        temp = lst.copy()
        while temp and m // len(temp) > min(temp):
            m -= temp.pop(temp.index(min(temp)))
        print(m // len(temp))


def q21921():
    # 블로그
    import sys
    m, x = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))

    prefix_sum = [0] * m
    for i in range(m):
        prefix_sum[i] = lst[i] + (prefix_sum[i - 1] if i > 0 else 0)

    max_sum = 0
    count = 0
    for i in range(m - x + 1):
        current_sum = prefix_sum[i + x - 1] - (prefix_sum[i - 1] if i > 0 else 0)
        if current_sum > max_sum:
            max_sum = current_sum
            count = 1
        elif current_sum == max_sum:
            count += 1

    if max_sum == 0:
        print('SAD')
    else:
        print(max_sum)
        print(count)


q21921()
