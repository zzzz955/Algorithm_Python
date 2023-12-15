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
q2231()