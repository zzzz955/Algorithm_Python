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


def q2480(a, b, c):
    # 주사위 세개
    if a == b == c:
        result = 10000 + a * 1000
    elif a == b or a == c:
        result = 1000 + a * 100
    elif b == a or b == c:
        result = 1000 + b * 100
    elif c == a or c == b:
        result = 1000 + c * 100
    elif a != b and a != c and b != c:
        result = max(a, b, c) * 100
    print(result)


def q4101(a, b):
    # 크냐?
    if a < 1 or b < 1:
        return
    if a > b:
        print('Yes')
    else:
        print('No')


def q10156(k, n, m):
    # 과자
    sum_price = k * n
    if m >= sum_price:
        print(0)
    elif m < sum_price:
        print(sum_price - m)
    else:
        return


def q3009():
    # 네 번째 점
    first_spot = list(map(int, input().split()))
    second_spot = list(map(int, input().split()))
    third_spot = list(map(int, input().split()))
    fourth_spot = [0, 0]

    if first_spot[0] == second_spot[0]:
        fourth_spot[0] = third_spot[0]
    elif first_spot[0] == third_spot[0]:
        fourth_spot[0] = second_spot[0]
    elif second_spot[0] == third_spot[0]:
        fourth_spot[0] = first_spot[0]
    else:
        return

    if first_spot[1] == second_spot[1]:
        fourth_spot[1] = third_spot[1]
    elif first_spot[1] == third_spot[1]:
        fourth_spot[1] = second_spot[1]
    elif second_spot[1] == third_spot[1]:
        fourth_spot[1] = first_spot[1]
    else:
        return
    print(f'{fourth_spot[0]} {fourth_spot[1]}')


def q2476():
    # 주사위 게임
    t = int(input())
    users_data = []
    prize_result = []
    for i in range(t):
        dice_val = list(map(int, input().split()))
        users_data.append(dice_val)
    def dice(data_list):
        if data_list[0] == data_list[1] == data_list[2]:
            result = 10000 + data_list[0] * 1000
        elif data_list[0] == data_list[1]:
            result = 1000 + data_list[0] * 100
        elif data_list[0] == data_list[2]:
            result = 1000 + data_list[0] * 100
        elif data_list[1] == data_list[2]:
            result = 1000 + data_list[1] * 100
        else:
            result = max(data_list) * 100
        return result
    for data in users_data:
        result_price = dice(data)
        prize_result.append(result_price)
    print(max(prize_result))


def q2754():
    # 학점계산
    grade = input()
    temp = grade[0]
    if len(grade) == 2:
        temp2 = grade[1]
    else:
        temp2 = ''
    if temp == 'A':
        point = 4.0
    elif temp == 'B':
        point = 3.0
    elif temp == 'C':
        point = 2.0
    elif temp == 'D':
        point = 1.0
    elif temp == 'F':
        point = 0.0
    else:
        return
    if temp2 == '+':
        point += 0.3
    elif temp2 == '-':
        point -= 0.3
    else:
        pass
    print(point)


def q2884():
    # 알람 시계
    H, M = map(int, input().split())

    total_minutes = H * 60 + M

    new_total_minutes = total_minutes - 45

    if new_total_minutes < 0:
        new_total_minutes += 24 * 60

    new_H = new_total_minutes // 60
    new_M = new_total_minutes % 60

    print(f'{new_H} {new_M}')


def q7567():
    # 그릇
    data = input()
    height = 10
    for i in range(len(data)-1):
        if data[i] == data[i+1]:
            height += 5
        elif data[i] != data[i+1]:
            height += 10
    print(height)


def q5063():
    # TGN
    test_case = int(input())
    rec = []
    for _ in range(test_case):
        rec_val = list(map(int, input().split()))
        rec.append(rec_val)
    for i in range(len(rec)):
        if rec[i][0] > rec[i][1] - rec[i][2]:
            print("do not advertise")
        elif rec[i][0] == rec[i][1] - rec[i][2]:
            print("does not matter")
        elif rec[i][0] < rec[i][1] - rec[i][2]:
            print("advertise")
        else:
            return


def q10102():
    # 개표
    judges = int(input())
    votes = input()
    result = 0
    for vote in votes:
        if vote == 'A':
            result += 1
    if result > len(votes) // 2:
        print('A')
    elif result == len(votes) / 2:
        print('Tie')
    else:
        print('B')


def q10886():
    # 0 = not cute / 1 = cute
    judges = int(input())
    votes = []
    for _ in range(judges):
        vote = int(input())
        votes.append(vote)
    if sum(votes) > len(votes) / 2:
        print('Junhee is cute!')
    else:
        print('Junhee is not cute!')


