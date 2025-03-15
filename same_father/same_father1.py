import sys
import copy
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1,T+1):

    conditions = list(map(int, input().split()))
    # V는 정점 갯수, E는 간선 갯수 , search는 찾는 숫자들
    V, E, search1, search2 = conditions
    # real_e 간선이 어떻게 생겼나 상세하게 알려주는 변수
    real_E = list(map(int, input().split()))

    # 루트 번호가 1번인 것이 중요한 포인트 같다.
    # make_stack = [search1]
    # temp1 = []
    # temp_e =0
    # while make_stack:
    #     a = make_stack.pop()
    #     temp_e += 1
    #     if a == 1:
    #         break
    #     if a in real_E:
    #         temp_idx = real_E.index(a)
    #         make_stack.append(real_E[temp_idx-1])
    #         temp1.append(real_E[temp_idx-1])

    # print(set(temp1))
    # print(f'#{tc} {start_sub_tree} {sub_tree_size}')

    child_to_parent = {}
    for i in range(0, len(real_E), 2):
        parent, child = real_E[i], real_E[i + 1]
        child_to_parent[child] = parent  # 자식이 key, 부모가 value

    # 특정 노드(search1)에서 부모를 따라 루트(1)까지 추적
    make_stack = [search1]
    # 첫 번째 숫자 부모 넣을 리스트
    temp1 = []

    while make_stack:
        node = make_stack.pop()
        if node == 1:  # 루트 도달 시 종료
            break
        if node in child_to_parent:  # 부모가 존재하면 스택에 추가
            parent = child_to_parent[node]
            make_stack.append(parent)
            temp1.append(parent)

    # 두 번째 숫자 부모 넣을 리스트
    make_stack1 = [search2]
    temp2 = []

    while make_stack1:
        node = make_stack1.pop()
        if node == 1:  # 루트 도달 시 종료
            break
        if node in child_to_parent:  # 부모가 존재하면 스택에 추가
            parent = child_to_parent[node]
            make_stack1.append(parent)
            temp2.append(parent)

    # 공통 조상 찾기
    result_list =[]
    for tem in temp1:
        if tem in temp2:
            result_list.append(tem)
    # 가장 큰 공통 조상
    # print(result_list)
    start_sub_tree = max(result_list)

    stack = [start_sub_tree]
    sub_tree_size = 1
    while stack:
        a = stack.pop()
        for i in range(0, len(real_E), 2):
            if a == real_E[i]:
                stack.append(real_E[i+1])
                sub_tree_size += 1
    # print(sub_tree_size)
    print(f'#{tc} {start_sub_tree} {sub_tree_size}')