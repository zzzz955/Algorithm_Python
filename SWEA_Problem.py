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
q2063()