def q10988():
    # 팰린드롬인지 확인하기
    string = input()
    result = []
    for i in range(len(string)):
        if string[i] != string[-i-1]:
            result.append(0)
        else:
            result.append(1)
    print(min(result))


def q5086():
    # 배수와 약수
    values = []
    while 1:
        val = list(map(int, input().split()))
        if val[0] == 0 and val[0] == 0:
            break
        values.append(val)
    for i in range(len(values)):
        first = values[i][0]
        second = values[i][1]
        if first // second < 1 and second % first == 0:
            print('factor')
        elif first // second >= 1 and first % second == 0:
            print('multiple')
        else:
            print('neither')


def q5717():
    # 상근이의 친구들
    values = []
    while 1:
        val = list(map(int, input().split()))
        if val[0] == 0 and val[0] == 0:
            break
        values.append(val)
    for i in range(len(values)):
        print(values[i][0] + values[i][1])


def q9610():
    # 사분면
    test_case = int(input())
    spots = []
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    axis = 0
    for _ in range(test_case):
        spot = list(map(int, input().split()))
        spots.append(spot)
    for i in range(len(spots)):
        if spots[i][0] > 0 and spots[i][1] > 0:
            q1 += 1
        elif spots[i][0] < 0 and spots[i][1] > 0:
            q2 += 1
        elif spots[i][0] < 0 and spots[i][1] < 0:
            q3 += 1
        elif spots[i][0] > 0 and spots[i][1] < 0:
            q4 += 1
        else:
            axis += 1
    print(f'Q1: {q1}\n'
          f'Q2: {q2}\n'
          f'Q3: {q3}\n'
          f'Q4: {q4}\n'
          f'AXIS: {axis}\n')


def q8958():
    # OX퀴즈
    test_case = int(input())
    answers = []
    results = []
    for _ in range(test_case):
        answer = input()
        answers.append(answer)
    for answer in answers:
        point = 0
        sum_point = 0
        for j in range(len(answer)):
            if answer[j] == 'O':
                point += 1
                sum_point += point
            elif answer[j] == 'X':
                point = 0
            else:
                return
        results.append(sum_point)
    for i in range(len(results)):
        print((results[i]))


def q9506():
    # 약수들의 합
    values = []
    divisors = []
    while 1:
        val = int(input())
        if val == -1:
            break
        values.append(val)
    for i in range(len(values)):
        index = 2
        divisor = []
        while index != values[i]:
            if values[i] % index == 0:
                divisor.append(index)
            index += 1
        divisors.append(divisor)
        string = f'{values[i]} = 1'
        if values[i] == sum(divisors[i], 1):
            for j in range(len(divisors[i])):
                string += f' + {divisors[i][j]}'
            print(string)
        else:
            print(f'{values[i]} is NOT perfect.')


def q10162():
    # 전자레인지
    t = int(input())
    if t % 10 == 0:
        btn3 = t // 10
        btn2 = btn3 // 6
        btn1 = btn2 // 5
        if btn2 > 0:
            btn3 %= 6
            if btn1 > 0:
                btn2 %= 5
        print(f'{btn1} {btn2} {btn3}')
    else:
        print(-1)


def q10103():
    # 주사위 게임
    rounds = int(input())
    chances = []
    c_point = 100
    s_point = 100
    for _ in range(rounds):
        chance = list(map(int, input().split()))
        chances.append(chance)
    for i in range(len(chances)):
        if chances[i][0] > chances[i][1]:
            s_point -= chances[i][0]
        elif chances[i][0] == chances[i][1]:
            pass
        else:
            c_point -= chances[i][1]
    print(c_point)
    print(s_point)


def q10214():
    # Baseball
    matches = int(input())
    for _ in range(matches):
        y_point = 0
        k_point = 0
        for _ in range(9):
            y, k = map(int, input().split())
            y_point += y
            k_point += k
        if y_point > k_point:
            print('Yonsei')
        elif y_point < k_point:
            print('Korea')
        else:
            print('Draw')


def q11557():
    # Yangjojang of The Year
    test_case = int(input())
    case_datas = []
    for i in range(test_case):
        univ_nums = int(input())
        datas = []
        for _ in range(univ_nums):
            data = list(input().split())
            data[1] = int(data[1])
            datas.append(data)
        max_value = 0
        for j in range(len(datas)):
            if max_value < datas[j][1]:
                max_value = datas[j][1]
        for k in range(len(datas)):
            if datas[k][1] == max_value:
                case_datas.append(datas[k])
    for i in range(len(case_datas)):
        print(case_datas[i][0])


def q10757():
    # 큰 수 A+B
    a, b = input().split()
    print(int(a) + int(b))

