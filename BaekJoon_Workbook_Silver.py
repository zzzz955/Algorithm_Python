def q1010():
    # 백준 1010번 파이썬 다리 놓기
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
    # 백준 1002번 파이썬 터렛
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
    # 백준 1769번 파이썬 3의 배수
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
    # 백준 1417번 파이썬 국회의원 선거
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
    # 백준 2828번 파이썬 사과 담기 게임
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
    # 백준 1713번 파이썬 후보 추천하기
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
    # 백준 1251번 파이썬 단어 나누기
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
    # 백준 2564번 파이썬 경비원
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
    # 백준 4659번 파이썬 비밀번호 발음하기
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
    # 백준 1205번 파이썬 등수 구하기
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
    # 백준 5671번 파이썬 호텔 방 번호
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
    # 백준 2839번 파이썬 설탕 배달
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
    # 백준 9095번 파이썬 1, 2, 3 더하기
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
    # 백준 1003번 파이썬 피보나치 함수
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
    # 백준 1929번 파이썬 소수 구하기
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
    # 백준 11723번 파이썬 집합
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
    # 백준 9655번 파이썬 돌 게임
    n = int(input())
    if n % 2 == 0:
        print('CY')
    else:
        print('SK')


def q10431():
    # 백준 10431번 파이썬 줄세우기
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
    # 백준 8979번 파이썬 올림픽
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
    # 백준 7568번 파이썬 덩치
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
    # 백준 25757번 파이썬 임스와 함께하는 미니게임
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
    # 백준 20125번 파이썬 쿠키의 신체 측정
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
    # 백준 1244번 파이썬 스위치 켜고 끄기
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
    # 백준 9017번 파이썬 크로스 컨트리(재채점 필요)
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
    # 백준 17266번 파이썬 어두운 굴다리
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
    # 백준 2164번 파이썬 카드2
    import sys
    n = int(sys.stdin.readline())
    index = 0
    while 2 ** index < n:
        index += 1
    result = 0
    for i in range(2 ** index - n + 1):
        result = 2 ** index - (2 * i)
    print(result)


def q13305():
    # 백준 13305번 파이썬 주유소
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
    # 백준 20920번 파이썬 영단어 암기는 괴로워
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
    # 백준 2512번 파이썬 예산
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
    # 백준 21921번 파이썬 블로그
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


def q1515():
    # 백준 1515번 파이썬 수 이어 쓰기
    nums = input()
    i = 0
    while 1:
        i += 1
        num = str(i)
        while len(num) > 0 and len(nums) > 0:
            if num[0] == nums[0]:
                nums = nums[1:]
            num = num[1:]
        if nums == '':
            print(i)
            break


def q19941():
    # 백준 19941번 파이썬 햄버거 분배
    import sys
    n, k = map(int, sys.stdin.readline().split())
    hp = sys.stdin.readline()
    count = 0
    for i in range(n):
        if hp[i] == 'P':
            done = False
            for j in range(k, 0, -1):
                if i - j >= 0:
                    if hp[i - j] == 'H':
                        hp = hp[:i - j] + 'X' + hp[i - j + 1:]
                        count += 1
                        done = True
                        break
            if done:
                continue
            for j in range(1, k + 1):
                if i + j < n:
                    if hp[i + j] == 'H':
                        hp = hp[:i + j] + 'X' + hp[i + j + 1:]
                        count += 1
                        break
    print(count)


def q17484():
    # 백준 17484번 파이썬 진우의 달 여행 (틀림, dfs 공부 후 재채점 필요)
    import sys
    import copy

    n, m = map(int, sys.stdin.readline().split())
    lst = []
    val = []
    for i in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        temp.insert(0, 101)
        temp.append(101)
        lst.append(temp)
    for i in range(1, m + 1):
        result = 0
        temp_lst = copy.deepcopy(lst)
        current = i
        for j in range(n):
            min_val = min(temp_lst[j][current - 1], temp_lst[j][current], temp_lst[j][current + 1])
            result += min_val
            if j + 1 < n:
                if min_val == temp_lst[j][current - 1]:
                    temp_lst[j + 1][current - 2] = 101
                    current -= 1
                elif min_val == temp_lst[j][current]:
                    temp_lst[j + 1][current] = 101
                else:
                    temp_lst[j + 1][current + 2] = 101
                    current += 1
            print(min_val)
        val.append(result)
    print(min(val))


def q2607():
    # 백준 2607번 파이썬 비슷한 단어
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(input().upper())
    length = len(lst[0])
    count = 0
    while len(lst) > 1:
        if abs(length - len(lst[1])) > 1:
            lst.pop(1)
        elif len(set(lst[0]).difference(set(lst[1]))) > 1:
            lst.pop(1)
        else:
            for t in lst[0]:
                if t in lst[1]: lst[1] = lst[1].replace(t, "", 1)
            if len(lst[1]) <= 1:
                count += 1
            lst.pop(1)
    print(count)


def q3758():
    # 백준 3758번 파이썬 KCPC
    import sys
    import collections

    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k, ids, m = map(int, sys.stdin.readline().split())
        lst = []
        order = []
        point = {}
        for _ in range(m):
            lst.append(list(map(int, sys.stdin.readline().split())))
        index = 0
        desc_lst = list(reversed(lst))
        while len(order) < n:
            if desc_lst[index][0] not in order:
                order.append(desc_lst[index][0])
            index += 1
        count = collections.Counter(item[0] for item in lst)
        lst = sorted(lst)
        index = 0
        while index < len(lst) - 1:
            if lst[index][:2] == lst[index + 1][:2]:
                max_val = max(lst[index][2], lst[index + 1][2])
                lst[index + 1][2] = max_val
                lst.pop(index)
                index -= 1
            index += 1
        while lst:
            if lst[0][0] in point:
                point[lst[0][0]] += lst[0][2]
            else:
                point[lst[0][0]] = lst[0][2]
            lst.pop(0)
        count = dict(count)
        rank = sorted(point.keys(), key=lambda x: (-point[x], count[x], list(reversed(order)).index(x)))
        for data in rank:
            if data == ids:
                print(rank.index(data) + 1)


def q20310():
    # 백준 20310번 파이썬 타노스
    s = list(input())
    count0, count1 = s.count('0') // 2, s.count('1') // 2
    index = 1
    while 1:
        if count0 == 0 and count1 == 0:
            break
        elif s[-index] == '0' and count0 > 0:
            count0 -= 1
            s.pop(-index)
            index = 1
            continue
        elif s[index - 1] == '1' and count1 > 0:
            count1 -= 1
            s.pop(index - 1)
            index = 1
            continue
        else:
            index += 1
    print(''.join(s))


def q19637():
    # 백준 19637번 파이썬 IF문 좀 대신 써줘
    import sys

    n, m = map(int, sys.stdin.readline().split())
    lst = []

    for _ in range(n):
        a, b = map(str, sys.stdin.readline().split())
        lst.append([a, int(b)])

    cps = [int(sys.stdin.readline()) for _ in range(m)]

    for cp in cps:
        start = 0
        end = n
        result = 0
        while start <= end:
            mid = (start + end) // 2
            if lst[mid][1] >= cp:
                result = mid
                end = mid - 1
            else:
                start = mid + 1
        print(lst[result][0])


def q22233():
    # 백준 22233번 파이썬 가희와 키워드
    import sys

    n, m = map(int, sys.stdin.readline().split())
    lst = set()

    for _ in range(n):
        keyword = sys.stdin.readline().strip()
        lst.add(keyword)

    for _ in range(m):
        key = list(map(str, sys.stdin.readline().rstrip().split(',')))
        for sentence in key:
            if sentence in lst:
                lst.remove(sentence)
        print(len(lst))


def q1927():
    # 백준 1927번 파이썬 최소 힙
    import sys
    import heapq

    n = int(sys.stdin.readline())
    lst = []
    for _ in range(n):
        x = int(int(sys.stdin.readline()))
        if x > 0:
            heapq.heappush(lst, x)
        else:
            if lst:
                print(heapq.heappop(lst))
            else:
                print(0)


def q20006():
    # 백준 20006번 파이썬 랭킹전 대기열
    p, m = map(int, input().split())
    room = []

    for _ in range(p):
        l, n = input().split()
        l = int(l)
        do = False
        for key in room:
            if key[0][0] - 10 <= l <= key[0][0] + 10 and len(key) < m:
                key.append([l, n])
                do = True
                break
        if not do:
            room.append([])
            room[-1].append([l, n])
    for key in room:
        if len(key) == m:
            key = sorted(key, key=lambda x: x[1])
            print('Started!')
            for i in key:
                print(*i)
        else:
            key = sorted(key, key=lambda x: x[1])
            print('Waiting!')
            for i in key:
                print(*i)


def q11501():
    # 백준 11501번 파이썬 주식
    import sys

    t = int(sys.stdin.readline())
    result = []
    for _ in range(t):
        n = int(input())
        lst = list(map(int, sys.stdin.readline().split()))
        prizes = 0
        max_val = 0

        for i in range(n - 1, -1, -1):
            if lst[i] > max_val:
                max_val = lst[i]
            else:
                prizes += max_val - lst[i]
        result.append(prizes)
    for answer in result:
        print(answer)


def q1406():
    # 백준 1406번 파이썬 에디터
    import sys

    left = list(sys.stdin.readline().strip())
    right = []
    n = int(sys.stdin.readline())
    for _ in range(n):
        op = sys.stdin.readline()
        if op[0] == 'L' and left:
            right.append(left.pop())
        elif op[0] == 'D' and right:
            left.append(right.pop())
        elif op[0] == 'B' and left:
            left.pop()
        elif op[0] == 'P':
            left.append(op[2])
    print(''.join(left + list(reversed(right))))


def q2304():
    # 백준 2304번 파이썬 창고 다각형
    n = int(input())
    lst = []
    area = 0
    for _ in range(n):
        lst.append(list(map(int, input().split())))
    lst.sort()

    max_h = max(range(len(lst)), key=lambda x: lst[x][1])
    height = lst[0][1]
    for i in range(max_h):
        if height < lst[i + 1][1]:
            area += (lst[i + 1][0] - lst[i][0]) * height
            height = lst[i + 1][1]
        else:
            area += (lst[i + 1][0] - lst[i][0]) * height

    height = lst[-1][1]
    for i in range(-1, -(len(lst) - max_h), -1):
        if height < lst[i - 1][1]:
            area += (lst[i][0] - lst[i - 1][0]) * height
            height = lst[i - 1][1]
        else:
            area += (lst[i][0] - lst[i - 1][0]) * height
    area += lst[max_h][1]
    print(area)


def q2075():
    # 백준 2075번 파이썬 N번째 큰 수
    import heapq
    lst = []

    n = int(input())
    for _ in range(n):
        nums = list(map(int, input().split()))
        if not lst:
            for num in nums:
                heapq.heappush(lst, num)
        else:
            for num in nums:
                if lst[0] < num:
                    heapq.heappush(lst, num)
                    heapq.heappop(lst)
    print(lst[0])


def q1138():
    # 백준 1138번 파이썬 한 줄로 서기
    n = int(input())
    order = list(map(int, input().split()))
    lst = []
    while order:
        lst.insert(order[-1], len(order))
        order.pop()
    print(*lst)


def q2941():
    # 백준 2941번 파이썬 크로아티아 알파벳
    s = input()
    lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    for word in lst:
        s = s.replace(word, 'x')
    print(len(s))


def q1316():
    # 백준 1316번 파이썬 그룹 단어 체커
    t = int(input())
    result = 0
    for _ in range(t):
        s = list(input())
        lst = list(set(s))
        check = True
        for word in lst:
            start = s.index(word)
            end = len(s) - list(reversed(s)).index(word)
            while start < end:
                if s[start] != word:
                    check = False
                    break
                start += 1
        if check:
            result += 1
    print(result)


def q25206():
    # 백준 25206번 파이썬 너의 평점은
    table = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
    table_points = 0
    points = 0
    for _ in range(20):
        lst = list(input().split())
        if lst[2] == 'P':
            continue
        else:
            table_points += float(lst[1]) * float(table[lst[2]])
            points += float(lst[1])
    print(table_points / points)


def q2563():
    # 백준 2563번 파이썬 색종이
    dp = [[0] * 100 for _ in range(100)]
    result = 0
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        for i in range(a, a + 10):
            if i > 100:
                continue
            else:
                for j in range(b, b + 10):
                    if j > 100:
                        continue
                    else:
                        dp[i][j] = 1
    for i in range(100):
        result += sum(dp[i])
    print(result)


def q1193():
    # 백준 1193번 파이썬 분수찾기
    x = int(input())
    dp = [0] * 4500
    dp[1] = 1
    index = 0
    for i in range(2, 4501):
        dp[i] = dp[i - 1] + i
        if dp[i - 1] >= x:
            index = i - 2
            break
    if index % 2 == 1:
        first = x - dp[index]
        last = dp[index + 1] - x + 1
        print(str(first) + '/' + str(last))
    else:
        first = dp[index + 1] - x + 1
        last = x - dp[index]
        print(str(first) + '/' + str(last))


def q24313():
    # 백준 24313번 파이썬 알고리즘 수업 - 점근적 표기 1
    a1, a2 = map(int, input().split())
    c = int(input())
    n0 = int(input())
    if a1 <= c and a1 * n0 + a2 <= c * n0:
        print(1)
    else:
        print(0)


