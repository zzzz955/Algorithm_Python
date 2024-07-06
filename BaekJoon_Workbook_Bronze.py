def q14563():
    # 백준 14563번 파이썬 완전수
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
    # 백준 1773번 파이썬 폭죽쇼
    n, c = map(int, (input().split()))
    dp = [0] * 2000001
    for _ in range(n):
        time = int(input())
        for i in range(time, c + 1, time):
            dp[i] = 1
    print(sum(dp))


def q2775():
    # 백준 2775번 파이썬 부녀회장이 될테야
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


def q2609():
    # 백준 2609번 파이썬 최대공약수와 최소공배수
    n1, n2 = map(int, input().split())
    for_lcm = n1 * n2
    for_gcd = 0
    if n1 >= n2:
        while n2 != 0:
            r = n1 % n2
            n1 = n2
            n2 = r
        for_gcd = n1
    else:
        while n1 != 0:
            r = n2 % n1
            n2 = n1
            n1 = r
        for_gcd = n2
    gcd = for_gcd
    lcm = for_lcm // gcd
    print(gcd)
    print(lcm)


def q1157():
    # 백준 1157번 파이썬 단어 공부
    s = input().upper()
    dp = [0] * 26
    for char in s:
        dp[ord(char) - 65] += 1
    if dp.count(max(dp)) >= 2:
        print('?')
    else:
        print(chr(dp.index(max(dp)) + 65))


def q4344():
    # 백준 4344번 파이썬 평균은 넘겠지
    c = int(input())
    result = []
    for _ in range(c):
        lst = list(map(int, input().split()))
        count = 0
        average = sum(lst[1:]) / lst[0]
        for i in range(1, len(lst)):
            if lst[i] > average:
                count += 1
        answer = str(round((count / lst[0] * 100), 3))
        if answer[-1] == '0':
            answer += '00%'
        else:
            answer += '%'
        result.append(answer)
    for answer in result:
        print(answer)


def q1032():
    # 백준 1032번 파이썬 명령 프롬프트
    n = int(input())
    files = []
    for _ in range(n):
        files.append(input())
    string = ''
    index = 0

    for j in range(len(files[0])):
        temp = True
        for i in range(1, n):
            if files[i - 1][j] != files[i][j]:
                temp = False
        if temp:
            string += files[0][index]
            index += 1
        else:
            string += '?'
            index += 1
    print(string)


def q2562():
    # 백준 2562번 파이썬 최댓값
    lst = []
    for _ in range(9):
        lst.append(int(input()))
    print(max(lst))
    print(lst.index(max(lst)) + 1)


def q10872():
    # 백준 10872번 파이썬 팩토리얼
    n = int(input())

    def factor(num):
        if num <= 1:
            return 1
        else:
            return num * factor(num - 1)

    print(factor(n))


def q23971():
    # 백준 23971번 파이썬 ZOAC 4
    import math
    h, w, n, m = map(int, input().split())
    print(math.ceil(h / (n + 1)) * math.ceil(w / (m + 1)))


def q5073():
    # 백준 5073번 파이썬 삼각형과 세 변
    result = []
    while 1:
        lst = list(map(int, input().split()))
        if sum(lst) == 0:
            break
        lst_temp1 = lst.copy()
        max_temp1 = lst_temp1.pop(lst_temp1.index(max(lst_temp1)))
        if sum(lst_temp1) <= max_temp1:
            result.append("Invalid")
        elif len(set(lst)) == 1:
            result.append("Equilateral")
        elif len(set(lst)) == 2:
            result.append("Isosceles")
        else:
            result.append("Scalene")
    for answer in result:
        print(answer)


def q2292():
    # 백준 2292번 파이썬 벌집
    n = int(input())
    index = 1
    first = 1
    prod = 6
    while first < n:
        first += prod * index
        index += 1
    print(index)


def q13458():
    # 백준 13458번 파이썬 시험 감독
    import math

    n = int(input())
    a = list(map(int, input().split()))
    b, c = map(int, input().split())
    result = 0
    for i in range(n):
        if a[i] >= b:
            a[i] -= b
        else:
            a[i] = a[i] // b
        result += math.ceil(a[i] / c) + 1
    print(result)


def q10926():
    # 백준 10926번 파이썬 ??!
    s = input()
    print(s + '??!')


def q18108():
    # 백준 18108번 파이썬 1998년생인 내가 태국에서는 2541년생?!
    y = int(input())
    print(str(y - 543))


def q11382():
    # 백준 11382번 파이썬 꼬마 정민
    a, b, c = map(int, input().split())
    print(str(a + b + c))


def q10171():
    # 백준 10171번 파이썬 고양이
    l1 = "\\    /\\"
    l2 = " )  ( ')"
    l3 = "(  /  )"
    l4 = " \\(__)|"
    lst = [l1, l2, l3, l4]
    for i in lst:
        print(i)


def q10172():
    # 백준 10172번 파이썬 개
    l1 = "|\\_/|"
    l2 = "|q p|   /}"
    l3 = '( 0 )"""\\'
    l4 = '|"^"`    |'
    l5 = "||_/=\\\\__|"
    lst = [l1, l2, l3, l4, l5]
    for i in lst:
        print(i)


def q2739():
    # 백준 2739번 파이썬 구구단
    n = int(input())
    for i in range(1, 10):
        s = str(n) + f' * {i} = {n * i}'
        print(s)


def q10950():
    # 백준 10950번 파이썬 A+B - 3
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        print(a + b)


def q8393():
    # 백준 8393번 파이썬 합
    n = int(input())
    result = 0
    for i in range(1, n + 1):
        result += i
    print(result)


def q25304():
    # 백준 25304번 파이썬 영수증
    x = int(input())
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        x -= a * b
    if x:
        print('No')
    else:
        print('Yes')


def q25314():
    # 백준 25314번 파이썬 코딩은 체육과목 입니다
    n = int(input())
    result = ''
    if n % 4 == 0:
        f = n // 4
    else:
        f = n // 4 + 1
    for _ in range(f):
        result += 'long '
    print(result + 'int')


