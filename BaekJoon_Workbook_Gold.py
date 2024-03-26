def q12348():
    # 분해합2
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
    # 나머지 합
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
    # 문자열 변환과 쿼리
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
q27396()