def q1018():
    # 백준 1018번 파이썬 체스판 다시 칠하기
    n, m = map(int, input().split())
    lst = []
    result = []
    for _ in range(n):
        lst.append(list(input()))
    for i in range(n - 7):
        for j in range(m - 7):
            w = 0
            b = 0
            for k in range(i, i + 8):
                for l in range(j, j + 8):
                    if (k + l) % 2 == 0:
                        if lst[k][l] != 'W':
                            w += 1
                        if lst[k][l] != 'B':
                            b += 1
                    else:
                        if lst[k][l] != 'B':
                            w += 1
                        if lst[k][l] != 'W':
                            b += 1
            result.append(min(w, b))
    print(min(result))


def q1436():
    # 백준 1436번 파이썬 영화감독 숌
    n = int(input())
    find = 666
    count = 0
    while 1:
        if '666' in str(find):
            count += 1
        if count == n:
            print(find)
            break
        find += 1


def q2751():
    # 백준 2751번 파이썬 수 정렬하기 2
    import sys

    n = int(sys.stdin.readline())
    lst = []
    for _ in range(n):
        lst.append(int(sys.stdin.readline()))
    lst.sort()
    for num in lst:
        print(num)


def q1427():
    # 백준 1427번 파이썬 소트인사이드
    n = list(input())
    n.sort(reverse=True)
    result = ''
    for num in n:
        result += num
    print(result)


def q11650():
    # 백준 11650번 파이썬 좌표 정렬하기
    n = int(input())
    xy = []
    for _ in range(n):
        x, y = map(int, input().split())
        xy.append([x, y])
    xy.sort()
    for i in xy:
        print(*i)


def q11651():
    # 백준 11651번 파이썬 좌표 정렬하기 2
    n = int(input())
    xy = []
    for _ in range(n):
        x, y = map(int, input().split())
        xy.append([y, x])
    xy.sort()
    for i in range(n):
        print(xy[i][1], xy[i][0])


def q1181():
    # 백준 1181번 파이썬 단어 정렬
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(input())
    lst = list(set(lst))
    lst.sort()
    lst.sort(key=lambda x: len(x))
    for s in lst:
        print(s)


def q10814():
    # 백준 10814번 파이썬 나이순 정렬
    n = int(input())
    lst = []
    for _ in range(n):
        y, n = input().split()
        lst.append([int(y), n])
    lst.sort(key=lambda x: x[0])
    for s in lst:
        print(*s)


def q18870():
    # 백준 18870번 파이썬 좌표 압축
    n = int(input())
    lst = list(map(int, input().split()))
    temp = sorted(set(lst))
    dic = {}
    for i in range(len(temp)):
        dic[temp[i]] = i
    for s in lst:
        print(dic[s], end=' ')


def q10815():
    # 백준 10815번 파이썬 숫자 카드
    n = int(input())
    lst1 = list(map(int, input().split()))
    m = int(input())
    lst2 = list(map(int, input().split()))
    dic = {}
    for i in lst1:
        dic[i] = 1
    for j in lst2:
        if j in dic.keys():
            print(1, end=' ')
        else:
            print(0, end=' ')


def q14425():
    # 백준 14425번 파이썬 문자열 집합
    n, m = map(int, input().split())
    lst = []
    for _ in range(n):
        lst.append(input())
    lst2 = []
    for _ in range(m):
        lst2.append(input())
    result = 0
    for s in lst2:
        if s in lst:
            result += 1
    print(result)


def q7785():
    # 백준 7785번 파이썬 회사에 있는 사람
    n = int(input())
    dic = {}
    for _ in range(n):
        a, b = input().split()
        if a not in dic.keys():
            dic[a] = 'enter'
        else:
            dic.pop(a)
    lst = sorted(dic.keys(), reverse=True)
    for name in lst:
        print(name)


def q1620():
    # 백준 1620번 파이썬 나는야 포켓몬 마스터 이다솜
    import sys

    n, m = map(int, sys.stdin.readline().split())
    dic1 = {}
    dic2 = {}
    for index in range(n):
        s = sys.stdin.readline().rstrip()
        dic1[s] = str(index + 1)
        dic1[str(index + 1)] = s
    for _ in range(m):
        a = sys.stdin.readline().rstrip()
        if a in dic1.keys():
            print(dic1[a])
        else:
            print(dic2[a])


def q10816():
    # 백준 10816번 파이썬 숫자 카드 2
    n = int(input())
    lst = list(map(int, input().split()))
    dic = {}
    for num in lst:
        if num in dic.keys():
            dic[num] += 1
        else:
            dic[num] = 1
    m = int(input())
    lst = list(map(int, input().split()))
    for num in lst:
        if num in dic.keys():
            print(dic[num], end=' ')
        else:
            print(0, end=' ')


def q1764():
    # 백준 1764번 파이썬 듣보잡
    import sys

    n, m = map(int, sys.stdin.readline().split())
    dic1 = {}
    for _ in range(n):
        s = sys.stdin.readline().rstrip()
        dic1[s] = 1
    for _ in range(m):
        a = sys.stdin.readline().rstrip()
        if a in dic1.keys():
            dic1[a] = 0
    print(list(dic1.values()).count(0))
    lst = []
    for key, val in dic1.items():
        if val == 0:
            lst.append(key)
    lst.sort()
    for name in lst:
        print(name)


def q1269():
    # 백준 1269번 파이썬 대칭 차집합
    import sys

    n, m = map(int, sys.stdin.readline().split())
    dic1 = {}
    lst1 = list(map(int, sys.stdin.readline().split()))
    lst2 = list(map(int, sys.stdin.readline().split()))
    for num in lst1:
        dic1[num] = 1
    for num in lst2:
        if num in dic1.keys():
            dic1[num] = 0
        else:
            dic1[num] = 1
    print(sum(list(dic1.values())))


def q11478():
    # 백준 11478번 파이썬 서로 다른 부분 문자열의 개수
    s = input()
    lst = []
    length = len(s)
    slices = 1
    while slices <= length:
        index = 0
        while 1:
            if index + slices > length:
                break
            else:
                lst.append(s[index:index + slices])
            index += 1
        slices += 1
    print(len(list(set(lst))))


