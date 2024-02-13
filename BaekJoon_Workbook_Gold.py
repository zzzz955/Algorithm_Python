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
q10986()