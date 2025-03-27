T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    # 1일 경우 처리
    if A == 1:
        print(B)
        continue
    if B == 1:
        print(A)
        continue
    temp_A = A
    temp_B = B
    A_Divisors = []
    B_Divisors = []
    start = 2
    while temp_A != 1:
        if temp_A % start == 0:
            A_Divisors.append(start)
            temp_A=temp_A//start
        else:
            start += 1
    start = 2
    while temp_B != 1:
        if temp_B % start == 0:
            B_Divisors.append(start)
            temp_B = temp_B//start
        else:
            start += 1

    A1 = set(A_Divisors)
    B1 = set(B_Divisors)
    A1.update(B1)
    last = sorted(A1)
    min_mul = 1
    if len(last) == 1:
        min_mul = max(A, B)
    else:
        for la in last:
            min_mul *= la
    print(min_mul)