def q15552():
    # 백준 15552번 파이썬 빠른 A+B
    import sys

    t = int(input())
    for _ in range(t):
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)


def q2438():
    # 백준 2438번 파이썬 별 찍기 - 1
    n = int(input())
    for i in range(1, n + 1):
        print('*' * i)


def q2439():
    # 백준 2439번 파이썬 별 찍기 - 2
    n = int(input())
    for i in range(1, n + 1):
        result = ' ' * (n - i) + '*' * i
        print(result)


def q10952():
    # 백준 10952번 파이썬 A+B - 5
    while 1:
        a, b = map(int, input().split())
        if a == b == 0:
            break
        else:
            print(a + b)


def q10951():
    # 백준 10951번 파이썬 A+B - 4
    import sys

    while 1:
        s = sys.stdin.readline().rstrip()
        if not s:
            break
        else:
            a, b = int(s[0]), int(s[-1])
            print(a + b)


def q10807():
    # 백준 10807번 파이썬 개수 세기
    n = int(input())
    lst = list(map(int, input().split()))
    v = int(input())
    print(lst.count(v))


def q10871():
    # 백준 10871번 파이썬 X보다 작은 수
    n, x = map(int, input().split())
    lst = list(map(int, input().split()))
    result = []
    for i in lst:
        if i < x:
            result.append(i)
    print(*result)


def q10818():
    # 백준 10818번 파이썬 최소, 최대
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    print(str(lst[0]) + ' ' + str(lst[-1]))


def q10810():
    # 백준 10810번 파이썬 공 넣기
    n, m = map(int, input().split())
    lst = [0] * (n + 1)
    for _ in range(m):
        i, j, k = map(int, input().split())
        for l in range(i, j + 1):
            lst[l] = k
    print(*lst[1:n + 1])


def q10813():
    # 백준 파이썬 공 바꾸기
    n, m = map(int, input().split())
    lst = [i for i in range(1, n + 1)]
    for _ in range(m):
        i, j = map(int, input().split())
        temp = lst[i - 1]
        lst[i - 1], lst[j - 1] = lst[j - 1], temp
    print(*lst)


def q5597():
    # 백준 5597번 파이썬 과제 안 내신 분..?
    lst = [i for i in range(1, 31)]
    for _ in range(28):
        lst.remove(int(input()))
    for result in lst:
        print(result)


def q3052():
    # 백준 3052번 파이썬 나머지
    lst = []
    for _ in range(10):
        n = int(input())
        lst.append(n % 42)
    lst = list(set(lst))
    print(len(lst))


def q10811():
    # 백준 10811번 파이썬 바구니 뒤집기
    n, m = map(int, input().split())
    lst = [i for i in range(1, n + 1)]
    for _ in range(m):
        i, j = map(int, input().split())
        lst[i - 1:j] = list(reversed(lst[i - 1:j]))
    print(*lst)


def q1546():
    # 백준 1546번 파이썬 평균
    n = int(input())
    lst = list(map(int, input().split()))
    max_val = max(lst)
    for i in range(len(lst)):
        lst[i] = lst[i] / max_val * 100
    print(sum(lst) / n)


def q27866():
    # 백준 27866번 파이썬 문자열
    s = input()
    i = int(input())
    print(s[i - 1])


def q2743():
    # 백준 2743번 파이썬 단어 길이 재기
    print(len(input()))


def q9086():
    # 백준 9086번 파이썬 문자열
    t = int(input())
    for _ in range(t):
        s = input()
        print(s[0] + s[-1])


def q11654():
    # 백준 11654번 파이썬 아스키 코드
    print(ord(input()))


def q11720():
    # 백준 11720번 파이썬 숫자의 합
    n = int(input())
    s = input()
    result = 0
    for i in range(n):
        result += int(s[i])
    print(result)


def q10809():
    # 백준 10809번 파이썬 알파벳 찾기
    s = input()
    alphabet = [chr(i) for i in range(97, 123)]
    result = [-1 for _ in range(len(alphabet))]
    for i in range(len(s)):
        if s[i] in alphabet:
            result[alphabet.index(s[i])] = s.index(s[i])
    print(*result)


def q1152():
    # 백준 1152번 파이썬 단어의 개수
    s = list(map(str, input().split()))
    print(len(s))


def q2908():
    # 백준 2908번 파이썬 상수
    a, b = map(str, input().split())
    new_a, new_b = '', ''
    for i in range(2, -1, -1):
        new_a += a[i]
        new_b += b[i]
    print(max(int(new_a), int(new_b)))


def q5622():
    # 백준 5622번 파이썬 다이얼
    s = input()
    dic = {3: ['A', 'B', 'C'], 4: ['D', 'E', 'F'], 5: ['G', 'H', 'I'], 6: ['J', 'K', 'L'], 7: ['M', 'N', 'O'],
           8: ['P', 'Q', 'R', 'S'], 9: ['T', 'U', 'V'], 10: ['W', 'X', 'Y', 'Z']}
    result = 0
    for i in range(len(s)):
        for key, item in dic.items():
            if s[i] in item:
                result += key
    print(result)


def q11718():
    # 백준 11718번 파이썬 그대로 출력하기
    import sys

    count = 0
    while count < 100:
        print(sys.stdin.readline().rstrip())
        count += 1


def q25083():
    # 백준 25083번 파이썬 새싹
    print(
        "         ,r'\"7" + "\n"
        "r`-_   ,'  ,/" + "\n"
        " \\. \". L_r'" + "\n"
        "   `~\\/" + "\n"
        "      |" + "\n"
        "      |"
    )


def q3033():
    # 백준 3033번 파이썬 킹, 퀸, 룩, 비숍, 나이트, 폰
    lst = list(map(int, input().split()))
    answer = [1, 1, 2, 2, 2, 8]
    result = []
    for i in range(6):
        result.append(answer[i] - lst[i])
    print(*result)