def q13241():
    # 백준 13241번 파이썬 최소공배수
    import math

    a, b = map(int, input().split())
    gcd = math.gcd(a, b)
    print((a * b) // gcd)


def q1735():
    # 백준 1735번 파이썬 분수 합
    import math

    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())
    lcm = math.lcm(b1, b2)
    result = (a1 * lcm // b1) + (a2 * lcm // b2)
    gcd = math.gcd(result, lcm)
    print(result // gcd, lcm // gcd)


def q2485():
    # 백준 2485번 파이썬 가로수
    import math, sys

    n = int(input())
    first = int(input())
    gcd = 1000000000
    lst = []
    for _ in range(n - 1):
        num = int(sys.stdin.readline())
        lst.append(num - first)
    for i in range(1, n - 1):
        gcd = min(gcd, math.gcd(lst[0], lst[i]))

    print((lst[-1] // gcd) - (n - 1))


def q4134():
    # 백준 4134번 파이썬 다음 소수
    t = int(input())

    def find(x):
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return 0
        return 1

    for _ in range(t):
        n = int(input())
        while 1:
            if n == 0 or n == 1:
                print(2)
                break
            elif find(n):
                print(n)
                break
            else:
                n += 1


def q4948():
    # 백준 4948번 파이썬 베르트랑 공준
    while 1:
        n = int(input())
        if n == 0:
            break
        else:
            limit = 246912
            dp = [1] * (limit + 1)
            dp[0] = dp[1] = 0
            for i in range(2, int(limit ** 0.5) + 1):
                if dp[i]:
                    for j in range(i * i, limit + 1, i):
                        dp[j] = 0
            print(sum(dp[n + 1:2 * n + 1]))


def q17103():
    # 백준 17103번 파이썬 골드바흐 파티션

    t = int(input())
    limit = 1000000
    dp = [1] * 1000001
    dp[0] = dp[1] = 0
    for i in range(2, int(limit ** 0.5) + 1):
        if dp[i]:
            for j in range(i * i, limit + 1, i):
                dp[j] = 0
    for _ in range(t):
        result = 0
        n = int(input())
        for i in range(2, n // 2 + 1):
            if dp[i] and dp[n - i]:
                result += 1
        print(result)


def q13909():
    # 백준 13909번 파이썬 창문 닫기
    n = int(input())
    result = 0
    for _ in range(1, int(n ** 0.5) + 1):
        result += 1
    print(result)


def q28278():
    # 백준 28278번 파이썬 스택 2
    import sys

    t = int(input())
    lst = []
    for _ in range(t):
        n = sys.stdin.readline().split()
        if n[0] == '1':
            lst.append(int(n[1]))
        elif n[0] == '2':
            if lst:
                print(lst.pop(-1))
            else:
                print(-1)
        elif n[0] == '3':
            print(len(lst))
        elif n[0] == '4':
            if lst:
                print(0)
            else:
                print(1)
        else:
            if lst:
                print(lst[-1])
            else:
                print(-1)


def q10773():
    # 백준 10773번 파이썬 제로
    k = int(input())
    lst = []
    for _ in range(k):
        n = int(input())
        if n:
            lst.append(n)
        else:
            lst.pop(-1)
    print(sum(lst))


def q9012():
    # 백준 9012번 파이썬 괄호
    t = int(input())
    for _ in range(t):
        s = input()
        stack = 0
        for char in s:
            if char == '(':
                stack += 1
            else:
                stack -= 1
            if stack < 0:
                break
        if stack == 0:
            print('YES')
        else:
            print('NO')


def q4949():
    # 백준 4949번 파이썬 균형잡힌 세상
    while 1:
        s = input()
        if s == '.':
            break
        lst = []
        result = 1
        for char in s:
            if (char == ')' or char == ']') and not lst:
                result = 0
                break
            if char == '(' or char == '[':
                lst.append(char)
            if char == ')':
                if lst[-1] != '(':
                    result = 0
                    break
                else:
                    lst.pop(-1)
            if char == ']':
                if lst[-1] != '[':
                    result = 0
                    break
                else:
                    lst.pop(-1)
        if not lst and result:
            print('yes')
        else:
            print('no')


def q12789():
    # 백준 12789번 파이썬 도키도키 간식드리미
    n = int(input())
    lst = list(map(int, input().split()))
    stack = []
    current = 1
    while 1:
        if not lst:
            break
        if lst[0] == current:
            lst.pop(0)
            current += 1
            continue
        if stack:
            if stack[-1] == current:
                stack.pop(-1)
                current += 1
                continue
        stack.append(lst.pop(0))
    if stack:
        stack.reverse()
        for _ in range(len(stack)):
            if current == stack[0]:
                stack.pop(0)
                current += 1
    if not stack:
        print('Nice')
    else:
        print('Sad')


def q18258():
    # 백준 18258번 파이썬 큐 2
    import collections as q, sys

    n = int(input())
    que = q.deque()
    for _ in range(n):
        p = sys.stdin.readline().split()
        if p[0] == 'push':
            que.append(p[1])
        elif p[0] == 'pop':
            if que:
                print(que.popleft())
            else:
                print(-1)
        elif p[0] == 'size':
            print(len(que))
        elif p[0] == 'empty':
            if que:
                print(0)
            else:
                print(1)
        elif p[0] == 'front':
            if que:
                print(que[0])
            else:
                print(-1)
        else:
            if que:
                print(que[-1])
            else:
                print(-1)


def q11866():
    # 백준 11866번 파이썬 요세푸스 문제 0
    from collections import deque

    n, k = map(int, input().split())
    lst = [i for i in range(1, n + 1)]
    q = deque(lst)
    result = []
    while q:
        for _ in range(k - 1):
            q.append(q.popleft())
        result.append(q.popleft())
    print('<', end='')
    print(', '.join(map(str, result)), end='')
    print('>')


def q28279():
    # 백준 28279번 파이썬 덱 2
    import collections, sys

    n = int(input())
    q = collections.deque()
    for _ in range(n):
        order = sys.stdin.readline().split()
        if order[0] == '1':
            q.appendleft(order[1])
        elif order[0] == '2':
            q.append(order[1])
        elif order[0] == '3':
            if q:
                print(q.popleft())
            else:
                print(-1)
        elif order[0] == '4':
            if q:
                print(q.pop())
            else:
                print(-1)
        elif order[0] == '5':
            print(len(q))
        elif order[0] == '6':
            if q:
                print(0)
            else:
                print(1)
        elif order[0] == '7':
            if q:
                print(q[0])
            else:
                print(-1)
        elif order[0] == '8':
            if q:
                print(q[-1])
            else:
                print(-1)


def q2346():
    # 백준 2346번 파이썬 풍선 터뜨리기
    import collections
    n = int(input())
    lst = list(map(int, input().split()))
    q = collections.deque()
    for i in range(1, n + 1):
        q.append(i)
    for _ in range(n):
        current = q[0]
        move = lst[current - 1]
        q.remove(current)
        print(current, end=' ')
        if move < 0 and q:
            move = abs(move)
            for _ in range(move):
                q.appendleft(q.pop())
        elif move > 0 and q:
            for _ in range(move - 1):
                q.append(q.popleft())


def q24511():
    # 백준 24511번 파이썬 queuestack
    from collections import deque

    n = int(input())
    qs = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    m = int(input())
    c = list(map(int, input().split()))
    q = deque()
    for i in range(n):
        if qs[i] == 0:
            q.append(lst[i])
    for num in c:
        if q:
            print(q.pop(), end=' ')
            q.appendleft(num)
        else:
            print(num, end=' ')


def q25192():
    # 백준 25192번 파이썬 인사성 밝은 곰곰이
    n = int(input())
    dic = {}
    result = 0
    for _ in range(n):
        s = input()
        if s == 'ENTER':
            result += len(dic)
            dic.clear()
        else:
            dic[s] = 1
    result += len(dic)
    print(result)


def q26069():
    # 백준 26069번 파이썬 붙임성 좋은 총총이
    n = int(input())
    dic = {'ChongChong': 1}
    for _ in range(n):
        one, two = input().split()
        if one not in dic.keys():
            dic[one] = 0
        if two not in dic.keys():
            dic[two] = 0
        if not dic[one] and not dic[two]:
            continue
        else:
            dic[one], dic[two] = 1, 1
    print(sum(dic.values()))


def q2108():
    # 백준 2108번 파이썬 통계학
    import sys

    n = int(input())
    lst = []
    dic = {}
    result = 0
    for _ in range(n):
        num = int(sys.stdin.readline())
        result += num
        lst.append(num)
        if num in dic.keys():
            dic[num] += 1
        else:
            dic[num] = 1
    lst.sort()
    many = max(dic.values())
    temps = []
    for key, item in dic.items():
        if item == many:
            temps.append(key)
    temps.sort()
    print(round(result / n))
    print(lst[n // 2])
    print(temps[1] if len(temps) > 1 else temps[0])
    print(lst[-1] - lst[0])


def q4779():
    # 백준 4779번 파이썬 칸토어 집합
    def cantor(start, depth):
        if depth == 1:
            return
        for i in range(start + depth // 3, start + (depth // 3 * 2)):
            lst[i] = ' '
        cantor(start, depth // 3)
        cantor(start + (depth // 3 * 2), depth // 3)

    while 1:
        try:
            n = int(input())
            lst = ['-'] * (3 ** n)
            cantor(0, 3 ** n)
            print(''.join(lst))
        except:
            break


def q15649():
    # 백준 15649번 파이썬 N과 M (1)
    n, m = map(int, input().split())

    def result(N, M, lst=[]):
        if M == 0:
            print(" ".join(map(str, lst)))
            return

        for i in range(1, N + 1):
            if i not in lst:
                lst.append(i)
                result(N, M - 1, lst)
                lst.pop()

    result(n, m)


def q15650():
    # 백준 15650번 파이썬 N과 M (2)
    n, m = map(int, input().split())

    def result(N, M, lst=[], start=1):
        if len(lst) == M:
            print(" ".join(map(str, lst)))
            return

        for i in range(start, N + 1):
            if i not in lst:
                lst.append(i)
                result(N, M, lst, i)
                lst.pop()

    result(n, m)


def q15651():
    # 백준 15651번 파이썬 N과 M (3)
    n, m = map(int, input().split())

    def result(N, M, lst=[]):
        if M == 0:
            print(" ".join(map(str, lst)))
            return

        for i in range(1, N + 1):
            lst.append(i)
            result(N, M - 1, lst)
            lst.pop()

    result(n, m)


def q15652():
    # 백준 15652번 파이썬 N과 M (4)
    n, m = map(int, input().split())

    def result(N, M, lst=[], start=1):
        if len(lst) == M:
            print(" ".join(map(str, lst)))
            return

        for i in range(start, N + 1):
            lst.append(i)
            result(N, M, lst, i)
            lst.pop()

    result(n, m)


def q2579():
    # 백준 2579번 파이썬 계단 오르기
    n = int(input())
    lst = [0] * 301
    for i in range(1, n + 1):
        lst[i] = int(input())
    dp = [0] * 301
    dp[1] = lst[1]
    dp[2] = lst[1] + lst[2]
    dp[3] = max(lst[1] + lst[3], lst[2] + lst[3])
    for i in range(4, n + 1):
        dp[i] = max(dp[i - 3] + lst[i - 1] + lst[i], dp[i - 2] + lst[i])
    print(dp[n])


def q11659():
    # 백준 11659번 파이썬 구간 합 구하기 4
    import sys

    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.insert(0, 0)
    dp = [0] * 100001
    for i in range(1, n + 1):
        dp[i] = lst[i] + dp[i - 1]
    for _ in range(m):
        id1, id2 = map(int, sys.stdin.readline().split())
        print(dp[id2] - dp[id1 - 1])


def q2559():
    # 백준 2559번 파이썬 수열
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    result = -10000000
    sum_val = 0
    index = 0
    for i in range(n):
        sum_val += lst[i]
        if i >= m - 1:
            result = max(sum_val, result)
            sum_val -= lst[index]
            index += 1
    print(result)


def q16139():
    # 백준 16139번 파이썬 인간-컴퓨터 상호작용
    import sys

    s = input()
    n = int(input())
    dp = [[0] * 200001 for _ in range(27)]
    for i in range(26):
        count = 0
        for j in range(len(s)):
            if s[j] == chr(i + 97):
                count += 1
            dp[i][j] = count
    for _ in range(n):
        a, start, end = sys.stdin.readline().split()
        start, end = int(start), int(end)
        print(dp[ord(a) - 97][end] - dp[ord(a) - 97][start - 1])


def q11047():
    # 백준 11047번 파이썬 동전 0
    n, k = map(int, input().split())
    lst = []
    for _ in range(n):
        lst.append(int(input()))
    lst.sort(reverse=True)
    count = 0
    for num in lst:
        count += k // num
        k %= num
    print(count)


def q1931():
    # 백준 1931번 파이썬 회의실 배정
    import sys

    n = int(input())
    lst = []
    for _ in range(n):
        s, e = map(int, sys.stdin.readline().split())
        lst.append((s, e))
    lst.sort(key=lambda x: (x[1], x[0]))
    count = 1
    end = lst[0][1]
    for i in range(n - 1):
        if end <= lst[i + 1][0]:
            end = lst[i + 1][1]
            count += 1
    print(count)


def q11399():
    # 백준 11399번 파이썬 ATM
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    current = 0
    result = 0
    for num in lst:
        current += num
        result += current
    print(result)


def q1541():
    # 백준 1541번 파이썬 잃어버린 괄호
    s = input()
    s += '+'
    lst = []
    index1 = 0
    index2 = 0
    minus = False
    for i in range(len(s)):
        if s[i] == '+':
            index2 = i
            if minus:
                lst.append(-int(s[index1:index2]))
            else:
                lst.append(int(s[index1:index2]))
            index1 = i + 1
        elif s[i] == '-':
            index2 = i
            if minus:
                lst.append(-int(s[index1:index2]))
            else:
                lst.append(int(s[index1:index2]))
            index1 = i + 1
            minus = True
    print(sum(lst))


def q1920():
    # 백준 1920번 파이썬 수 찾기
    n = int(input())
    lst1 = list(map(int, input().split()))
    m = int(input())
    lst2 = list(map(int, input().split()))
    length = len(lst1)
    lst1.sort()
    for num in lst2:
        low = 0
        high = length - 1
        temp = lst1
        isin = False
        while low <= high:
            mid = (low + high) // 2
            if temp[mid] == num:
                isin = True
                break
            elif temp[mid] < num:
                low = mid + 1
            else:
                high = mid - 1
        if isin:
            print(1)
        else:
            print(0)


def q1654():
    # 백준 1654번 파이썬 랜선 자르기
    import sys

    k, n = map(int, input().split())
    lst = []
    for _ in range(k):
        lst.append(int(sys.stdin.readline()))
    start, end = 1, max(lst)
    while start <= end:
        mid = (start + end) // 2
        lan = 0
        for num in lst:
            lan += num // mid
        if lan >= n:
            start = mid + 1
        else:
            end = mid - 1
    print(end)


def q2805():
    # 백준 2805번 파이썬 나무 자르기
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    start, end = 1, max(lst)
    while start <= end:
        mid = (start + end) // 2
        height = 0
        for num in lst:
            if num > mid:
                height += num - mid
        if height >= m:
            start = mid + 1
        else:
            end = mid - 1
    print(end)


def q11660():
    # 백준 11660번 파이썬 구간 합 구하기 5
    import sys

    n, m = map(int, input().split())
    lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + lst[i - 1][j - 1]
    for _ in range(m):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        print(dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1])


def q14916():
    # 백준 14916번 파이썬 거스름돈
    n = int(input())
    result = 0
    if n // 5:
        if n % 5 % 2:
            result += (n // 5) - 1
            n = n % 5 + 5
        else:
            result += n // 5
            n = n % 5
    if n // 2:
        result += n // 2
        n %= 2
    if n:
        print(-1)
    else:
        print(result)


def q9625():
    # 백준 9625번 파이썬 BABBA
    k = int(input())
    dp = [0] * 46
    dp[1] = 1
    for i in range(2, 46):
        dp[i] = dp[i - 2] + dp[i - 1]
    print(dp[k - 1], dp[k])


def q10826():
    # 백준 10826번 파이썬 피보나치 수 4
    n = int(input())
    dp = [0] * 10001
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
    print(dp[n])


def q13301():
    # 백준 13301번 파이썬 타일 장식물
    n = int(input())
    dp = [1] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
    dp2 = [4] * (n + 1)
    for i in range(2, n + 1):
        dp2[i] = dp2[i - 1] + (dp[i - 1] * 2)
    print(dp2[n])


def q16395():
    # 백준 16395번 파이썬 파스칼의 삼각형
    n, k = map(int, input().split())
    nf = 1
    kf = 1
    nkf = 1
    for i in range(1, n):
        nf *= i
    for i in range(1, k):
        kf *= i
    for i in range(1, n - k + 1):
        nkf *= i
    print(nf // kf // nkf)


def q15312():
    # 백준 15312번 파이썬 이름 궁합
    a = input()
    b = input()
    name = []
    alpha = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
    for i in range(len(a)):
        name.append(a[i])
        name.append(b[i])
    for i in range(len(name)):
        name[i] = alpha[ord(name[i]) - 65]
    while len(name) > 2:
        temp = []
        for i in range(len(name) - 1):
            sum_val = sum(name[i:i + 2])
            if sum_val >= 10:
                sum_val %= 10
            temp.append(sum_val)
        name = temp
    print(''.join(map(str, name)))


def q14606():
    # 백준 14606번 파이썬 피자 (Small)
    n = int(input())

    dp = [0] * (n + 1)
    dp[1] = 0
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + (i // 2)
    print(dp[n] + dp[n - 1])


def q14607():
    # 백준 14607번 파이썬 피자 (Large)
    n = int(input())
    print(n * (n - 1) // 2)


def q9656():
    # 백준 9656번 파이썬 돌 게임 2
    n = int(input())
    if n % 2 == 1:
        print('CY')
    else:
        print('SK')


def q19947():
    # 백준 19947번 파이썬 투자의 귀재 배주형
    h, y = map(int, input().split())
    dp = [0 * i for i in range(11)]
    dp[0] = h
    dp[1] = int(h * 1.05)
    dp[2] = int(dp[1] * 1.05)
    dp[3] = int(h * 1.20)
    dp[4] = int(dp[1] * 1.20)
    for i in range(5, y + 1):
        dp[i] = int(max(dp[i - 5] * 1.35, dp[i - 3] * 1.20, dp[i - 1] * 1.05))
    print(dp[y])


def q25644():
    # 백준 25644번 파이썬 최대 상승
    n = int(input())
    lst = list(map(int, input().split()))
    lst.reverse()
    dp = [0] * (n + 1)
    max_val = lst[0]
    for i in range(1, len(lst)):
        dp[i] = max_val - lst[i]
        max_val = max(max_val, lst[i])
    print(max(dp))


def q2491():
    # 백준 2491번 파이썬 수열
    n = int(input())
    lst = list(map(int, input().split()))
    dp1 = [1] * (n + 1)
    dp2 = [1] * (n + 1)
    for i in range(1, n):
        if lst[i - 1] <= lst[i]:
            dp1[i] = dp1[i - 1] + 1
        else:
            dp1[i] = 1
        if lst[i - 1] >= lst[i]:
            dp2[i] = dp2[i - 1] + 1
        else:
            dp2[i] = 1
    print(max(max(dp1), max(dp2)))


def q2670():
    # 백준 2670번 파이썬 연속부분최대곱
    import sys

    n = int(input())
    lst = [float(input()) for _ in range(n)]
    dp = [1] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1] * lst[i - 1], lst[i - 1])
    dp[0] = 0
    print(f'{max(dp):.3f}')


def q10211():
    # 백준 10211번 파이썬 Maximum Subarray
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = list(map(int, input().split()))
        dp = [0] * (n + 1)
        if max(lst) < 0:
            print(max(lst))
            continue
        for i in range(1, n + 1):
            dp[i] = max(dp[i - 1] + lst[i - 1], 0)
        print(max(dp))


def q13699():
    # 백준 13699번 파이썬 점화식
    n = int(input())
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]
    print(dp[n])


def q15624():
    # 백준 15624번 파이썬 피보나치 수 7
    n = int(input())
    dp = [0] * 1000001
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 1000000007
    print(dp[n])


def q14495():
    # 백준 14495번 파이썬 피보나치 비스무리한 수열
    n = int(input())
    dp = [0] * 117
    dp[1] = dp[2] = dp[3] = 1
    for i in range(4, n + 1):
        dp[i] = dp[i - 3] + dp[i - 1]
    print(dp[n])


def q15489():
    # 백준 15489번 파이썬 파스칼 삼각형
    r, c, w = map(int, input().split())
    dp = [[1] * 31 for _ in range(31)]
    for i in range(1, 31):
        for j in range(1, 32 - i):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    result = 0
    for i in range(w):
        for j in range(w - i):
            result += dp[r - c + i][j + c - 1]
    print(result)


def q25214():
    # 백준 25214번 파이썬 크림 파스타
    n = int(input())
    lst = list(map(int, input().split()))
    dp = [0] * (n + 1)
    min_val = 1000000000
    for i in range(1, n + 1):
        min_val = min(min_val, lst[i - 1])
        dp[i] = max(lst[i - 1] - min_val, dp[i - 1])
    dp.pop(0)
    print(*dp)


def q24417():
    # 백준 24417번 파이썬 알고리즘 수업 - 피보나치 수 2
    n = int(input())
    x, y = 1, 1
    for i in range(n - 2):
        y, x = ((x + y) % 1000000007), y
    print(y, n - 2)


def q2161():
    # 백준 2161번 파이썬 카드1
    import collections

    n = int(input())
    deq = collections.deque()
    for i in range(n, 0, -1):
        deq.append(i)
    for _ in range(n):
        print(deq.pop(), end=' ')
        if deq:
            deq.appendleft(deq.pop())


def q4158():
    # 백준 4158번 파이썬 CD
    import sys

    while 1:
        n, m = map(int, sys.stdin.readline().split())
        if n == m == 0:
            break
        dic = {}
        for _ in range(n):
            dic[int(sys.stdin.readline())] = 0
        for _ in range(m):
            num = int(sys.stdin.readline())
            if num in dic.keys():
                dic[num] += 1
        result = 0
        for val in dic.values():
            if val == 1:
                result += 1
        print(result)


def q23253():
    # 백준 23253번 파이썬 자료구조는 정말 최고야
    import sys

    n, m = map(int, sys.stdin.readline().split())
    result = 1
    for _ in range(m):
        k = int(sys.stdin.readline())
        lst = list(map(int, sys.stdin.readline().split()))
        if result:
            for i in range(k - 1):
                if lst[i] < lst[i + 1]:
                    result = 0
                    break
        else:
            break
    print('Yes' if result else 'No')


def q27964():
    # 백준 27964번 파이썬 콰트로치즈피자
    n = int(input())
    lst = input().split()
    dic = {}
    for name in lst:
        length = len(name)
        if length >= 6 and name[length - 6:length] == 'Cheese':
            if name not in dic.keys():
                dic[name] = 1
    print('yummy' if sum(dic.values()) >= 4 else 'sad')


def q25497():
    # 백준 25497번 파이썬 기술 연계마스터 임스
    n = int(input())
    skills = input()
    result = 0
    l_count = 0
    s_count = 0
    for skill in skills:
        if skill == 'L':
            l_count += 1
        elif skill == 'S':
            s_count += 1
        elif skill == 'R':
            if l_count:
                l_count -= 1
                result += 1
            else:
                break
        elif skill == 'K':
            if s_count:
                s_count -= 1
                result += 1
            else:
                break
        else:
            result += 1
    print(result)


def q25631():
    # 백준 25631번 파이썬 마트료시카 합치기
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    dic = {}
    for num in lst:
        if num in dic.keys():
            dic[num] += 1
        else:
            dic[num] = 1
    print(max(dic.values()))
    '''for num in lst:
        for key in dic.keys():
            if dic[key] and num < key:
                dic[key] -= 1
                break
    print(sum(dic.values()))'''


def q9733():
    # 백준 9733번 파이썬 꿀벌
    import sys

    lines = sys.stdin.readlines()
    length = 0
    dic = {'Re': 0, 'Pt': 0, 'Cc': 0, 'Ea': 0, 'Tb': 0, 'Cm': 0, 'Ex': 0}
    for line in lines:
        lst = line.split()
        for work in lst:
            if work in dic.keys():
                dic[work] += 1
            length += 1
    for key, val in dic.items():
        print(f'{key} {val} {(val / length):.2f}')
    print(f'Total {length} 1.00')


def q25325():
    # 백준 25325번 파이썬 학생 인기도 측정
    n = int(input())
    students = input().split()
    dic = {}
    for student in students:
        dic[student] = 0
    for _ in range(n):
        lst = input().split()
        for i in lst:
            dic[i] += 1
    keys = sorted(dic.items(), key=lambda x: x[0])
    keys = sorted(keys, key=lambda x: x[1], reverse=True)
    for name, num in keys:
        print(name, num)


def q28445():
    # 백준 28445번 파이썬 알록달록 앵무새
    dad = input().split()
    mom = input().split()
    colors = sorted(set(dad + mom))
    for i in colors:
        for j in colors:
            print(i, j)


def q26042():
    # 백준 26042번 파이썬 식당 입구 대기 줄
    import sys

    n = int(sys.stdin.readline())
    lst = []
    count = 0
    for _ in range(n):
        temp = sys.stdin.readline().split()
        if temp[0] == '1':
            count += 1
            lst.append((count, int(temp[1])))
        else:
            count -= 1
            lst.append((count, lst[-1][1]))
    lst.sort(key=lambda x: (-x[0], x[1]))
    print(*lst[0])


def q29723():
    # 백준 29723번 파이썬 브실이의 입시전략
    import sys

    n, m, k = map(int, sys.stdin.readline().split())
    dic = {}
    for _ in range(n):
        s, p = sys.stdin.readline().split()
        dic[s] = int(p)
    lst = []
    for _ in range(k):
        lst.append(sys.stdin.readline().rstrip())
    point = 0
    for subject in lst:
        point += dic.pop(subject)
    asc, desc = sorted(dic.values()), sorted(dic.values(), reverse=True)
    min_point, max_point = point, point
    for i in range(m - k):
        min_point += asc[i]
        max_point += desc[i]
    print(min_point, max_point)


def q25584():
    # 백준 25584번 파이썬 근무 지옥에 빠진 푸앙이 (Large)
    import sys

    n = int(sys.stdin.readline().rstrip())
    dic = {}
    lst = [4, 6, 4, 10]
    for _ in range(n):
        for time in lst:
            workers = sys.stdin.readline().split()
            for worker in workers:
                if worker != '-':
                    if worker in dic.keys():
                        dic[worker] += time
                    else:
                        dic[worker] = time
    if dic:
        print('Yes' if max(dic.values()) - min(dic.values()) <= 12 else 'No')
    else:
        print('Yes')


def q10828():
    # 백준 10828번 파이썬 스택
    import sys

    n = int(sys.stdin.readline())
    lst = []
    for _ in range(n):
        order = sys.stdin.readline().split()
        if order[0] == 'push':
            lst.append(int(order[1]))
        if order[0] == 'pop':
            print(lst.pop() if lst else -1)
        if order[0] == 'size':
            print(len(lst))
        if order[0] == 'empty':
            print(0 if lst else 1)
        if order[0] == 'top':
            print(lst[-1] if lst else -1)


def q10845():
    # 백준 10845번 파이썬 큐
    import sys, queue
    n = int(sys.stdin.readline())
    que = queue.Queue()

    for _ in range(n):
        order = sys.stdin.readline().split()
        if order[0] == 'push':
            que.put(int(order[1]))
        if order[0] == 'pop':
            print(-1 if que.empty() else que.get())
        if order[0] == 'size':
            print(que.qsize())
        if order[0] == 'empty':
            print(1 if que.empty() else 0)
        if order[0] == 'front':
            print(-1 if que.empty() else que.queue[0])
        if order[0] == 'back':
            print(-1 if que.empty() else que.queue[-1])


def q10866():
    # 백준 10866번 파이썬 덱
    import sys, collections
    n = int(sys.stdin.readline())
    deq = collections.deque()

    for _ in range(n):
        order = sys.stdin.readline().split()
        if order[0] == 'push_front':
            deq.appendleft(int(order[1]))
        if order[0] == 'push_back':
            deq.append(int(order[1]))
        if order[0] == 'pop_front':
            print(deq.popleft() if deq else -1)
        if order[0] == 'pop_back':
            print(deq.pop() if deq else -1)
        if order[0] == 'size':
            print(len(deq))
        if order[0] == 'empty':
            print(0 if deq else 1)
        if order[0] == 'front':
            print(deq[0] if deq else -1)
        if order[0] == 'back':
            print(deq[-1] if deq else -1)


def q1158():
    # 백준 1158번 파이썬 요세푸스 문제
    import collections

    n, k = map(int, input().split())
    deq = collections.deque()
    for i in range(1, n + 1):
        deq.append(i)
    result = []
    while deq:
        for _ in range(k):
            deq.append(deq.popleft())
        result.append(str(deq.pop()))
    print('<' + ', '.join(result) + '>')


def q17219():
    # 백준 17219번 파이썬 비밀번호 찾기
    import sys

    n, m = map(int, sys.stdin.readline().split())
    dic = {}
    for _ in range(n):
        s, p = sys.stdin.readline().split()
        dic[s] = p
    for _ in range(m):
        s = sys.stdin.readline().rstrip()
        print(dic[s])


def q1302():
    # 백준 1302번 파이썬 베스트셀러
    import sys

    n = int(sys.stdin.readline())
    dic = {}
    for _ in range(n):
        book = sys.stdin.readline().rstrip()
        if book in dic.keys():
            dic[book] += 1
        else:
            dic[book] = 1
    sorted_books = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
    print(sorted_books[0][0])


def q3986():
    # 백준 3986번 파이썬 좋은 단어
    n = int(input())
    result = 0
    for _ in range(n):
        s = list(input())
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
            elif stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        if not stack:
            result += 1
    print(result)


def q11652():
    # 백준 11652번 파이썬 카드
    import sys

    n = int(sys.stdin.readline())
    dic = {}
    for _ in range(n):
        m = int(sys.stdin.readline())
        if m in dic.keys():
            dic[m] += 1
        else:
            dic[m] = 1
    result = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
    print(result[0][0])


def q2776():
    # 백준 2776번 파이썬 암기왕
    t = int(input())
    for _ in range(t):
        n = int(input())
        note1 = list(map(int, input().split()))
        m = int(input())
        note2 = list(map(int, input().split()))
        dic = {}
        for num in note1:
            dic[num] = 1
        for num in note2:
            print(dic[num] if num in dic.keys() else 0)


def q5568():
    # 백준 5568번 파이썬 카드 놓기
    n = int(input())
    k = int(input())
    lst = []
    for _ in range(n):
        lst.append(input())
    dic = {}
    if k == 2:
        for i in range(n):
            temp = lst[i]
            for j in range(n):
                if i == j:
                    continue
                dic[temp + lst[j]] = 1
    if k == 3:
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                temp = lst[i] + lst[j]
                for z in range(n):
                    if i == z or j == z:
                        continue
                    dic[temp + lst[z]] = 1
    if k == 4:
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                for z in range(n):
                    if i == z or j == z:
                        continue
                    temp = lst[i] + lst[j] + lst[z]
                    for x in range(n):
                        if i == x or j == x or z == x:
                            continue
                        dic[temp + lst[x]] = 1
    print(sum(dic.values()))


def q1822():
    # 백준 1822번 파이썬 차집합
    n, m = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    a -= b
    print(len(a))
    if a:
        a = sorted(a)
        print(*a)


def q15828():
    # 백준 15828번 파이썬 Router
    import sys, queue

    n = int(sys.stdin.readline())
    que = queue.Queue()
    while 1:
        p = int(sys.stdin.readline())
        if p == -1:
            break
        if p and que.qsize() < n:
            que.put(p)
        if p == 0:
            que.get()
    if que.empty():
        print('empty')
    else:
        for _ in range(que.qsize()):
            print(que.get(), end=' ')


def q10546():
    # 백준 10546번 파이썬 배부른 마라토너
    import sys

    n = int(sys.stdin.readline())
    dic = {}
    for _ in range(n):
        name = sys.stdin.readline().rstrip()
        if name in dic.keys():
            dic[name] += 1
        else:
            dic[name] = 1
    for _ in range(n - 1):
        name = sys.stdin.readline().rstrip()
        if name in dic.keys():
            dic[name] -= 1
    fail = sorted(dic.items(), key=lambda x: (-x[1]))
    print(fail[0][0])


def q9322():
    # 백준 9322번 파이썬 철벽 보안 알고리즘
    t = int(input())
    for _ in range(t):
        n = int(input())
        key1 = input().split()
        key2 = input().split()
        password = input().split()
        for key in key1:
            index = key2.index(key)
            key2[index], key2[key1.index(key)] = key2[key1.index(key)], key2[index]
            password[index], password[key1.index(key)] = password[key1.index(key)], password[index]
        print(*password)


def q1544():
    # 백준 1544번 파이썬 사이클 단어
    import sys

    n = int(sys.stdin.readline())
    dic = {}
    for _ in range(n):
        s = sys.stdin.readline().rstrip()
        correct = False
        for _ in range(len(s)):
            if s in dic.keys():
                correct = True
                break
            else:
                s = s[1:] + s[0]
        if correct:
            dic[s] += 1
        else:
            dic[s] = 1
    print(len(dic))


def q20551():
    # 백준 20551번 파이썬 Sort 마스터 배지훈의 후계자
    import sys

    def devine(l, c):
        left, right = 0, len(l) - 1

        while left <= right:
            mid = (left + right) // 2
            if l[mid] == c and l[mid - 1] != c:
                return mid
            elif l[mid] == c and l[mid - 1] == c and mid == 0:
                return mid
            elif l[mid] < c:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    n, m = map(int, sys.stdin.readline().split())
    lst = []
    for _ in range(n):
        lst.append(int(sys.stdin.readline()))
    lst.sort()
    for _ in range(m):
        num = int(sys.stdin.readline())
        print(devine(lst, num))


def q16499():
    # 백준 16499번 파이썬 동일한 단어 그룹화하기
    import sys

    n = int(sys.stdin.readline())
    lst = []
    for _ in range(n):
        s = list(sys.stdin.readline().rstrip())
        s.sort()
        if s not in lst:
            lst.append(s)
    print(len(lst))


def q11507():
    # 백준 11507번 파이썬 카드셋트
    s = input()
    greska = False
    dic = {'P': [], 'K': [], 'H': [], 'T': []}
    for i in range(0, len(s), 3):
        if s[i + 1:i + 3] in dic[s[i]]:
            greska = True
            break
        else:
            dic[s[i]].append(s[i + 1:i + 3])
    if greska:
        print('GRESKA')
    else:
        for val in dic.values():
            print(13 - len(val), end=' ')


def q1835():
    # 백준 1835번 파이썬 카드
    import collections

    deq = collections.deque()
    n = int(input())
    deq.append(n)
    for i in range(n - 1, 0, -1):
        deq.appendleft(i)
        for j in range(i):
            deq.appendleft(deq.pop())
    print(*deq)


def q2358():
    # 백준 2358번 파이썬 평행선
    import sys

    n = int(sys.stdin.readline())
    dic_x = {}
    dic_y = {}
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        if x in dic_x:
            dic_x[x] = True
        else:
            dic_x[x] = False
        if y in dic_y:
            dic_y[y] = True
        else:
            dic_y[y] = False
    result = 0
    for val in dic_x.values():
        if val:
            result += 1
    for val in dic_y.values():
        if val:
            result += 1
    print(result)


def q9575():
    # 백준 9575번 파이썬 행운의 수
    import sys

    t = int(sys.stdin.readline())
    for _ in range(t):
        an = int(sys.stdin.readline())
        a = set(map(int, sys.stdin.readline().split()))
        bn = int(sys.stdin.readline())
        b = set(map(int, sys.stdin.readline().split()))
        cn = int(sys.stdin.readline())
        c = set(map(int, sys.stdin.readline().split()))
        dic = {}
        for i in a:
            for j in b:
                for k in c:
                    chk = True
                    result = set(str(i + j + k))
                    for num in result:
                        if num == '5' or num == '8':
                            pass
                        else:
                            chk = False
                            break
                    if chk:
                        dic[str(i + j + k)] = 1
        print(sum(dic.values()))


def q14670():
    # 백준 14670번 파이썬 병약한 영정
    import sys

    n = int(sys.stdin.readline())
    dic = {}
    for _ in range(n):
        me, mn = map(int, sys.stdin.readline().split())
        dic[me] = mn
    r = int(sys.stdin.readline())
    for _ in range(r):
        lst = list(map(int, sys.stdin.readline().split()))
        result = []
        chk = True
        for i in range(1, len(lst)):
            if lst[i] in dic:
                result.append(dic[lst[i]])
            else:
                chk = False
                break
        if chk:
            print(*result)
        else:
            print('YOU DIED')


def q29754():
    # 백준 29754번 파이썬 세상에는 많은 유튜버가 있고, 그중에서 버츄얼 유튜버도 존재한다(틀렸습니다로 재채점 필요)
    import sys

    n, m = map(int, (sys.stdin.readline().split()))
    lst = []
    dic = {}
    for _ in range(n):
        name, day, st, et = sys.stdin.readline().split()
        week = (int(day) - 1) // 7
        time = (int(et[:2]) * 60 + int(et[3:])) - (int(st[:2]) * 60 + int(st[3:]))
        if name in dic:
            dic[name][week][0] += 1
            dic[name][week][1] += time
        else:
            dic[name] = [[0, 0] for _ in range(m // 7)]
            dic[name][week] = [1, time]
    for key, val in dic.items():
        chk = True
        for i in val:
            if i[0] < 5 or i[1] < 3600:
                chk = False
                break
        if chk:
            lst.append(key)
    if lst:
        for i in lst:
            print(i)
    else:
        print(-1)


def q19583():
    # 백준 19583번 파이썬 싸이버개강총회
    import sys

    def time_cal(t):
        h, m = t.split(':')
        return int(h) * 60 + int(m)

    s, e, q = sys.stdin.readline().split()
    s = time_cal(s)
    e = time_cal(e)
    q = time_cal(q)
    dic1 = {}
    dic2 = {}
    result = 0
    while 1:
        lst = sys.stdin.readline().split()
        if not lst:
            break
        time = time_cal(lst[0])
        if time <= s:
            dic1[lst[1]] = 1
        if e <= time <= q:
            dic2[lst[1]] = 1
    for key in dic1.keys():
        if key in dic2.keys():
            result += 1
    print(result)


def q14911():
    # 백준 14911번 파이썬 궁합 쌍 찾기(틀렸습니다로 재채점 필요)
    nums = set(map(int, input().split()))
    n = int(input())
    dic = set()
    for i in nums:
        if i >= n:
            break
        for j in nums:
            if i + j == n:
                if i > j:
                    dic.add((j, i))
                else:
                    dic.add((i, j))
    result = sorted(dic, key=lambda x: (x[0], x[1]))
    for i in result:
        print(*i)
    print(len(result))


def q28446():
    # 백준 28446번 파이썬 볼링공 찾아주기
    import sys

    m = int(sys.stdin.readline())
    dic = {}
    for _ in range(m):
        order = list(map(int, sys.stdin.readline().split()))
        if order[0] == 1:
            dic[order[2]] = order[1]
        else:
            print(dic[order[1]])


def q26596():
    # 백준 26596번 파이썬 황금 칵테일(틀렸습니다로 재채점 필요)
    import sys

    n = int(sys.stdin.readline())
    dic = {}
    for _ in range(n):
        name, qt = sys.stdin.readline().split()
        if name in dic:
            dic[name] += int(qt)
        else:
            dic[name] = int(qt)
    chk = False
    for val1 in dic.values():
        for val2 in dic.values():
            if int(val1 * 1.618) == val2 and val1 != val2:
                chk = True
                break
    print('Delicious!' if chk else 'Not Delicious...')


def q29721():
    # 백준 29721번 파이썬 변형 체스 놀이 : 다바바(Dabbaba)
    import sys

    n, k = map(int, sys.stdin.readline().split())
    dic1 = set()
    dic2 = set()
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        dic2.add((x, y))
        for i in range(-2, 5, 4):
            if 0 < x + i <= n:
                dic1.add((x + i, y))
        for i in range(-2, 5, 4):
            if 0 < y + i <= n:
                dic1.add((x, y + i))
    result = dic1 - dic2
    print(len(result))


def q4881():
    # 백준 4881번 파이썬 자리수의 제곱
    import sys

    def p(n):
        lst = [n]
        while lst.count(lst[-1]) < 2:
            num = lst[-1]
            new = 0
            for i in str(num):
                new += int(i) ** 2
            lst.append(new)
        return lst

    def c(list1, list2):
        result = []
        for i in list1:
            if i in list2:
                result.append(list1.index(i) + list2.index(i) + 2)
        for i in list2:
            if i in list1:
                result.append(list1.index(i) + list2.index(i) + 2)
        return min(result) if result else 0

    while 1:
        a, b = map(int, sys.stdin.readline().split())
        if a == b == 0:
            break
        lst_a = p(a)
        lst_b = p(b)
        print(a, b, c(lst_a, lst_b))


def q26043():
    # 백준 26043번 파이썬 식당 메뉴
    import sys, queue

    n = int(sys.stdin.readline())
    que = queue.Queue()
    a, b, c = [], [], []
    for _ in range(n):
        order = list(map(int, sys.stdin.readline().split()))
        if order[0] == 1:
            que.put((order[1], order[2]))
        else:
            s, m = que.get()
            if order[1] == m:
                a.append(s)
            else:
                b.append(s)
    for i in que.queue:
        c.append(i[0])
    print(*sorted(a)) if a else print('None')
    print(*sorted(b)) if b else print('None')
    print(*sorted(c)) if c else print('None')


def q25329():
    # 백준 25329번 파이썬 학생별 통화 요금 계산
    import sys, math

    def time_cal(time):
        h, m = map(int, time.split(':'))
        total = h * 60 + m
        return total

    def price_cal(minutes):
        default = 10
        additional = 0
        if minutes > 100:
            additional += math.ceil((minutes - 100) / 50) * 3
        return default + additional

    n = int(sys.stdin.readline())
    dic = {}
    for _ in range(n):
        t, s = sys.stdin.readline().split()
        if s in dic:
            dic[s] += time_cal(t)
        else:
            dic[s] = time_cal(t)
    result = []
    for key, val in dic.items():
        result.append((key, price_cal(val)))
    result = sorted(result, key=lambda x: (-x[1], x[0]))
    for i in result:
        print(*i)


def q14402():
    # 백준 14402번 파이썬 야근
    import sys

    q = int(sys.stdin.readline())
    dic = {}
    for _ in range(q):
        n, w = sys.stdin.readline().split()
        if n in dic and dic[n]:
            if w == '+':
                dic[n].append(w)
            else:
                if dic[n][-1] == '+':
                    dic[n].pop()
                else:
                    dic[n].append(w)
        else:
            dic[n] = [w]
    result = 0
    for val in dic.values():
        result += len(val)
    print(result)


def q1439():
    # 백준 1439번 파이썬 뒤집기
    s = input()
    if len(set(s)) == 1:
        print(0)
        return
    start0, start1 = s.split('0'), s.split('1')
    result0, result1 = 0, 0
    for i in start0:
        if i:
            result0 += 1
    for i in start1:
        if i:
            result1 += 1
    print(min(result0, result1))


def q1343():
    # 백준 1343번 파이썬 폴리오미노
    s = input().split('.')
    for i in range(len(s)):
        if s[i] == '':
            s[i] = '.'
        elif len(s[i]) % 4 == 0:
            s[i] = 'A' * len(s[i]) + '.'
        elif len(s[i]) % 2 == 0:
            s[i] = 'A' * (len(s[i]) // 4) * 4 + 'B' * 2 + '.'
        else:
            print(-1)
            return
    s[-1] = s[-1][:-1]
    print(''.join(s))


def q16435():
    # 백준 16435번 파이썬 스네이크버드
    n, l = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    for i in range(n):
        if lst[i] <= l:
            l += 1
    print(l)


def q15904():
    # 백준 15904번 파이썬 UCPC는 무엇의 약자일까?
    s = input()
    ans = 'UCPC'
    index = 0
    for i in s:
        if index == 4:
            break
        if ans[index] == i:
            index += 1
    print('I love UCPC' if index == 4 else 'I hate UCPC')


def q9237():
    # 백준 9237번 파이썬 이장님 초대
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    day = 1
    max_val = 0
    for i in lst:
        max_val = max(i, max_val - 1)
        day += 1
    print(max_val + day)


def q3135():
    # 백준 3135번 파이썬 라디오
    a, b = map(int, input().split())
    n = int(input())
    lst = [int(input()) for _ in range(n)]
    min_val = abs(a - b)
    clicks = 0
    for i in lst:
        if min_val > abs(i - b):
            min_val = abs(i - b)
            clicks = 1
    print(min_val + clicks)


def q6550():
    # 백준 6550번 파이썬 부분 문자열
    while 1:
        try:
            s, t = input().split()
            index = 0
            ans = len(s)
            chk = False
            for char in t:
                if char == s[index]:
                    index += 1
                if ans <= index:
                    chk = True
                    break
            print('Yes' if chk else 'No')
        except:
            break


def q1817():
    # 백준 1817번 파이썬 짐 챙기는 숌
    n, m = map(int, input().split())
    try:
        lst = list(map(int, input().split()))
        result = 1
        temp = 0
        for i in lst:
            temp += i
            if temp > m:
                result += 1
                temp = i
        print(result)
    except:
        print(0)


def q11256():
    # 백준 11256번 파이썬 사탕
    import sys

    t = int(sys.stdin.readline())
    for _ in range(t):
        j, n = map(int, sys.stdin.readline().split())
        lst = []
        result = 0
        for _ in range(n):
            r, c = map(int, sys.stdin.readline().split())
            lst.append(r * c)
        lst.sort(reverse=True)
        for i in lst:
            if j <= i:
                result += 1
                break
            else:
                j -= i
                result += 1
        print(result)


def q15720():
    # 백준 15720번 파이썬 카우버거
    b, c, d = map(int, input().split())
    burger = list(map(int, input().split()))
    side = list(map(int, input().split()))
    drink = list(map(int, input().split()))
    index = min(b, c, d)
    print(sum(burger) + sum(side) + sum(drink))
    burger.sort(reverse=True)
    side.sort(reverse=True)
    drink.sort(reverse=True)
    for i in range(index):
        burger[i] = int(burger[i] * 0.9)
        side[i] = int(side[i] * 0.9)
        drink[i] = int(drink[i] * 0.9)
    print(sum(burger) + sum(side) + sum(drink))


def q16208():
    # 백준 16208번 파이썬 귀찮음
    n = int(input())
    lst = list(map(int, input().split()))
    length = sum(lst)
    lst.sort()
    result = 0
    for i in lst:
        length -= i
        result += length * i
    print(result)


def q2891():
    # 백준 2891번 파이썬 카약과 강풍
    n, s, r = map(int, input().split())
    slst = set(map(int, input().split()))
    rlst = set(map(int, input().split()))
    slst, rlst = slst - rlst, rlst - slst
    result = 0
    for i in slst:
        if i - 1 in rlst:
            rlst.remove(i - 1)
        elif i + 1 in rlst:
            rlst.remove(i + 1)
        else:
            result += 1
    print(result)


def q2057():
    # 백준 2057번 파이썬 팩토리얼 분해
    n = int(input())
    if n == 0:
        print('NO')
        return
    dp = [0 for _ in range(21)]
    dp[0], dp[1] = 1, 1
    for i in range(2, 21):
        temp = 1
        for j in range(1, i + 1):
            temp *= j
        dp[i] = temp
    dp.sort(reverse=True)
    for i in range(21):
        if n - dp[i] >= 0:
            n -= dp[i]
    print('YES' if n == 0 else 'NO')


def q14655():
    # 백준 14655번 파이썬 욱제는 도박쟁이야!!
    n = int(input())
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    max_val, min_val = 0, 0
    for i in lst1:
        max_val += abs(i)
    for i in lst2:
        min_val += abs(i)
    print(max_val + min_val)


def q25496():
    # 백준 25496번 파이썬 장신구 명장 임스
    p, n = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    result = 0
    for i in lst:
        if p < 200:
            p += i
            result += 1
        else:
            break
    print(result)


def q30457():
    # 백준 30457번 파이썬 단체줄넘기
    n = int(input())
    lst = list(map(int, input().split()))
    temp1 = [0]
    temp2 = [0]
    lst.sort(reverse=True)
    for _ in range(n):
        if lst[-1] > temp1[-1]:
            temp1.append(lst.pop())
        elif lst[-1] > temp2[-1]:
            temp2.append(lst.pop())
        else:
            lst.pop()
    print(len(temp1) + len(temp2) - 2)


def q29615():
    # 백준 29615번 파이썬 알파빌과 베타빌
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    dic = set(map(int, input().split()))
    index = 0
    for i in lst:
        if index == m:
            break
        if i in dic:
            dic.remove(i)
        index += 1
    print(len(dic))


def q12034():
    # 백준 12034번 파이썬 김인천씨의 식료품가게 (Large)
    t = int(input())
    case = 0
    for _ in range(t):
        case += 1
        n = int(input())
        lst = list(map(int, input().split()))
        result = []
        for i in lst:
            if int(i * (4 / 3)) in lst:
                lst.remove(int(i * (4 / 3)))
                result.append(str(i))
        print(f'Case #{case}: {" ".join(result)}')


def q28464():
    # 백준 28464번 파이썬 Potato
    n = int(input())
    lst = sorted(list(map(int, input().split())), reverse=True)
    s, p = 0, 0
    for _ in range(n // 2):
        s += lst.pop()
    p = sum(lst)
    print(s, p)


def q25707():
    # 백준 25707번 파이썬 팔찌 만들기
    n = int(input())
    lst = sorted(list(map(int, input().split())))
    result = 0
    for i in range(n - 1):
        result += lst[i + 1] - lst[i]
    result += lst[-1] - lst[0]
    print(result)


def q27940():
    # 백준 27940번 파이썬 가지 산사태
    import sys

    n, m, k = map(int, sys.stdin.readline().split())
    result = 0
    index = 0
    chk = False
    for _ in range(m):
        index += 1
        t, r = map(int, sys.stdin.readline().split())
        result += r
        if result > k:
            print(index, 1)
            chk = True
            break
    if not chk:
        print(-1)


def q12033():
    # 백준 12033번 파이썬 김인천씨의 식료품가게 (Small)
    t = int(input())
    case = 0
    for _ in range(t):
        case += 1
        n = int(input())
        lst = list(map(int, input().split()))
        result = []
        for i in lst:
            if int(i * (4 / 3)) in lst:
                lst.remove(int(i * (4 / 3)))
                result.append(str(i))
        print(f'Case #{case}: {" ".join(result)}')


def q23028():
    # 백준 23028번 파이썬 5학년은 다니기 싫어요
    n, a, b = map(int, input().split())
    lst = []
    chk = False
    for _ in range(10):
        x, y = map(int, input().split())
        lst.append((x, y))
    for i in range(8 - n):
        can = 6
        if a < 66:
            a += lst[i][0] * 3
            b += lst[i][0] * 3
            can -= lst[i][0]
        if can:
            b += min(can, lst[i][1]) * 3
        if a >= 66 and b >= 130:
            chk = True
            break
    print('Nice' if chk else 'Nae ga wae')


def q28136():
    # 백준 28136번 파이썬 원, 탁!
    n = int(input())
    lst = list(map(int, input().split()))
    result = 0
    for i in range(n - 1):
        if lst[i] >= lst[i + 1]:
            result += 1
    if lst[0] <= lst[-1]:
        result += 1
    print(result)


def q1946():
    # 백준 1946번 파이썬 신입 사원
    import sys

    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
        lst.sort(key=lambda x: (x[0]))
        result = 0
        top = lst[0][1]
        for i in lst:
            if top >= i[1]:
                top = i[1]
                result += 1
        print(result)


def q15903():
    # 백준 15903번 파이썬 카드 합체 놀이
    import heapq

    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    heapq.heapify(lst)
    for i in range(m):
        a, b = heapq.heappop(lst), heapq.heappop(lst)
        a, b = a + b, a + b
        heapq.heappush(lst, a)
        heapq.heappush(lst, b)
    print(sum(lst))


def q11497():
    # 백준 11497번 파이썬 통나무 건너뛰기
    import sys, collections

    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        lst = list(map(int, sys.stdin.readline().split()))
        lst.sort(reverse=True)
        deq = collections.deque()
        chk = True
        for i in lst:
            if chk:
                deq.appendleft(i)
                chk = False
            else:
                deq.append(i)
                chk = True
        result = 0
        for i in range(n - 1):
            result = max(result, abs(deq[i] - deq[i + 1]))
        print(result)


def q1105():
    # 백준 1105번 파이썬 팔
    l, r = input().split()
    if len(l) != len(r) or not l.count('8') or not r.count('8'):
        print(0)
        return
    else:
        result = 0
        for i in range(len(l)):
            if l[i] == r[i]:
                if l[i] == '8':
                    result += 1
            else:
                break
        print(result)


def q1676():
    # 백준 1676번 파이썬 팩토리얼 0의 개수
    n = int(input())
    dp = [1] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] * i
    s = str(dp[n])[::-1]
    result = 0
    for char in s:
        if char == '0':
            result += 1
        else:
            break
    print(result)


def q1874():
    # 백준 1874번 파이썬 스택 수열
    import sys

    n = int(sys.stdin.readline())
    lst = [int(sys.stdin.readline()) for _ in range(n)]
    stack = [0]
    op = []
    num = 1
    for i in lst:
        while num <= i:
            stack.append(num)
            op.append('+')
            num += 1
        if stack[-1] == i:
            stack.pop()
            op.append('-')
        else:
            print('NO')
            return
    for i in op:
        print(i)


def q1966():
    # 백준 1966번 파이썬 프린터 큐
    import collections

    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        prio = collections.deque(list(map(int, input().split())))
        deq = collections.deque([i for i in range(n)])
        want = deq[m]
        result = 0
        max_prio = max(list(prio))
        while 1:
            if prio[0] == max_prio:
                result += 1
                prio.popleft()
                chk = deq.popleft()
                if chk == want:
                    break
                max_prio = max(list(prio))
            else:
                prio.append(prio.popleft())
                deq.append(deq.popleft())
        print(result)


def q18110():
    # 백준 18110번 파이썬 solved.ac
    import sys

    n = int(sys.stdin.readline())
    if n == 0:
        print(0)
        return
    lst = [int(sys.stdin.readline()) for _ in range(n)]
    rd = int(len(lst) * 15 / 100 + 0.5)
    lst.sort()
    if rd:
        lst = lst[rd:-rd]
    print(int(sum(lst) / len(lst) + 0.5))


def q18111():
    # 백준 18111번 파이썬 마인크래프트
    import sys

    n, m, b = map(int, sys.stdin.readline().split())
    lst = []
    for _ in range(n):
        lst.extend(map(int, sys.stdin.readline().split()))
    sec = [0 for i in range(257)]
    h = 0
    for i in range(257):
        block = b
        for j in lst:
            if j <= i:
                sec[i] += i - j
                block -= i - j
            else:
                sec[i] += 2 * (j - i)
                block += j - i
        if block >= 0 and sec[i] <= sec[h]:
            h = i
    print(sec[h], h)


def q2606():
    # 백준 2606번 파이썬 바이러스
    n = int(input())
    v = int(input())
    graph = [[] for i in range(n + 1)]
    visited = [0] * (n + 1)
    for i in range(v):
        a, b = map(int, input().split())
        graph[a] += [b]
        graph[b] += [a]

    def dfs(v):
        visited[v] = 1
        for nx in graph[v]:
            if visited[nx] == 0:
                dfs(nx)

    dfs(1)
    print(sum(visited) - 1)


def q9375():
    # 백준 9375번 파이썬 패션왕 신해빈
    t = int(input())
    for _ in range(t):
        n = int(input())
        dic = {}
        for _ in range(n):
            a, b = input().split()
            if b in dic:
                dic[b].append(a)
            else:
                dic[b] = ['']
                dic[b].append(a)
        result = 1
        for i in dic.values():
            result *= len(i)
        print(result - 1)


def q11726():
    # 백준 11726번 파이썬 2×n 타일링
    n = int(input())
    dp = [0 for _ in range(n + 1)]
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
    print(dp[n])


def q11727():
    # 백준 11727번 파이썬 2×n 타일링 2
    n = int(input())
    dp = [0 for _ in range(n + 1)]
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + 2 * (dp[i - 2])) % 10007
    print(dp[n])


def q17626():
    # 백준 17626번 파이썬 Four Squares
    n = int(input())
    dp = [0 if i ** 0.5 % 1 else 1 for i in range(n + 1)]
    result = 4
    for i in range(int(n ** 0.5), 0, -1):
        if dp[n]:
            result = 1
            break
        elif dp[n - i ** 2]:
            result = 2
            break
        else:
            for j in range(int((n - i ** 2) ** 0.5), 0, -1):
                if dp[(n - i ** 2) - j ** 2]:
                    result = 3
    print(result)


def q11279():
    # 백준 11279번 파이썬 최대 힙
    import sys, heapq

    n = int(sys.stdin.readline())
    lst = []
    for _ in range(n):
        x = int(sys.stdin.readline())
        if x:
            heapq.heappush(lst, -x)
        else:
            if lst:
                print(-heapq.heappop(lst))
            else:
                print(0)


def q5525():
    # 백준 5525번 파이썬 IOIOI
    n = int(input())
    m = int(input())
    s = input()
    result, index, current = 0, 0, 0
    while index < m - 2:
        if s[index:index + 3] == 'IOI':
            index += 2
            current += 1
            if current == n:
                current -= 1
                result += 1
        else:
            index += 1
            current = 0
    print(result)


def q11286():
    # 백준 11286번 파이썬 절댓값 힙
    import sys, heapq

    n = int(sys.stdin.readline())
    lst = []
    for _ in range(n):
        x = int(sys.stdin.readline())
        if x != 0:
            if x < 0:
                heapq.heappush(lst, (-x, 0))
            else:
                heapq.heappush(lst, (x, 1))
        else:
            if lst:
                ans = heapq.heappop(lst)
                if ans[1]:
                    print(ans[0])
                else:
                    print(-ans[0])
            else:
                print(0)


def q30088():
    # 백준 30088번 파이썬 공포의 면담실
    import sys

    n = int(sys.stdin.readline())
    dic = {}
    for i in range(n):
        lst = list(map(int, sys.stdin.readline().split()))
        dic[i] = sum(lst[1:])
    sort = sorted(dic.values())
    result = []
    last = 0
    for num in sort:
        last += num
        result.append(last)
    print(sum(result))


def q28470():
    # 백준 28470번 파이썬 슥~빡! 빡~슥!
    from math import floor

    n = int(input())
    att = list(map(int, input().split()))
    avi = list(map(int, input().split()))
    k = list(map(float, input().split()))
    result = 0
    for i in range(n):
        at = floor(att[i] * (k[i] * 10)) // 10
        av = floor(avi[i] * (k[i] * 10)) // 10
        if k[i] >= 1:
            result += at
            result -= avi[i]
        else:
            result += att[i]
            result -= av
    print(result)


def q29812():
    # 백준 29812번 파이썬 아니 이게 왜 안 돼
    n = int(input())
    s = input()
    d, m = map(int, input().split())
    cnt_h = cnt_y = cnt_u = 0
    energy = 0
    cnt = 0
    for char in s:
        if char == 'H':
            cnt_h += 1
            if cnt == 1:
                cnt = 0
                energy += d
            if cnt > 1:
                energy += min(d + m, cnt * d)
                cnt = 0
        elif char == 'Y':
            cnt_y += 1
            if cnt == 1:
                cnt = 0
                energy += d
            if cnt > 1:
                energy += min(d + m, cnt * d)
                cnt = 0
        elif char == 'U':
            cnt_u += 1
            if cnt == 1:
                cnt = 0
                energy += d
            if cnt > 1:
                energy += min(d + m, cnt * d)
                cnt = 0
        else:
            cnt += 1
    if cnt == 1:
        cnt = 0
        energy += d
    if cnt > 1:
        energy += min(d + m, cnt * d)
    max_val = min(cnt_h, cnt_y, cnt_u)
    print(energy if energy else 'Nalmeok')
    print(max_val if max_val else 'I love HanYang University')


def q1026():
    # 백준 1026번 파이썬 보물
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort(reverse=True)
    result = 0
    for i in range(n):
        result += a[i] * b[i]
    print(result)


def q2217():
    # 백준 2217번 파이썬 로프
    import sys

    n = int(sys.stdin.readline())
    lst = []
    for _ in range(n):
        lst.append(int(sys.stdin.readline()))
    lst.sort(reverse=True)
    max_val = lst[0]
    cnt = 1
    for i in range(1, n):
        cnt += 1
        temp = max(max_val, lst[i] * cnt)
        if temp > max_val:
            max_val = temp
    print(max_val)


def q10610():
    # 백준 10610번 파이썬 30
    n = sorted(list(input()), reverse=True)
    if n[-1] != '0':
        print(-1)
    else:
        result = 0
        for i in n:
            result += int(i)
        print(-1 if result % 3 else ''.join(n))


def q1049():
    # 백준 1049번 파이썬 기타줄
    n, m = map(int, input().split())
    mp = 1000
    mo = 1000
    for _ in range(m):
        p, o = map(int, input().split())
        mp = min(p, mp)
        mo = min(o, mo)
    price = 0
    while n > 0:
        if n >= 6:
            if mp < mo * 6:
                price += mp
                n -= 6
            else:
                price += mo * 6
                n -= 6
        else:
            if mp < mo * n:
                price += mp
                n = 0
            else:
                price += mo * n
                n = 0
    print(price)


def q2847():
    # 백준 2847번 파이썬 게임을 만든 동준이
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(int(input()))
    lst.reverse()
    result = 0
    for i in range(1, n):
        if lst[i] >= lst[i - 1]:
            temp = lst[i - 1] - 1
            result += lst[i] - temp
            lst[i] = temp
    print(result)


def q1969():
    # 백준 1969번 파이썬 DNA
    n, m = map(int, input().split())
    lst = []
    word = ''
    for _ in range(n):
        lst.append(input())
    for i in range(m):
        acgt = [0, 0, 0, 0]
        for j in lst:
            if j[i] == 'A': acgt[0] += 1
            if j[i] == 'C': acgt[1] += 1
            if j[i] == 'G': acgt[2] += 1
            if j[i] == 'T': acgt[3] += 1
        max_val = max(acgt)
        if acgt[0] == max_val: word += 'A'
        elif acgt[1] == max_val: word += 'C'
        elif acgt[2] == max_val: word += 'G'
        else: word += 'T'
    print(word)
    cnt = 0
    for i in lst:
        for j in range(m):
            if i[j] != word[j]:
                cnt += 1
    print(cnt)


def q1758():
    # 백준 1758번 파이썬 알바생 강호
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(int(input()))
    lst.sort(reverse=True)
    result = 0
    for i in range(n):
        t = lst[i] - i
        if t > 0:
            result += t
    print(result)


def q11508():
    # 백준 11508번 파이썬 2+1 세일
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(int(input()))
    lst.sort(reverse=True)
    result = 0
    b = n // 3
    for i in range(b):
        result += lst[3 * i] + lst[3 * i + 1]
    if n % 3 == 1:
        result += lst[n - 1]
    if n % 3 == 2:
        result += lst[n - 2] + lst[n - 1]
    print(result)


def q19939():
    # 백준 19939번 파이썬 박 터뜨리기
    n, k = map(int, input().split())
    dp = [i for i in range(1, k + 1)]
    dp_sum = [1] * k
    for i in range(1, k):
        dp_sum[i] = dp_sum[i - 1] + dp[i]
    if n < dp_sum[k - 1]:
        print(-1)
        return
    else:
        if n % k:
            if k % 2:
                print(k)
            else:
                if n % k == k // 2:
                    print(k - 1)
                else:
                    print(k)
        else:
            if k % 2:
                print(k - 1)
            else:
                print(k)


def q14469():
    # 백준 14469번 파이썬 소가 길을 건너간 이유 3
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(list(map(int, input().split())))
    lst.sort()
    result = 0
    for i in range(n):
        if result < lst[i][0]:
            result = 0
            result += lst[i][0] + lst[i][1]
        else:
            result += lst[i][1]
    print(result)


def q1246():
    # 백준 1246번 파이썬 온라인 판매
    n, m = map(int, input().split())
    lst = []
    for _ in range(m):
        lst.append(int(input()))
    lst.sort(reverse=True)
    mv = 0
    index = 0
    if n == 1 or m == 1:
        print(lst[0], lst[0])
        return
    else:
        for i in range(min(n, m)):
            if mv < lst[i] * (i + 1):
                mv = lst[i] * (i + 1)
                index = lst[i]
        if index == 0:
            index = lst[min(n, m)]
    print(index, mv)


def q20044():
    # 백준 20044번 파이썬 Project Teams
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    mv = 200000
    for i in range(n):
        mv = min(mv, lst[i] + lst[-i - 1])
    print(mv)


def q13413():
    # 백준 13413번 파이썬 오셀로 재배치
    t = int(input())
    for _ in range(t):
        n = int(input())
        s1 = list(input())
        s2 = list(input())
        result = 0
        wrong = 0
        s1w = 0
        s2w = 0
        for i in range(n):
            if s1[i] != s2[i]:
                wrong += 1
            if s1[i] == 'W':
                s1w += 1
            if s2[i] == 'W':
                s2w += 1
        wrong -= abs(s1w - s2w)
        result += abs(s1w - s2w)
        result += wrong // 2
        print(result)


def q3213():
    # 백준 3213번 파이썬 피자
    import math

    n = int(input())
    dic = {'1/2': 0, '1/4': 0, '3/4': 0}
    result = 0
    for _ in range(n):
        dic[input()] += 1
    result += math.ceil(dic['1/2'] / 2)
    result += dic['3/4']
    if dic['1/4'] > 0:
        dic['1/4'] -= dic['3/4']
    if dic['1/4'] > 0 and dic['1/2'] % 2:
        dic['1/4'] -= 2
    if dic['1/4'] > 0:
        result += math.ceil(dic['1/4'] / 4)
    print(result)


def q25379():
    # 백준 25379번 파이썬 피하자
    n = int(input())
    lst = list(map(int, input().split()))
    result1 = 0
    result2 = 0
    temp = 0
    for i in range(n):
        if lst[i] % 2:
            temp += 1
        else:
            result1 += temp
    lst.reverse()
    temp = 0
    for i in range(n):
        if lst[i] % 2:
            temp += 1
        else:
            result2 += temp
    print(min(result1, result2))


def q20186():
    # 백준 20186번 파이썬 수 고르기
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    lst = lst[:k]
    for i in range(k):
        lst[i] = lst[i] - i
    print(sum(lst))


def q17521():
    # 백준 17521번 파이썬 Byte Coin
    n, w = map(int, input().split())
    lst = [int(input()) for _ in range(n)]
    coin = 0
    for i in range(n - 1):
        if lst[i] < lst[i + 1] and w // lst[i]:
            coin += w // lst[i]
            w %= lst[i]
        elif lst[i] > lst[i + 1] and coin:
            w += coin * lst[i]
            coin = 0
    if coin:
        w += coin * lst[n - 1]
    print(w)


def q28324():
    # 백준 28324번 파이썬 스케이트 연습
    n = int(input())
    lst = list(map(int, input().split()))
    lst.reverse()
    speed = 0
    result = 0
    for i in range(n):
        if lst[i] > speed:
            speed += 1
            result += speed
        else:
            result += lst[i]
            speed = lst[i]
    print(result)


def q12782():
    # 백준 12782번 파이썬 비트 우정지수
    t = int(input())
    for _ in range(t):
        n, m = map(str, input().split())
        result = 0
        wrong = 0
        n1 = 0
        m1 = 0
        for i in range(len(n)):
            if n[i] != m[i]:
                wrong += 1
            if n[i] == '1':
                n1 += 1
            if m[i] == '1':
                m1 += 1
        wrong -= abs(n1 - m1)
        result += abs(n1 - m1)
        result += wrong // 2
        print(result)


def q12788():
    # 백준 12788번 파이썬 제 2회 IUPC는 잘 개최될 수 있을까?
    n = int(input())
    m, k = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    need = m * k
    if need > sum(lst):
        print('STRESS')
        return
    result = 0
    while 1:
        if need > 0:
            need -= lst[result]
            result += 1
        else:
            break
    print(result)


def q12927():
    # 백준 12927번 파이썬 배수 스위치
    lst = list(input())
    length = len(lst)
    result = 0
    if lst.count('Y') == 0:
        print(0)
        return
    else:
        for i in range(length):
            if lst[i] == 'Y':
                for j in range(length // (i + 1)):
                    if lst[i + j * (i + 1)] == 'Y':
                        lst[i + j * (i + 1)] = 'N'
                    else:
                        lst[i + j * (i + 1)] = 'Y'
                result += 1
        print(result if lst.count('Y') == 0 else -1)


def q2865():
    # 백준 2865번 파이썬 나는 위대한 슈퍼스타K
    n, m, k = map(int, input().split())
    dic = {}
    for i in range(n):
        dic[i + 1] = 0
    for i in range(m):
        point = input().split()
        for j in range(0, 2 * n, 2):
            dic[int(point[j])] = max(dic[int(point[j])], float(point[j + 1]))
    print('%.1f' % sum(sorted(dic.values(), reverse=True)[:k]))


def q17262():
    # 백준 17262번 파이썬 팬덤이 넘쳐흘러
    import sys

    n = int(sys.stdin.readline())
    lst = []
    for _ in range(n):
        s, e = map(int, sys.stdin.readline().split())
        lst.append((s, e))
    lst.sort(reverse=True)
    max_s = lst[0][0]
    lst.sort(key=lambda x: (x[1]))
    min_e = lst[0][1]
    print(max(0, max_s - min_e))


def q22993():
    # 백준 22993번 파이썬 서든어택 3
    n = int(input())
    lst = list(map(int, input().split()))
    if n == 1:
        print('Yes')
        return
    p = lst.pop(0)
    lst.sort()
    max_val = max(lst)
    for i in range(n - 1):
        if p > lst[i]:
            p += lst[i]
        else:
            break
    print('Yes' if p > max_val else 'No')


def q20363():
    # 백준 20363번 파이썬 당근 키우기
    x, y = map(int, input().split())
    lst = sorted([x, y])
    print(lst[1] + int(lst[0] / 10) + lst[0])


def q24498():
    # 백준 24498번 파이썬 blobnom
    n = int(input())
    lst = list(map(int, input().split()))
    result = 0
    if n < 3:
        print(max(lst))
    else:
        for i in range(1, n - 1):
            result = max(result, lst[i] + min(lst[i - 1], lst[i + 1]))
        print(max(result, lst[0], lst[-1]))


def q20937():
    # 백준 20937번 파이썬 떡국
    n = int(input())
    lst = list(map(int, input().split()))
    dic = {}
    for i in lst:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    print(max(dic.values()))


def q16162():
    # 백준 16162번 파이썬 가희와 3단 고음
    n, a, d = map(int, input().split())
    lst = list(map(int, input().split()))
    result = 0
    for i in range(n):
        if lst[i] == a:
            result += 1
            a += d
    print(result)


def q27919():
    # 백준 27919번 파이썬 UDPC 파티
    v = input()
    dic = {'U': 0, 'D': 0}
    for i in v:
        if i == 'U' or i == 'C':
            dic['U'] += 1
        else:
            dic['D'] += 1
    if dic['D']:
        if dic['U'] > dic['D'] // 2 + dic['D'] % 2:
            print('UDP')
        else:
            print('DP')
    else:
        print('U')


def q26099():
    # 백준 26099번 파이썬 설탕 배달 2
    n = int(input())
    val5 = n // 5
    val3 = 0
    mod = n % 5
    if mod == 1:
        if val5:
            val5 -= 1
            val3 += 2
    if mod == 2:
        if val5:
            val5 -= 2
            val3 += 4
    if mod == 3:
        if val5:
            val3 += 1
        else:
            val3 += 1
    if mod == 4:
        if val5:
            val5 -= 1
            val3 += 3
    if val5 < 0:
        val5 = 0
    print(val5 + val3 if val5 * 5 + val3 * 3 == n else -1)


def q25943():
    # 백준 25943번 파이썬 양팔저울
    n = int(input())
    lst = list(map(int, input().split()))
    left = lst[0]
    right = lst[1]
    w = [100, 50, 20, 10, 5, 2, 1]
    result = 0
    for i in range(2, n):
        if left == right:
            left += lst[i]
        else:
            if left > right:
                right += lst[i]
            else:
                left += lst[i]
    if left > right:
        right, left = left, right
    for i in w:
        if left == right:
            break
        else:
            result += (right - left) // i
            left += (right - left) // i * i
    print(result)


def q9657():
    # 백준 9657번 파이썬 돌 게임 3
    n = int(input())
    dp = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        if i % 7 != 0 and i % 7 != 2:
            dp[i] = 1
    print('SK' if dp[n] else 'CY')


def q10825():
    # 백준 10825번 파이썬 국영수
    import sys

    n = int(sys.stdin.readline())
    lst = [sys.stdin.readline().split() for _ in range(n)]
    lst.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
    for i in lst:
        print(i[0])


def q2567():
    # 백준 2567번 색종이 - 2 파이썬
    n = int(input())
    dp = [[0] * 101 for _ in range(101)]
    result = 0
    for _ in range(n):
        x, y = map(int, input().split())
        for i in range(x, x + 10):
            for j in range(y, y + 10):
                dp[i][j] = 1
    for i in range(100):
        for j in range(100):
            if dp[i][j]:
                if i == 0 or dp[i - 1][j] == 0:
                    result += 1
                if i == 99 or dp[i + 1][j] == 0:
                    result += 1
                if j == 0 or dp[i][j - 1] == 0:
                    result += 1
                if j == 99 or dp[i][j + 1] == 0:
                    result += 1
    print(result)


def q2628():
    # 백준 2628번 종이자르기 파이썬
    x, y = map(int, input().split())
    n = int(input())
    width = [0, x]
    height = [0, y]
    for _ in range(n):
        a, b = map(int, input().split())
        if a == 0:
            height.append(b)
        else:
            width.append(b)
    width.sort()
    height.sort()
    max_width = 0
    max_height = 0
    for i in range(1, len(width)):
        max_width = max(max_width, width[i] - width[i - 1])
    for i in range(1, len(height)):
        max_height = max(max_height, height[i] - height[i - 1])
    print(max_width * max_height)


def q10157():
    # 백준 10157번 자리배정 파이썬
    c, r = map(int, input().split())
    k = int(input())
    if k > c * r:
        print(0)
        return
    dp = [[0] * r for _ in range(c)]
    direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    x, y = 0, 0
    index = 1
    direct_index = 1
    while index <= c * r:
        dp[x][y] = index
        if k == index:
            print(x + 1, y + 1)
            return
        next_x = x + direct[direct_index][0]
        next_y = y + direct[direct_index][1]
        if (0 <= next_x < c) and (0 <= next_y < r) and (dp[next_x][next_y] == 0):
            x, y = next_x, next_y
        else:
            direct_index = (direct_index + 1) % 4
            x += direct[direct_index][0]
            y += direct[direct_index][1]
        index += 1


def q2578():
    # 백준 2578번 빙고 파이썬
    def call_number(board, number):
        for i in range(5):
            for j in range(5):
                if board[i][j] == number:
                    board[i][j] = 0
                    return

    def check_bingo(board):
        bingo_cnt = 0
        for row in board:
            if all(i == 0 for i in row):
                bingo_cnt += 1
        for col in range(5):
            if all(board[row][col] == 0 for row in range(5)):
                bingo_cnt += 1
        if all(board[i][i] == 0 for i in range(5)):
            bingo_cnt += 1
        if all(board[i][4 - i] == 0 for i in range(5)):
            bingo_cnt += 1
        return bingo_cnt

    lst1 = [list(map(int, input().split())) for _ in range(5)]
    lst2 = [list(map(int, input().split())) for _ in range(5)]
    cnt = 0

    for i in range(5):
        for j in range(5):
            cnt += 1
            call_number(lst1, lst2[i][j])
            chk = check_bingo(lst1)
            if chk >= 3:
                print(cnt)
                return


def q10709():
    # 백준 10709번 기상캐스터 파이썬
    h, w = map(int, input().split())
    lst = [list(input() + '.') for _ in range(h)]
    result = [[-1] * w for _ in range(h)]
    day = 0
    while day < w:
        for i in range(h):
            for j in range(w):
                if lst[i][j] == 'c' and result[i][j] == -1:
                    result[i][j] = day
        for i in range(h):
            for j in range(w - 1, -1, -1):
                if lst[i][j] == 'c':
                    lst[i][j], lst[i][j + 1] = '.', 'c'
        day += 1
    for i in result:
        print(*i)


def q2980():
    # 백준 2980번 도로와 신호등 파이썬
    n, l = map(int, input().split())
    dp = [1] * (l + 1)
    lst = [list(map(int, input().split())) for _ in range(n)]
    time = 0
    index = 1
    while index <= l:
        time += 1
        for i in lst:
            if time % (i[1] + i[2]) < i[1]:
                dp[i[0]] = 0
            else:
                dp[i[0]] = 1
        if dp[index] == 1:
            index += 1
    print(time)


def q2669():
    # 백준 2669번 직사각형 네개의 합집합의 면적 구하기 파이썬
    lst = [list(map(int, input().split())) for _ in range(4)]
    dp = [[0] * 101 for _ in range(101)]
    for a in lst:
        for i in range(a[0], a[2]):
            for j in range(a[1], a[3]):
                dp[i][j] = 1
    result = 0
    for i in dp:
        result += sum(i)
    print(result)


def q2477():
    # 백준 2477번 참외밭 파이썬
    k = int(input())
    dist = []
    length = []
    for _ in range(6):
        d, l = map(int, input().split())
        dist.append(d)
        length.append(l)

    big_w, big_h = 0, 0
    for i in range(6):
        if dist[i] == 1 or dist[i] == 2:
            big_w = max(big_w, length[i])
        if dist[i] == 3 or dist[i] == 4:
            big_h = max(big_h, length[i])

    small_w, small_h = 0, 0
    for i in range(6):
        if dist[i] == 1 or dist[i] == 2:
            if length[i] == big_w:
                small_h = abs(length[(i + 1) % 6] - length[(i + 5) % 6])
        if dist[i] == 3 or dist[i] == 4:
            if length[i] == big_h:
                small_w = abs(length[(i + 1) % 6] - length[(i + 5) % 6])
    print(k * ((big_w * big_h) - (small_w * small_h)))


def q10158():
    # 백준 10158번 개미 파이썬
    c, r = map(int, input().split())
    p, q = map(int, input().split())
    t = int(input())

    x = (p + t) % (2 * c)
    y = (q + t) % (2 * r)

    if x > c:
        x = 2 * c - x
    if y > r:
        y = 2 * r - y

    print(x, y)


def q2527():
    # 백준 2527번 직사각형 파이썬
    for _ in range(4):
        x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
        left = max(x1, x2)
        right = min(p1, p2)
        bottom = max(y1, y2)
        top = min(q1, q2)
        if left > right or bottom > top:
            print('d')
        elif left == right and bottom == top:
            print('c')
        elif left == right or bottom == top:
            print('b')
        else:
            print('a')


def q1063():
    # 백준 1063번 킹 파이썬
    k, r, n = input().split()
    dic = {'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1),
           'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1)}
    k_pos = [(ord(k[0]) - 64), int(k[1])]
    r_pos = [(ord(r[0]) - 64), int(r[1])]
    for _ in range(int(n)):
        d = input()
        next_k_pos = [k_pos[0] + dic[d][0], k_pos[1] + dic[d][1]]
        if next_k_pos == r_pos:
            next_r_pos = [r_pos[0] + dic[d][0], r_pos[1] + dic[d][1]]
            if 1 <= next_r_pos[0] <= 8 and 1 <= next_r_pos[1] <= 8:
                k_pos = r_pos
                r_pos = next_r_pos
        elif 1 <= next_k_pos[0] <= 8 and 1 <= next_k_pos[1] <= 8:
            k_pos = next_k_pos
    print(chr(k_pos[0] + 64) + str(k_pos[1]))
    print(chr(r_pos[0] + 64) + str(r_pos[1]))


def q3085():
    # 백준 3085번 사탕 게임 파이썬
    n = int(input())
    lst = [list(input()) for _ in range(n)]
    dist = [(1, 0), (0, 1)]
    result = 0

    def chk(board):
        x_result = 0
        y_result = 0
        for a in range(n):
            temp = 1
            temp_max = 1
            for b in range(1, n):
                if lst[a][b - 1] == lst[a][b]:
                    temp += 1
                    temp_max = max(temp_max, temp)
                else:
                    temp = 1
            x_result = max(x_result, temp_max)

            temp = 1
            temp_max = 1
            for b in range(1, n):
                if lst[b - 1][a] == lst[b][a]:
                    temp += 1
                    temp_max = max(temp_max, temp)
                else:
                    temp = 1
            y_result = max(y_result, temp_max)
        return max(x_result, y_result)

    for i in range(n):
        for j in range(n):
            for dx, dy in dist:
                ni, nj = i + dx, j + dy
                if ni < n and nj < n:
                    lst[i][j], lst[ni][nj] = lst[ni][nj], lst[i][j]
                    cnt = chk(lst)
                    result = max(result, cnt)
                    lst[i][j], lst[ni][nj] = lst[ni][nj], lst[i][j]
                if result == n:
                    print(n)
                    return
    print(result)


def q4673():
    # 백준 4673번 셀프 넘버 파이썬
    dp = [False] * 10001
    for i in range(1, 10001):
        temp = i
        while i > 0:
            temp += i % 10
            i //= 10
        if temp < 10000:
            dp[temp] = True
    for i in range(1, 10000):
        if not dp[i]:
            print(i)


def q1475():
    # 백준 1475번 방 번호 파이썬
    n = int(input())
    dic = {i: 0 for i in range(10)}
    while n:
        dic[n % 10] += 1
        n //= 10
    if dic[6] + dic[9]:
        dic[6], dic[9] = int((dic[6] + dic[9]) / 2 + 0.5), int((dic[9] + dic[6]) / 2 + 0.5)
    print(max(dic.values()))


def q2167():
    # 백준 2167번 2차원 배열의 합 파이썬
    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    k = int(input())
    for _ in range(k):
        i, j, x, y = map(int, input().split())
        result = 0
        for a in range(i - 1, x):
            result += sum(lst[a][j - 1:y])
        print(result)


def q17413():
    # 백준 17413번 단어 뒤집기 2 파이썬
    s = input()
    start = 0
    lst = []
    tag = False
    for i in range(len(s)):
        if s[i] == '<':
            lst.append(s[start:i])
            start = i
            tag = True
        if s[i] == '>':
            lst.append(s[start:i + 1])
            start = i + 1
            tag = False
        if s[i] == ' ' and tag == False:
            lst.append(' ' + s[start:i])
            start = i + 1
    lst.append(s[start:])
    result = ''
    for i in lst:
        if '<' in i:
            result += i
        else:
            result += i[::-1]
    print(result)


def q10799():
    # 백준 10799번 쇠막대기 파이썬
    s = input()
    stack = []
    result = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if s[i - 1] == '(':
                stack.pop()
                result += len(stack)
            else:
                stack.pop()
                result += 1
    print(result)


def q13335():
    # 백준 13335번 트럭 파이썬
    from collections import deque

    n, w, l = map(int, input().split())
    lst = deque(list(map(int, input().split())))
    bridge = deque()
    time = 0
    while lst or bridge:
        time += 1
        if bridge:
            for i in range(len(bridge)):
                bridge[i][0] -= 1
            if bridge[0][0] == 0:
                bridge.popleft()
        weight = sum(map(lambda x: x[1], bridge))
        if lst:
            if weight + lst[0] <= l:
                bridge.append([w, lst.popleft()])
    print(time)


def q1260():
    # 백준 1260번 파이썬 DFS와 BFS
    from collections import deque

    n, m, v = map(int, input().split())
    lst = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        lst[a].append(b)
        lst[b].append(a)
    for i in lst:
        i.sort()

    def dfs(graph, start, visited):
        stack = [start]
        result = []

        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                result.append(node)
                for neighbor in sorted(graph[node], reverse=True):
                    if not visited[neighbor]:
                        stack.append(neighbor)
        return result

    def bfs(graph, start, visited):
        queue = deque([start])
        result = []
        visited[start] = True

        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in sorted(graph[node]):
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return result

    visited_dfs = [False] * (n + 1)
    visited_bfs = [False] * (n + 1)
    dfs_result = dfs(lst, v, visited_dfs)
    bfs_result = bfs(lst, v, visited_bfs)
    print(*dfs_result)
    print(*bfs_result)


def q2178():
    # 백준 2178번 미로 탐색 파이썬
    from collections import deque

    n, m = map(int, input().split())
    lst = [list(map(int, list(input()))) for _ in range(n)]
    v = [[False] * m for _ in range(n)]
    dist = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def bfs(graph, start):
        q = deque([start])
        v[0][0] = True
        while q:
            x, y, d = q.popleft()
            if x == n - 1 and y == m - 1:
                return d
            for dx, dy in dist:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and not v[nx][ny]:
                    v[nx][ny] = True
                    q.append((nx, ny, d + 1))
    print(bfs(lst, (0, 0, 1)))


def q2667():
    # 백준 2667번 단지번호붙이기 파이썬
    from collections import deque

    n = int(input())
    lst = [list(map(int, list(input()))) for _ in range(n)]
    v = [[0] * n for _ in range(n)]
    dist = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(graph, start, c):
        q = deque([start])
        v[start[0]][start[1]] = True
        while q:
            x, y = q.popleft()
            for dx, dy in dist:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] and not v[nx][ny]:
                    v[nx][ny] = True
                    c += 1
                    q.append((nx, ny))
        return c

    cnt = []
    for i in range(n):
        for j in range(n):
            if lst[i][j] == 1 and v[i][j] == 0:
                cnt.append(bfs(lst, (i, j), 1))
    cnt.sort()
    print(len(cnt))
    for i in cnt:
        print(i)


def q10867():
    # 백준 10867번 중복 빼고 정렬하기 파이썬
    n = int(input())
    lst = sorted(set(map(int, input().split())))
    print(*lst)
q10867()