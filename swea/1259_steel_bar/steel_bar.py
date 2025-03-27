import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    temp = list(map(int, input().split()))
    paired_list = [list(pair) for pair in zip(temp[::2], temp[1::2])]

    # print(paired_list)
    flag = True
    final_list =[]

    start_list = []
    
    # 시작점 찾기
    for i in range(len(paired_list)):
        temp_start = paired_list[i][0]
        for j in range(len(paired_list)):
            if temp_start ==paired_list[j][1]:
                temp_start = 0
                break
        if temp_start!=0:
            final_list.append(paired_list[i])
            start_list.append((paired_list.pop(i)))
            break
    
    # print(start_list)
    # print(paired_list)
    
    # 돌리기
    while flag:
        start, end = start_list.pop()
        # for i in range(len(paired_list)):
        #     if end == paired_list[i][0]:
        #         final_list.append(paired_list[i])
        #         start_list.append(paired_list.pop(i))
        #         continue
        for pair_start, pair_end in paired_list:
            if end == pair_start:
                final_list.append([pair_start,pair_end])
                start_list.append([pair_start,pair_end])
                break
        # print(start_list)
        if not start_list:
            # print("왜없음?")
            flag = False
        # if start_list[0][1] not in paired_list:
        #     print("왜없음?")
        #     flag = False
    flattened = ' '.join(map(str, sum(final_list, [])))

    print(f'#{tc} {flattened}')