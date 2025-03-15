import sys
import copy
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1,T+1):

    conditions = list(map(int, input().split()))
    # V는 정점 갯수, E는 간선 갯수 , search는 찾는 숫자들
    V, E, search1, search2 = conditions
    # real_e 간선이 어떻게 생겼나 상세하게 알려주는 변수
    real_E = list(map(int,input().split()))
    reversed_E = copy.deepcopy(real_E)
    # for i in range(len(real_E)-1,-1,-1):
    #     reversed_E.append(real_E[i])
    # print(reversed_E)
    reversed_E.reverse()
    # print(reversed_E)
    # print(real_E)
    # 공통 조상을 찾기 시작
    same_father = 0
    # search1, search2 해당 숫자부터 root까지 모두 임시리스트에 담는다.

    # search1의 조상 모음
    temp1 = []
    # search2의 조상 모음
    temp2 = []

    # 조상 모으는 반복문
    for i in range(0, len(real_E), 2):
        # print(reversed_E[i], search1)
        if reversed_E[i] == search1:
            temp1.append(reversed_E[i+1])
            search1 = reversed_E[i+1]
            # print(search1)
        if reversed_E[i] == search2:
            temp2.append(reversed_E[i+1])
            search2 = reversed_E[i+1]
    # print(temp1, temp2)

    # 공통 조상 찾기
    result_list =[]
    for tem in temp1:
        if tem in temp2:
            result_list.append(tem)
    # 가장 큰 공통 조상
    # print(result_list)
    start_sub_tree = max(result_list)
    # print(start_sub_tree)

    # stack으로 찾아야 하지 않을까?
    # print(real_E)
    stack = [start_sub_tree]
    sub_tree_size = 1
    while stack:
        a = stack.pop()
        for i in range(0, len(real_E), 2):
            if a == real_E[i]:
                stack.append(real_E[i+1])
                sub_tree_size += 1
    # print(sub_tree_size)


    # 루트 번호가 1번인것이 중요한 포인트 같다.
    # 시작부터 새롭게 계속돌면서 정렬을 하면 에반가? 에반게리온임..
    make_stack = [search1]
    while make_stack:
        a = make_stack.pop()
        if a in real_E:
            temp_idx = real_E.index(a)
            make_stack.append(real_E[temp_idx-1])
    print(make_stack)

    # print(f'#{tc} {start_sub_tree} {sub_tree_size}')