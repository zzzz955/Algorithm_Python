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
    # 쿠키의 신체 측정
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
    for i in range(2 ** index - n + 1):
        result = 2 ** index - (2 * i)
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


def q1515():
    # 수 이어 쓰기
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
    # 햄버거 분배
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
    # 진우의 달 여행 (틀림, dfs 공부 후 재채점 필요)
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
    # 비슷한 단어
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
    # KCPC
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
    # 타노스
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
    # IF문 좀 대신 써줘
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
    # 가희와 키워드
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
    # 최소 힙
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
    # 랭킹전 대기열
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
    # 주식
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
    # 에디터
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
    # 창고 다각형
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
    # N번째 큰 수
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
    # 한 줄로 서기
    n = int(input())
    order = list(map(int, input().split()))
    lst = []
    while order:
        lst.insert(order[-1], len(order))
        order.pop()
    print(*lst)


def q2941():
    # 크로아티아 알파벳
    s = input()
    lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    for word in lst:
        s = s.replace(word, 'x')
    print(len(s))


def q1316():
    # 그룹 단어 체커
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
    # 너의 평점은
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
    # 색종이
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
    # 분수찾기
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
    # 알고리즘 수업 - 점근적 표기 1
    a1, a2 = map(int, input().split())
    c = int(input())
    n0 = int(input())
    if a1 <= c and a1 * n0 + a2 <= c * n0:
        print(1)
    else:
        print(0)


def q1018():
    # 체스판 다시 칠하기
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
    # 영화감독 숌
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
    # 수 정렬하기 2
    import sys

    n = int(sys.stdin.readline())
    lst = []
    for _ in range(n):
        lst.append(int(sys.stdin.readline()))
    lst.sort()
    for num in lst:
        print(num)


def q1427():
    # 소트인사이드
    n = list(input())
    n.sort(reverse=True)
    result = ''
    for num in n:
        result += num
    print(result)


def q11650():
    # 좌표 정렬하기
    n = int(input())
    xy = []
    for _ in range(n):
        x, y = map(int, input().split())
        xy.append([x, y])
    xy.sort()
    for i in xy:
        print(*i)


def q11651():
    # 좌표 정렬하기 2
    n = int(input())
    xy = []
    for _ in range(n):
        x, y = map(int, input().split())
        xy.append([y, x])
    xy.sort()
    for i in range(n):
        print(xy[i][1], xy[i][0])


def q1181():
    # 단어 정렬
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
    # 나이순 정렬
    n = int(input())
    lst = []
    for _ in range(n):
        y, n = input().split()
        lst.append([int(y), n])
    lst.sort(key=lambda x: x[0])
    for s in lst:
        print(*s)


def q18870():
    # 좌표 압축
    n = int(input())
    lst = list(map(int, input().split()))
    temp = sorted(set(lst))
    dic = {}
    for i in range(len(temp)):
        dic[temp[i]] = i
    for s in lst:
        print(dic[s], end=' ')


def q10815():
    # 숫자 카드
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
    # 문자열 집합
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
    # 회사에 있는 사람
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
    # 나는야 포켓몬 마스터 이다솜
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
    # 숫자 카드 2
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
    # 듣보잡
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
    # 대칭 차집합
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
    # 서로 다른 부분 문자열의 개수
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
    # 최소공배수
    import math

    a, b = map(int, input().split())
    gcd = math.gcd(a, b)
    print((a * b) // gcd)


def q1735():
    # 분수 합
    import math

    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())
    lcm = math.lcm(b1, b2)
    result = (a1 * lcm // b1) + (a2 * lcm // b2)
    gcd = math.gcd(result, lcm)
    print(result // gcd, lcm // gcd)


def q2485():
    # 가로수
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
    # 다음 소수
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
    # 베르트랑 공준
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
    # 골드바흐 파티션

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
    # 창문 닫기
    n = int(input())
    result = 0
    for _ in range(1, int(n ** 0.5) + 1):
        result += 1
    print(result)


def q28278():
    # 스택 2
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
    # 제로
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
    # 괄호
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
    # 균형잡힌 세상
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
    # 도키도키 간식드리미
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
    # 큐 2
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
    # 요세푸스 문제 0
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
    # 덱 2
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
    # 풍선 터뜨리기
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
    # queuestack
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
    # 인사성 밝은 곰곰이
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
    # 붙임성 좋은 총총이
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
    # 통계학
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
    # 칸토어 집합
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
    # N과 M (1)
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
    # N과 M (2)
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
    # N과 M (3)
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
    # N과 M (4)
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
    # 계단 오르기
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
    # 구간 합 구하기 4
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
    # 수열
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
    # 인간-컴퓨터 상호작용
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
    # 동전 0
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
    # 회의실 배정
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
    # ATM
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
    # 잃어버린 괄호
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
    # 수 찾기
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
    # 랜선 자르기
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
    # 나무 자르기
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
    # 구간 합 구하기 5
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
    # 거스름돈
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
    # BABBA
    k = int(input())
    dp = [0] * 46
    dp[1] = 1
    for i in range(2, 46):
        dp[i] = dp[i - 2] + dp[i - 1]
    print(dp[k - 1], dp[k])


def q10826():
    # 피보나치 수 4
    n = int(input())
    dp = [0] * 10001
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
    print(dp[n])


def q13301():
    # 타일 장식물
    n = int(input())
    dp = [1] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
    dp2 = [4] * (n + 1)
    for i in range(2, n + 1):
        dp2[i] = dp2[i - 1] + (dp[i - 1] * 2)
    print(dp2[n])
q13301()