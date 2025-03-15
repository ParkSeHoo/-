import sys
sys.stdin = open('input.txt')

def check_parent(x, total_time):
    global count
    global r_total

    count += 1
    temp_time = total_time
    temp_time += how_long[x-1]

    if parent[x][0] == x:
        r_total = max(r_total, temp_time)
        return
    else:
        for i in range(len(parent[x])):
            # temp_total += how_long[parent[x][i]]
            check_parent(parent[x][i], temp_time)

# 첫줄에 TC

T = int(input())

for tc in range(1, T+1):

    # N = 건설 할 수 있는 갯수 , K = 규칙 갯수
    N, K = map(int, input().split())

    # 순서에 맞는 소요시간
    # ex) 10 1 100 10
    # 1  2  3   4
    # 10 1 100  10
    how_long = list(map(int, input().split()))

    # 규칙 설명 x 가 완성 되어야 y를 지을 수 있다.
    order = []

    time_list = [0] * (N + 1)
    for i in range(1,len(time_list)):
        time_list[i] = how_long[i-1]
    # print(time_list)
    for _ in range(K):
        temp = tuple(map(int, input().split()))
        # print(temp)
        order.append(temp)

    # 지어야 끝나는 건물의 번호
    end_condition = int(input())

    # 부모를 기록할 빈 이중 리스트
    # parent = [[]]*N
    parent = [[i] for i in range(N+1)]

    # print(parent)
    for x, y in order:
        # print(x,y)
        if y in parent[y]:
            parent[y].pop()
        parent[y].append(x)

    # 부모 정리가 끝난 리스트
    # print(parent)
    # for k in range(len(time_list)):
    #     time_list[i] = how_long[]


    # 건물 짓는데 걸린 총 시간
    r_total = 0
    count = 0
    check_parent(end_condition, 0)
    print(r_total)
    # print(how_long[end_condition-1])
    # print(count)