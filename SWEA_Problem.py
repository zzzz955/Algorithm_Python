def q1936():
    # SWEA 1936번 D1 1대1 가위바위보 파이썬
    a, b = map(int, input().split())
    if a > b or (a == 1 and b == 3):
        print('A')
    else:
        print('B')


def q2058():
    # SWEA 2058번 D1 자릿수 더하기 파이썬
    n = input()
    result = 0
    for i in n:
        result += int(i)
    print(result)


def q2063():
    # SWEA 2063번 D1 중간값 찾기 파이썬
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    print(lst[n // 2])


def q1959():
    # SWEA 1959번 D2 두 개의 숫자열 파이썬
    t = int(input())
    for i in range(1, t + 1):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        result = -2 ** 31
        for j in range(abs(n - m) + 1):
            temp = 0
            if n - m <= 0:
                for k in range(n):
                    temp += a[k] * b[j + k]
            else:
                for k in range(m):
                    temp += a[j + k] * b[k]
            result = max(result, temp)
        print(f"#{i} {result}")


def q1961():
    # SWEA 1961번 D2 숫자 배열 회전 파이썬
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        array = ''
        for _ in range(n):
            lst = list(map(str, input().split()))
            for temp in lst:
                for char in temp:
                    array += char
        angle90 = []
        angle180 = []
        angle270 = []
        for j in range(n):
            for k in range(n - 1, -1, -1):
                angle90.append(array[j + k * n])
        for j in range(len(array) - 1, -1, -1):
            angle180.append(array[j])
        for j in range(n - 1, -1, -1):
            for k in range(n):
                angle270.append(array[j + k * n])
        print(f'#{i}')
        for j in range(n):
            print(''.join(angle90[j * n:j * n + n]), ''.join(angle180[j * n:j * n + n]), ''.join(angle270[j * n:j * n + n]))


def q12712():
    # SWEA 12712번 D2 파리퇴치3 파이썬
    t = int(input())
    for i in range(1, t + 1):
        n, m = map(int, input().split())
        lst = [list(map(int, input().split())) for _ in range(n)]
        result = 0
        for j in range(n):
            for k in range(n):
                temp1 = 0
                temp2 = 0
                for l in range(-m + 1, m):
                    if 0 <= j + l < n:
                        temp1 += lst[j + l][k]
                    if 0 <= k + l < n:
                        temp1 += lst[j][k + l]
                    if 0 <= j + l < n and 0 <= k + l < n:
                        temp2 += lst[j + l][k + l]
                    if 0 <= j - l < n and 0 <= k + l < n:
                        temp2 += lst[j - l][k + l]
                temp1 -= lst[j][k]
                temp2 -= lst[j][k]
                result = max(result, temp1, temp2)
        print(f'#{i} {result}')


def q1486():
    # SWEA 1486번 D4 장훈이의 높은 선반 파이썬
    t = int(input())
    for i in range(1, t + 1):
        n, b = map(int, input().split())
        lst = list(map(int, input().split()))
        result = 200001
        for j in range(2 ** n):
            temp = 0
            for k in range(n):
                if j & (2 ** k):
                    temp += lst[k]
            if temp >= b:
                result = min(result, temp)
        print(f'#{i} {result - b}')
q1486()

