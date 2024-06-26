def q1936():
    # SWEA 1936번 D1 1대1 가위바위보 파이썬
    a, b = map(int, input().split())
    if a > b or (a == 1 and b == 3):
        print('A')
    else:
        print('B')
q1936()