def q2444():
    # 백준 2444번 파이썬 별 찍기 - 7
    n = int(input())
    for i in range(n - 1, 0, -1):
        print((' ' * i) + ('*' * (2 * (n - i) - 1)))
    print('*' * (2 * n - 1))
    for i in range(1, n):
        print((' ' * i) + ('*' * (2 * (n - i) - 1)))


def q2738():
    # 백준 2738번 파이썬 행렬 덧셈
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    for i in range(n):
        b = list(map(int, input().split()))
        for j in range(m):
            a[i][j] += b[j]
    for i in range(n):
        print(*a[i])


def q2566():
    # 백준 2566번 파이썬 최댓값
    max_val = 0
    index = [1, 1]
    for i in range(1, 10):
        temp = list(map(int, input().split()))
        temp_max = max(temp)
        if max_val < temp_max:
            max_val = temp_max
            index[0] = i
            index[1] = temp.index(temp_max) + 1
    print(max_val)
    print(*index)


def q10798():
    # 백준 10798번 파이썬 세로읽기
    lst = []
    result = ''
    for _ in range(5):
        temp = list(input())
        for _ in range(15 - len(temp)):
            temp.append('')
        lst.append(temp)
    for i in range(15):
        for j in range(5):
            result += lst[j][i]
    print(result)


def q2745():
    # 백준 2745번 파이썬 진법 변환
    n, b = input().split()
    print(int(n, int(b)))


def q11005():
    # 백준 11005번 파이썬 진법 변환 2
    import sys

    n, b = map(int, sys.stdin.readline().split())
    dic = {}
    for i in range(10, 36):
        dic[i] = str(chr(55 + i))
    dic[0] = '0'
    result = ''
    while n > 0:
        remainder = n % b
        if b == 10:
            print(n)
            break
        elif remainder < 10:
            result = str(remainder) + result
        else:
            result = dic[remainder] + result
        n //= b
    print(result)


def q2720():
    # 백준 2720번 파이썬 세탁소 사장 동혁
    t = int(input())
    for _ in range(t):
        c = int(input())
        lst = [0, 0, 0, 0]
        while c:
            if c // 25 != 0:
                lst[0] += 1
                c -= 25
            elif c // 10 != 0:
                lst[1] += 1
                c -= 10
            elif c // 5 != 0:
                lst[2] += 1
                c -= 5
            else:
                lst [3] += 1
                c -= 1
        print(*lst)


def q2903():
    # 백준 2903번 파이썬 중앙 이동 알고리즘
    n = int(input())
    dp = [0] * 16
    dp[0] = 2
    for i in range(1, 16):
        dp[i] = dp[i - 1] + dp[i - 1] - 1
    print(dp[n] * dp[n])


def q2869():
    # 백준 2869번 파이썬 달팽이는 올라가고 싶다
    import math

    a, b, v = map(int, input().split())
    v -= a
    print(math.ceil(v / (a - b)) + 1)


def q2501():
    # 백준 2501번 파이썬 약수 구하기
    n, k = map(int, input().split())
    lst = []
    d = 1
    if n % 2 == 0:
        while n // 2 >= d:
            if n % d == 0:
                lst.append(d)
            d += 1
        lst.append(n)
    else:
        while n // 3 >= d:
            if n % d == 0:
                lst.append(d)
            d += 1
        lst.append(n)
    if len(lst) >= k:
        print(lst[k - 1])
    else:
        print(0)


def q1978():
    # 백준 1978번 파이썬 소수 찾기
    n = int(input())
    lst = list(map(int, input().split()))
    result = 0
    dp = [0] * 1001
    dp[1] = 1
    for i in range(2, 500):
        for j in range(2, 500):
            if i * j > 1000:
                continue
            dp[i * j] = 1
    for num in lst:
        if not dp[num]:
            result += 1
    print(result)


def q2581():
    # 백준 2581번 파이썬 소수
    m = int(input())
    n = int(input())
    dp = [0] * 10001
    dp[1] = 1
    s = []
    for i in range(2, 5001):
        for j in range(2, 5001):
            if i * j > 10000:
                continue
            dp[i * j] = 1
    for i in range(m, n + 1):
        if not dp[i]:
            s.append(i)
    if s:
        print(sum(s))
        print(min(s))
    else:
        print(-1)


def q27323():
    # 백준 27323번 파이썬 직사각형
    a = int(input())
    b = int(input())
    print(a * b)


def q1085():
    # 백준 1085번 파이썬 직사각형에서 탈출
    x, y, w, h = map(int, input().split())
    print(min(abs(w - x), abs(h - y), x, y))


def q15894():
    # 백준 15894번 파이썬 수학은 체육과목 입니다
    n = int(input())
    print(n * 4)


def q9063():
    # 백준 9063번 파이썬 대지
    n = int(input())
    xs = []
    ys = []
    for _ in range(n):
        x, y = map(int, input().split())
        xs.append(x)
        ys.append(y)
    print((max(ys) - min(ys)) * (max(xs) - min(xs)))


def q10101():
    # 백준 10101번 파이썬 삼각형 외우기
    lst = []
    for _ in range(3):
        lst.append(int(input()))

    if lst[0] + lst[1] + lst[2] == 180:
        if lst[0] == lst[1] == 60:
            print('Equilateral')
        elif lst[0] == lst[1] or lst[1] == lst[2] or lst[0] == lst[2]:
            print('Isosceles')
        else:
            print('Scalene')
    else:
        print('Error')


def q14215():
    # 백준 14215번 파이썬 세 막대
    lst = list(map(int, input().split()))
    lst.sort()
    result = 0
    if lst[0] + lst[1] > lst[2]:
        result = sum(lst)
    else:
        result = (lst[0] + lst[1]) * 2 - 1
    print(result)


def q24262():
    # 백준 24262번 파이썬 알고리즘 수업 - 알고리즘의 수행 시간 1
    print(1)
    print(0)


