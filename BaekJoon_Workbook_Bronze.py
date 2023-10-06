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
q14563()