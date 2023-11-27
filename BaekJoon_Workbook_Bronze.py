

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


def q2609():
    # 최대공약수와 최소공배수
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
    # 단어 공부
    s = input().upper()
    dp = [0] * 26
    for char in s:
        dp[ord(char) - 65] += 1
    if dp.count(max(dp)) >= 2:
        print('?')
    else:
        print(chr(dp.index(max(dp)) + 65))


def q4344():
    # 평균은 넘겠지
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
    # 명령 프롬프트
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
    # 최댓값
    lst = []
    for _ in range(9):
        lst.append(int(input()))
    print(max(lst))
    print(lst.index(max(lst)) + 1)


def q10872():
    # 팩토리얼
    n = int(input())

    def factor(num):
        if num <= 1:
            return 1
        else:
            return num * factor(num - 1)
    print(factor(n))


def q23971():
    # ZOAC 4
    import math
    h, w, n, m = map(int, input().split())
    print(math.ceil(h / (n + 1)) * math.ceil(w / (m + 1)))


def q5073():
    # 삼각형과 세 변
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
    # 벌집
    n = int(input())
    index = 1
    first = 1
    prod = 6
    while first < n:
        first += prod * index
        index += 1
    print(index)


def q13458():
    # 시험 감독
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
    # ??!
    s = input()
    print(s + '??!')


def q18108():
    # 1998년생인 내가 태국에서는 2541년생?!
