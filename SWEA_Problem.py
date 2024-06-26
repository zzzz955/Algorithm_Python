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
q1959()