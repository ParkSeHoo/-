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
    A_dict={}
    B_dict={}
    start = 2
    temp_set=set()
    while temp_A != 1:
        if temp_A % start == 0:
            temp_set.add(start)
            if start in A_dict:
                A_dict[start] += 1
            else:
                A_dict[start] = 1
            temp_A = temp_A//start
        else:
            start += 1
    start = 2
    while temp_B != 1:
        if temp_B % start == 0:
            temp_set.add(start)
            if start in B_dict:
                B_dict[start] += 1
            else:
                B_dict[start] = 1
            temp_B = temp_B//start
        else:
            start += 1
    # print(A_dict)
    all_num = sorted(temp_set)
    min_mul = 1
    for i in range(len(all_num)):
        root = all_num[i]
        order = max(A_dict.get(all_num[i], 0), B_dict.get(all_num[i], 0))
        min_mul *= root**order

    print(min_mul)