def q24263():
    # 백준 24263번 파이썬 알고리즘 수업 - 알고리즘의 수행 시간 2
    print(input())
    print(1)


def q24264():
    # 백준 24264번 파이썬 알고리즘 수업 - 알고리즘의 수행 시간 3
    n = int(input())
    print(n * n)
    print(2)


def q24265():
    # 백준 24265번 파이썬 알고리즘 수업 - 알고리즘의 수행 시간 4
    n = int(input())
    result = 0
    for i in range(1, n):
        result += i
    print(result)
    print(2)


def q24266():
    # 백준 24266번 파이썬 알고리즘 수업 - 알고리즘의 수행 시간 5
    n = int(input())
    print(n * n * n)
    print(3)


def q24267():
    # 백준 24267번 파이썬 알고리즘 수업 - 알고리즘의 수행 시간 6
    n = int(input())
    result = 0
    s = 0
    for i in range(1, n - 1):
        s += i
        result += s
    print(result)
    print(3)


def q2798():
    # 백준 2798번 파이썬 블랙잭
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    max_val = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if max_val < lst[i] + lst[j] + lst[k] <= m:
                    max_val = lst[i] + lst[j] + lst[k]
    print(max_val)


def q2231():
    # 백준 2231번 파이썬 분해합
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


def q19532():
    # 백준 19532번 파이썬 수학은 비대면강의입니다
    a, b, c, d, e, f = map(int, input().split())
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if a * x + b * y == c and d * x + e * y == f:
                print(x, y)


def q2750():
    # 백준 2750번 파이썬 수 정렬하기
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(int(input()))
    lst.sort()
    for num in lst:
        print(num)


