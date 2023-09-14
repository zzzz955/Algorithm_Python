# Python 배우기 (1~50)
# https://www.acmicpc.net/workbook/view/459


def q2557():
    # Hello World
    print('Hello World!')


def q1000(a, b):
    # A+B
    print(a + b)


def q10998(a, b):
    # A×B
    print(a * b)


def q1001(a, b):
    # A-B
    print(a - b)


def q1008(a, b):
    # A/B
    print(a / b)


def q10869(a, b):
    # 사칙연산
    print(a + b)
    print(a - b)
    print(a * b)
    print(int(a // b))
    print(a % b)


def q10430(a, b, c):
    # 나머지
    print((a + b) % c)
    print(((a % c) + (b % c)) % c)
    print((a * b) % c)
    print((a % c) * (b % c))


def q2558(a, b):
    print(a + b)


def q2588(a, b):
    # 곱셈
    div = 1
    while b // div > 0:
        print(a * ((b // div) % 10))
        div *= 10
    print(a * b)


def q3046(r1, s):
    # R2
    r2 = 2 * s - r1
    print(r2)


def q2163(n, m):
    # 초콜릿 자르기
    divided_list = []
    size = n * m
    for i in range(1, size+1):
        if size % i == 0:
            divided_list.append(i)
    print(len(divided_list))


def q11021(t):
    # A+B - 7
    input_list = []
    for _ in range(t):
        input_list.append(list(map(int, input().split())))
    for i in range(t):
        print(f'Case #{i+1}: {sum(input_list[i])}')


def q11022(t):
    # A+B - 8
    input_list = []
    for _ in range(t):
        input_list.append(list(map(int, input().split())))
    for i in range(t):
        print(f'Case #{i+1}: {input_list[i][0]} + {input_list[i][1]} = {sum(input_list[i])}')


def q10699():
    # 오늘 날짜
    import datetime
    print(datetime.datetime.now().date())


def q7287():
    # 등록
    # 웹사이트 크롤링 불가
    import requests
    import bs4

    myId = "zzzz955"
    URL = "https://www.acmicpc.net/user/" + myId
    response = requests.get(URL)

    soup = bs4.BeautifulSoup(response.text, "html.parser")
    print(soup.find('div').find('span', {'id': 'u-solved'}).text)


def q2525(a, b, c):
    # 오븐 시계
    b += c
    if b > 60:
        b = b - 60
        a += 1
    if a > 24:
        a = a - 24
    print(f'{a} {b}')


def q2530(a, b, c, d):
    # 인공지능 시계
    c += d
    while a >= 24 or b >= 60 or c >= 60:
        if c >= 60:
            c -= 60
            b += 1
        if b >= 60:
            b -= 60
            a += 1
        if a >= 24:
            a -= 24
    print(f'{a} {b} {c}')


def q2914(a, i):
    # 저작권
    x = a * i
    if a != 0:
        x -= a-1
    return x


def q5355(d, op1=None, op2=None, op3=None):
    # 화성 수학
    d = float(d)

    if op1 == '@':
        d *= 3
    elif op1 == '%':
        d += 5
    elif op1 == '#':
        d -= 7

    if op2 == '@':
        d *= 3
    elif op2 == '%':
        d += 5
    elif op2 == '#':
        d -= 7

    if op3 == '@':
        d *= 3
    elif op3 == '%':
        d += 5
    elif op3 == '#':
        d -= 7

    print("{:.2f}".format(d))


def q2675(r, s):
    # 문자열 반복
    string = ''
    for i in range(len(s)):
        string += s[i]*r
    print(string)


def q2935(a, op, b):
    # 소음
    if op == '*':
        result = a * b
    elif op == '+':
        result = a + b
    else:
        result = None
    print(result)


def q9498(n):
    # 시험 성적
    if 90 <= n <= 100:
        print('A')
    elif 80 <= n < 90:
        print('B')
    elif 70 <= n < 80:
        print('C')
    elif 60 <= n < 70:
        print('D')
    else:
        print('F')


def q10817(a, b, c):
    # 세 수
    print(sorted([a, b, c], reverse=True)[1])


def q11653(n):
    # 소인수분해
    divide = 2
    while n != 1:
        if n % divide == 0:
            n = n // divide
            print(divide)
            divide = 2
            continue
        divide += 1


def q1789(s):
    # 수들의 합
    index = 0
    num = 0
    plus = 1
    while num < s:
        num += plus
        plus += 1
        index += 1
    if num > s:
        index -= 1
    print(index)


def q2753(y):
    # 윤년
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        print(1)
    else:
        print(0)


def q10039():
    # 평균 점수
    num_list = []
    for i in range(5):
        point = int(input())
        if point < 40:
            point = 40
        num_list.append(point)
    print(sum(num_list) // 5)


def q1934(a, b):
    # 최소공배수
    divisor = []
    common_divisor = []
    for i in range(1, a):
        if a % i == 0:
            divisor.append(i)
    for i in range(1, b):
        if b % i == 0:
            divisor.append(i)
    for num in divisor:
        if a % num == 0 and b % num == 0:
            common_divisor.append(num)
    print(a * b // max(common_divisor))