def q2587():
    # 백준 2587번 파이썬 대표값2
    lst = []
    for _ in range(5):
        lst.append(int(input()))
    lst.sort()
    print(sum(lst) // 5)
    print(lst[2])


def q25303():
    # 백준 25303번 파이썬 커트라인
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    print(lst[k - 1])


def q10989():
    # 백준 10989번 파이썬 수 정렬하기 3
    import sys

    n = int(sys.stdin.readline())
    dic = {}
    for _ in range(n):
        temp = int(sys.stdin.readline())
        if temp in dic:
            dic[temp] += 1
        else:
            dic[temp] = 1
    dic = sorted(dic.items())
    for key, val in dic:
        for _ in range(val):
            print(key)


def q15439():
    # 백준 15439번 파이썬 베라의 패션
    n = int(input())
    print(n ** 2 - n)


def q24723():
    # 백준 24723번 파이썬 녹색거탑
    n = int(input())
    print(2 ** n)


def q11050():
    # 백준 11050번 파이썬 이항 계수 1
    n, k = map(int, input().split())
    fact_n = 1
    fact_k = 1
    fact_kn = n - k
    if not fact_kn:
        fact_kn = 1
    for i in range(1, n + 1):
        fact_n *= i
    for i in range(1, k + 1):
        fact_k *= i
    for i in range(1, fact_kn + 1):
        fact_k *= i
    print(fact_n // fact_k)


def q1037():
    # 백준 1037번 파이썬 약수
    n = int(input())
    lst = list(map(int, input().split()))
    if n > 1:
        print(max(lst) * min(lst))
    else:
        print(lst[0] ** 2)


def q27433():
    # 백준 27433번 파이썬 팩토리얼 2
    n = int(input())

    def fact(a):
        if a <= 1:
            return 1
        else:
            return a * fact(a - 1)

    print(fact(n))


def q10870():
    # 백준 10870번 파이썬 피보나치 수 5
    n = int(input())

    def fibo(a):
        if a <= 0:
            return 0
        elif a == 1:
            return 1
        else:
            return fibo(a - 2) + fibo(a - 1)
    print(fibo(n))


def q25501():
    # 백준 25501번 파이썬 재귀의 귀재
    n = int(input())

    def recursion(s, l, r, c):
        c += 1
        if l >= r:
            return 1, c
        elif s[l] != s[r]:
            return 0, c
        else:
            return recursion(s, l + 1, r - 1, c)

    def is_palindrome(s, c):
        return recursion(s, 0, len(s) - 1, c)

    for _ in range(n):
        string = input()
        count = 0
        print(*is_palindrome(string, count))


def q2748():
    # 백준 2748번 파이썬 피보나치 수 2
    n = int(input())
    dp = [0] * 91
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
    print(dp[n])


def q17202():
    # 백준 17202번 파이썬 핸드폰 번호 궁합
    a = list(map(int, input()))
    b = list(map(int, input()))
    dp = [[] for _ in range(16)]
    lst = []
    for i in range(8):
        lst.append(a.pop(0))
        lst.append(b.pop(0))
    for i in range(len(lst) - 1):
        dp[0].append((lst[i] + lst[i + 1]) % 10)
    for i in range(1, 16):
        for j in range(len(dp[i - 1]) - 1):
            dp[i].append((dp[i - 1][j] + dp[i - 1][j + 1]) % 10)
    print(''.join(map(str, dp[13])))


def q17608():
    # 백준 17608번 파이썬 막대기
    import sys

    n = int(sys.stdin.readline())
    lst = []
    count = 1
    for _ in range(n):
        lst.append(int(sys.stdin.readline()))
    lst.reverse()
    max_val = lst[0]
    for i in range(n):
        if lst[i] > max_val:
            max_val = lst[i]
            count += 1
    print(count)


def q2605():
    # 백준 2605번 파이썬 줄 세우기
    n = int(input())
    lst = list(map(int, input().split()))
    order = []
    for i in range(1, n + 1):
        order.insert(lst[i - 1], i)
    order.reverse()
    print(*order)


def q12605():
    # 백준 12605번 파이썬 단어순서 뒤집기
    n = int(input())
    words = []
    for _ in range(n):
        lst = list(map(str, input().split()))
        lst.reverse()
        words.append(lst)
    for i in range(n):
        print(f'Case #{i + 1}:', *words[i])


def q27160():
    # 백준 27160번 파이썬 할리갈리
    n = int(input())
    dic = {}
    for _ in range(n):
        fruit, ea = input().split()
        if fruit in dic.keys():
            dic[fruit] += int(ea)
        else:
            dic[fruit] = int(ea)
    print('YES' if 5 in dic.values() else 'NO')


def q11531():
    # 백준 11531번 파이썬 ACM 대회 채점
    dic = {}
    while 1:
        lst = input().split()
        if int(lst[0]) == -1:
            break
        if lst[1] not in dic.keys():
            dic[lst[1]] = [False, 0]
        if lst[2] == 'right':
            dic[lst[1]][0] = True
            dic[lst[1]][1] += int(lst[0])
        else:
            dic[lst[1]][1] += 20
    solved = 0
    penalties = 0
    for _, item in dic.items():
        if item[0]:
            solved += 1
            penalties += item[1]
    print(solved, penalties)


def q29701():
    # 백준 29701번 파이썬 모스 부호
    n = int(input())
    lst = input().split()
    dic = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
        '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
        '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0',
        '--..--': ',', '.-.-.-': '.', '..--..': '?', '---...': ':', '-....-': '-', '.--.-.': '@'
    }
    for char in lst:
        print(dic[char], end='')


def q30034():
    # 백준 30034번 파이썬 Slice String
    n = int(input())
    slice_char = input().split()
    m = int(input())
    slice_num = input().split()
    slices = slice_char + slice_num
    k = int(input())
    merge = input().split()
    for char in merge:
        while char in slices:
            slices.remove(char)
    s = int(input())
    string = input().split()
    for char in slices:
        index = 0
        while index < len(string):
            if char in string[index]:
                temp = list(string[index].split(char))
                string.pop(index)
                for i in range(len(temp)):
                    string.insert(index + i, temp[i])
            index += 1
    for char in string:
        if char:
            print(char)


def q15098():
    # 백준 15098번 파이썬 No Duplicates
    lst = input().split()
    dic = {}
    is_dup = True
    while lst:
        current = lst.pop()
        if current in dic.keys():
            is_dup = False
            break
        else:
            dic[current] = 1
    print('yes' if is_dup else 'no')


def q25593():
    # 백준 25593번 파이썬 근무 지옥에 빠진 푸앙이 (Small)
    n = int(input())
    dic = {}
    lst = [4, 6, 4, 10]
    for _ in range(n):
        for time in lst:
            workers = input().split()
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


def q31562():
    # 백준 31562번 파이썬 전주 듣고 노래 맞히기
    n, m = map(int, input().split())
    music = {}
    for _ in range(n):
        lst = input().split()
        music[lst[1]] = lst[2:5]
    for _ in range(m):
        lst = input().split()
        count = 0
        result = ''
        for key, val in music.items():
            if val == lst:
                result = key
                count += 1
        if count > 1:
            print('?')
        elif count:
            print(result)
        else:
            print('!')


def q9933():
    # 백준 9933번 파이썬 민균이의 비밀번호
    n = int(input())
    dic = {}
    for _ in range(n):
        s = input()
        lst = list(s)
        lst.reverse()
        reverse = ''
        for char in lst:
            reverse += char
        dic[s] = reverse
    result = ''
    key, val = list(dic.keys()), list(dic.values())
    for i in range(n):
        if key[i] == val[i]:
            result = key[i]
            break
        for j in range(i, n):
            if key[i] == val[j]:
                result = key[i]
                break
    print(len(result), result[len(result) // 2])


def q1009():
    # 백준 1009번 파이썬 분산처리
    import sys

    t = int(sys.stdin.readline())
    for _ in range(t):
        a, b = map(int, sys.stdin.readline().split())
        a = a % 10

        if a == 0:
            print(10)
        elif a == 1 or a == 5 or a == 6:
            print(a)
        elif a == 4 or a == 9:
            b = b % 2
            if b == 1:
                print(a)
            else:
                print((a * a) % 10)
        else:
            b = b % 4
            if b == 0:
                print((a ** 4) % 10 % 10 % 10)
            else:
                print((a ** b) % 10 % 10 % 10)


def q14720():
    # 백준 14720번 파이썬 우유 축제
    n = int(input())
    lst = list(map(int, input().split()))
    result = 0
    chk = 0
    for num in lst:
        if chk == 0 and num == 0:
            chk = 1
            result += 1
        if chk == 1 and num == 1:
            chk = 2
            result += 1
        if chk == 2 and num == 2:
            chk = 0
            result += 1
    print(result)


def q11034():
    # 백준 11034번 파이썬 캥거루 세마리2
    while 1:
        try:
            a, b, c = map(int, input().split())
            print(max(b - a - 1, c - b - 1))
        except:
            break


def q28014():
    # 백준 28014번 파이썬 첨탑 밀어서 부수기
    n = int(input())
    lst = list(map(int, input().split()))
    result = 1
    for i in range(1, n):
        if lst[i] >= lst[i - 1]:
            result += 1
    print(result)


def q30018():
    # 백준 30018번 파이썬 타슈
    n = int(input())
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    result = 0
    for i in range(n):
        chk = lst1[i] - lst2[i]
        if chk > 0:
            result += chk
    print(result)


def q5585():
    # 백준 5585번 파이썬 거스름돈
    n = int(input())
    n = 1000 - n
    result = 0
    while n > 0:
        if n // 500:
            n -= 500
            result += 1
        elif n // 100:
            n -= 100
            result += 1
        elif n // 50:
            n -= 50
            result += 1
        elif n // 10:
            n -= 10
            result += 1
        elif n // 5:
            n -= 5
            result += 1
        else:
            n -= 1
            result += 1
    print(result)


def q2864():
    # 백준 2864번 파이썬 5와 6의 차이
    a, b = input().split()
    min_lst = [a, b]
    max_lst = [a, b]
    for i in range(2):
        temp = ''
        for char in min_lst[i]:
            if char == '6':
                temp += '5'
            else:
                temp += char
        min_lst[i] = temp
        temp = ''
        for char in max_lst[i]:
            if char == '5':
                temp += '6'
            else:
                temp += char
        max_lst[i] = temp
    print(int(min_lst[0]) + int(min_lst[1]), int(max_lst[0]) + int(max_lst[1]))


def q14487():
    # 백준 14487번 파이썬 욱제는 효도쟁이야!!
    n = int(input())
    lst = list(map(int, input().split()))
    lst.remove(max(lst))
    print(sum(lst))


def q22864():
    # 백준 22864번 파이썬 피로도
    a, b, c, m = map(int, input().split())
    result = 0
    tired = 0
    for _ in range(24):
        if tired + a <= m:
            tired += a
            result += b
        else:
            tired -= c
            if tired < 0:
                tired = 0
    print(result)


def q18238():
    # 백준 18238번 파이썬 ZOAC 2
    import collections
    deq = collections.deque()

    s = input()
    for i in range(26):
        deq.append(chr(i + 65))
    result = 0
    for char in s:
        temp = 0
        for i in range(26):
            if char == deq[i]:
                temp += i
                break
            if char == deq[-i]:
                temp += -i
                break
        if temp < 0:
            for _ in range(abs(temp)):
                deq.appendleft(deq.pop())
        else:
            for _ in range(temp):
                deq.append(deq.popleft())
        result += abs(temp)
    print(result)


def q21313():
    # 백준 21313번 파이썬 문어
    n = int(input())
    result = [1, 2]
    for i in range(2, n - 1):
        if result[-1] == 2:
            result.append(1)
        else:
            result.append(2)
    if n % 2:
        result.append(3)
    else:
        result.append(2)
    print(*result)


def q28062():
    # 백준 28062번 파이썬 준석이의 사탕 사기
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    result = sum(lst)
    if result % 2:
        for i in lst:
            if (result - i) % 2:
                continue
            else:
                result -= i
                break
    print(0 if result % 2 else result)


def q14471():
    # 백준 14471번 파이썬 포인트 카드
    n, m = map(int, input().split())
    lst = []
    for _ in range(m):
        a, b = map(int, input().split())
        lst.append([a, b])
    lst = sorted(lst, key=lambda x: -x[0])
    prize = 0
    price = 0
    for i in lst:
        if prize >= m - 1:
            break
        if i[0] >= n:
            prize += 1
            continue
        else:
            price += n - i[0]
            prize += 1
    print(price)


def q28323():
    # 백준 28323번 파이썬 불안정한 수열
    n = int(input())
    lst = list(map(int, input().split()))
    mod0 = []
    mod1 = []
    for i in lst:
        if not mod0 and not i % 2:
            mod0.append(i)
        if mod0:
            if mod0[-1] % 2 and not i % 2:
                mod0.append(i)
            elif not mod0[-1] % 2 and i % 2:
                mod0.append(i)
            else:
                continue
    for i in lst:
        if not mod1 and i % 2:
            mod1.append(i)
        if mod1:
            if mod1[-1] % 2 and not i % 2:
                mod1.append(i)
            elif not mod1[-1] % 2 and i % 2:
                mod1.append(i)
            else:
                continue
    print(max(len(mod0), len(mod1)))


def q30700():
    # 백준 30700번 파이썬 KOREA 문자열 만들기
    s = input()
    result = ''
    for char in s:
        if not result and char == 'K':
            result += char
        if result:
            if result[-1] == 'K' and char == 'O':
                result += char
            if result[-1] == 'O' and char == 'R':
                result += char
            if result[-1] == 'R' and char == 'E':
                result += char
            if result[-1] == 'E' and char == 'A':
                result += char
            if result[-1] == 'A' and char == 'K':
                result += char
    print(len(result))


def q30019():
    # 백준 30019번 파이썬 강의실 예약 시스템
    import sys

    n, m = map(int, input().split())
    dic = {}
    for _ in range(m):
        k, s, e = map(int, sys.stdin.readline().split())
        if k not in dic:
            dic[k] = (s, e)
            print('YES')
        else:
            if s >= dic[k][1]:
                dic[k] = (s, e)
                print('YES')
            else:
                print('NO')


def q4796():
    # 백준 4796번 파이썬 캠핑
    case = 1
    while 1:
        l, p, v = map(int, input().split())
        result = 0

        if l == p == v == 0:
            break
        while v > 0:
            if v > l:
                result += l
            else:
                result += v
            v -= p
        print(f'Case {case}: {result}')
        case += 1


def q2810():
    # 백준 2810번 파이썬 컵홀더
    n = int(input())
    s = list(input())
    result = 1
    index = 0
    while 1:
        try:
            if s[index] == 'S':
                result += 1
            if s[index] == 'L':
                result += 1
                s[index + 1] = ''
            index += 1
        except:
            break
    print(result if result < n else n)


def q14659():
    # 백준 14659번 파이썬 한조서열정리하고옴ㅋㅋ
    n = int(input())
    lst = list(map(int, input().split()))
    result = 0
    max_val = 0
    temp = 0
    for i in lst:
        if i > max_val:
            max_val = i
            temp = 0
        else:
            temp += 1
        result = max(result, temp)
    print(result)


def q17224():
    # 백준 17224번 파이썬 APC는 왜 서브태스크 대회가 되었을까?
    n, l, k = map(int, input().split())
    lst = []
    for _ in range(n):
        s1, s2 = map(int, input().split())
        lst.append((s1, s2))
    lst = sorted(lst, key=lambda x: (x[1], x[0]))
    solved = 0
    point = 0
    for i in lst:
        if solved >= k:
            break
        if i[1] <= l:
            point += 140
            solved += 1
        elif i[0] <= l:
            point += 100
            solved += 1
        else:
            continue
    print(point)


def q25400():
    # 백준 25400번 파이썬 제자리
    n = int(input())
    lst = list(map(int, input().split()))
    remove = 0
    index = 0
    num = 1
    while index < len(lst):
        if lst[index] == num:
            index += 1
            num += 1
        else:
            remove += 1
            index += 1
    print(remove)


def q15881():
    # 백준 15881번 파이썬 Pen Pineapple Apple Pen
    n = int(input())
    s = input()
    chk = 'pPAp'
    index = 0
    result = 0
    for i in range(n):
        if s[i] == chk[index]:
            index += 1
        elif s[i] == 'p':
            index = 1
        else:
            index = 0
        if index == 4:
            result += 1
            index = 0
    print(result)


def q27961():
    # 백준 27961번 파이썬 고양이는 많을수록 좋다
    n = int(input())
    default = 0
    result = 0
    while 1:
        if default >= n:
            break
        default = max(default + 1, default * 2)
        result += 1
    print(result)


def q25176():
    # 백준 25176번 파이썬 청정수열 (Easy)
    result = 1
    for i in range(1, int(input()) + 1):
        result *= i
    print(result)


def q27930():
    # 백준 27930번 파이썬 당신은 운명을 믿나요?
    s = input()
    korea = ''
    yonsei = ''
    chk1 = 'KOREA'
    chk2 = 'YONSEI'
    index1 = 0
    index2 = 0
    for char in s:
        if korea == 'KOREA':
            print('KOREA')
            break
        if yonsei == 'YONSEI':
            print('YONSEI')
            break
        if char == chk1[index1]:
            korea += char
            index1 += 1
        if char == chk2[index2]:
            yonsei += char
            index2 += 1


def q19564():
    # 백준 19564번 파이썬 반복
    s = input()
    result = 1
    for i in range(len(s) - 1):
        if s[i] >= s[i + 1]:
            result += 1
    print(result)


def q15786():
    # 백준 15786번 파이썬 Send me the money
    n, m = map(int, input().split())
    s = input()
    for _ in range(m):
        p = input()
        index = 0
        chk = False
        for char in p:
            if char == s[index]:
                index += 1
            if index == len(s):
                chk = True
                break
        print('true' if chk else 'false')


def q28063():
    # 백준 28063번 파이썬 동전 복사
    n = int(input())
    x, y = map(int, input().split())
    if n == 1:
        print(0)
    elif n == 2:
        print(2)
    else:
        if (x == 1 and y == 1) or (x == 1 and y == n) or (x == n and y == 1) or (x == n and y == n):
            print(2)
        elif (x == 1 and y < n) or (x < n and y == n) or (x < n and y == 1) or (x == n and y < n):
            print(3)
        else:
            print(4)


def q31067():
    # 백준 31067번 파이썬 다오의 경주 대회
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    result = 0
    chk = True
    for i in range(n - 1):
        if lst[i] < lst[i + 1]:
            continue
        elif lst[i] < lst[i + 1] + k:
            result += 1
            lst[i + 1] += k
            continue
        else:
            chk = False
            break
    print(result if chk else -1)


def q30236():
    # 백준 30236번 파이썬 증가 수열
    import sys

    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        lst = list(map(int, sys.stdin.readline().split()))
        result = []
        current = 0
        for i in range(n):
            current += 1
            if lst[i] != current:
                result.append(current)
            else:
                current += 1
                result.append(current)
        print(result[-1])


def q9329():
    # 백준 9329번 파이썬 패스트 푸드 상금
    import sys

    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        lst = []
        for _ in range(n):
            temp = list(map(int, sys.stdin.readline().split()))
            dic = {}
            for j in range(1, temp[0] + 1):
                dic[temp[j]] = 0
            lst.append([dic, temp[-1]])
        stickers = list(map(int, sys.stdin.readline().split()))
        for i in range(1, m + 1):
            for j in lst:
                if i in j[0]:
                    j[0][i] += stickers[i - 1]
                    break
        result = 0
        for i in lst:
            result += min(i[0].values()) * i[1]
        print(result)


def q27951():
    # 백준 27951번 파이썬 옷걸이
    n = int(input())
    lst = list(map(int, input().split()))
    u, d = map(int, input().split())
    for i in lst:
        if i == 1:
            u -= 1
        if i == 2:
            d -= 1
    if u < 0 or d < 0:
        print('NO')
        return
    result = ''
    for i in lst:
        if i == 3:
            if u:
                u -= 1
                result += 'U'
            else:
                d -= 1
                result += 'D'
        else:
            if i == 1:
                result += 'U'
            else:
                result += 'D'
    print('YES')
    print(result)


def q1259():
    # 백준 1259번 파이썬 팰린드롬수
    while 1:
        s = input()
        if s == '0':
            break
        print('yes' if s == s[::-1] else 'no')


def q4153():
    # 백준 4153번 파이썬 직각삼각형
    while 1:
        a, b, c = map(int, input().split())
        if a == b == c == 0:
            break
        lst = sorted([a, b, c])
        print('right' if lst[0] ** 2 + lst[1] ** 2 == lst[2] ** 2 else 'wrong')


def q15829():
    # 백준 15829번 파이썬 Hashing
    l = int(input())
    s = input()
    result = 0

    def do_hash(string, i):
        return (ord(string) - 96) * (31 ** i)

    for i in range(l):
        result += do_hash(s[i], i)
    print(result % 1234567891)


def q2309():
    # 백준 2309번 일곱 난쟁이 파이썬
    lst = [int(input()) for _ in range(9)]
    s = sum(lst)
    for i in range(9):
        flag = False
        for j in range(i + 1, 9):
            if s - (lst[i] + lst[j]) == 100:
                a, b = lst[i], lst[j]
                lst.remove(a)
                lst.remove(b)
                flag = True
                break
        if flag:
            break
    print(*sorted(lst))


def q10163():
    # 백준 10163번 색종이 파이썬
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    lst.reverse()
    result = []
    dp = [[0] * 1001 for _ in range(1001)]
    for i in lst:
        width = 0
        for j in range(i[0], i[0] + i[2]):
            for k in range(i[1], i[1] + i[3]):
                if dp[j][k] == 0:
                    dp[j][k] = 1
                    width += 1
        result.append(width)
    result.reverse()
    for i in result:
        print(i)


def q8320():
    # 백준 8320번 직사각형을 만드는 방법 파이썬
    n = int(input())
    result = n
    for i in range(2, 101):
        result += max(0, n // i - (i - 1))
    print(result)


def q3985():
    # 백준 3985번 롤 케이크 파이썬
    l = int(input())
    n = int(input())
    dp = [0] * (l + 1)
    large1, index1, large2, index2 = 0, 0, 0, 0
    for i in range(1, n + 1):
        p, k = map(int, input().split())
        cnt = 0
        if k - p > large1:
            large1 = k - p
            index1 = i
        for j in range(p, k + 1):
            if not dp[j]:
                dp[j] = i
                cnt += 1
        if cnt > large2:
            large2 = cnt
            index2 = i
    print(index1)
    print(index2)


def q13300():
    # 백준 13300번 방 배정 파이썬
    import math

    n, k = map(int, input().split())
    dic1 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    dic2 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for _ in range(n):
        s, y = map(int, input().split())
        if s:
            dic1[y] += 1
        else:
            dic2[y] += 1
    result = 0
    for val in dic1.values():
        result += math.ceil(val / k)
    for val in dic2.values():
        result += math.ceil(val / k)
    print(result)


def q14696():
    # 백준 14696번 딱지놀이 파이썬
    n = int(input())
    for _ in range(n):
        a = {4: 0, 3: 0, 2: 0, 1: 0}
        b = {4: 0, 3: 0, 2: 0, 1: 0}
        lst1 = list(map(int, input().split()))
        lst2 = list(map(int, input().split()))
        for i in range(1, lst1[0] + 1):
            a[lst1[i]] += 1
        for i in range(1, lst2[0] + 1):
            b[lst2[i]] += 1
        winner = -1
        for i in range(4, 0, -1):
            if a[i] > b[i]:
                winner = 0
                break
            if a[i] < b[i]:
                winner = 1
                break
        print('A' if winner == 0 else 'B' if winner == 1 else 'D')


def q10718():
    # 백준 10718번 We love kriii 파이썬
    print("강한친구 대한육군")
    print("강한친구 대한육군")


def q2741():
    # 백준 2741번 N 찍기 파이썬
    for i in range(1, int(input()) + 1):
        print(i)


def q2742():
    # 백준 2742번 기찍 N 파이썬
    for i in range(int(input()), 0, -1):
        print(i)


def q1110():
    # 백준 1110번 더하기 사이클 파이썬
    n = int(input())
    if n // 10:
        n2 = (n % 10 * 10) + ((n // 10 + n) % 10 % 10)
    else:
        n2 = n * 10 + n
    result = 1
    while n != n2:
        result += 1
        if n2 // 10:
            n2 = (n2 % 10 * 10) + ((n2 // 10 + n2) % 10 % 10)
        else:
            n2 = n2 * 10 + n2
    print(result)


def q2577():
    # 백준 2577번 숫자의 개수 파이썬
    lst = [int(input()) for _ in range(3)]
    val = str(eval('*'.join(map(str, lst))))
    dic = {str(i): 0 for i in range(10)}
    for char in val:
        dic[char] += 1
    for val in dic.values():
        print(val)


def q2440():
    # 백준 2440번 별 찍기 - 3 파이썬
    for i in range(int(input()), 0, -1):
        print('*' * i)


def q10250():
    # 백준 10250번 ACM 호텔 파이썬
    t = int(input())
    for _ in range(t):
        h, w, n = map(int, input().split())
        if n % h:
            front = n % h * 100
            back = n // h + 1
        else:
            front = h * 100
            back = n // h
        print(front + back)


def q2441():
    # 백준 2441번 별 찍기 - 4 파이썬
    n = int(input())
    for i in range(n):
        print(' ' * i + '*' * (n - i))


def q2920():
    # 백준 2920번 음계 파이썬
    lst = list(map(int, input().split()))
    desc = [8, 7, 6, 5, 4, 3, 2, 1]
    asc = [1, 2, 3, 4, 5, 6, 7, 8]
    if lst == asc:
        print('ascending')
    elif lst == desc:
        print('descending')
    else:
        print('mixed')


def q2475():
    # 백준 2475번 검증수 파이썬
    lst = list(map(int, input().split()))
    result = 0
    for i in range(5):
        result += lst[i] ** 2
    print(result % 10)


def q1924():
    # 백준 1924번 2007년 파이썬
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
              7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    weeks = {0: 'SUN', 1: 'MON', 2: 'TUE', 3: 'WED', 4: 'THU', 5: 'FRI', 6: 'SAT'}
    x, y = map(int, input().split())
    for i in range(1, x):
        y += months[i]
    print(weeks[y % 7])


def q2442():
    # 백준 2442번 별 찍기 - 5 파이썬
    n = int(input())
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))


def q11721():
    # 백준 11721번 열 개씩 끊어 출력하기 파이썬
    s = input()
    length = len(s)
    for _ in range(length // 10 + 1):
        print(s[:10])
        s = s[10:]


def q11719():
    # 백준 11719번 그대로 출력하기 2 파이썬
    while 1:
        try:
            print(input())
        except:
            break


def q2446():
    # 백준 2446번 별 찍기 - 9 파이썬
    n = int(input())
    for i in range(n):
        print(' ' * i + '*' * (2 * n - (2 * i + 1)))
    for i in range(1, n):
        print(' ' * (n - (i + 1)) + '*' * (2 * i + 1))


def q2747():
    # 백준 2747번 피보나치 수 파이썬
    n = int(input())
    dp = [0] * 46
    dp[1], dp[2] = 1, 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[n])


def q10808():
    # 백준 10808번 알파벳 개수 파이썬
    s = input()
    alpha = {chr(i): 0 for i in range(97, 123)}
    for i in s:
        alpha[i] += 1
    print(*alpha.values())
q10808()