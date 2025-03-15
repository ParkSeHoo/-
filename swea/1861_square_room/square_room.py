import sys
sys.stdin = open("input.txt")

T = int(input())

# 가로가 row x로 해야 하나?
# 그럼 list를 만들었을때 list[y][x]가 됨 
# 강사님 코드 한번 봐야겠다. 
x_directions = [0, 0, 1, -1]
y_directions = [1, -1, 0, 0]
def search_rooms(rooms, current_x, current_y, count, visited):
    # 여기에 넣으면 매번 반복 될때마다 바뀌는데?
    # 한번 만 넣어야 하는데?
    # 흠 일단 알겠습니다.
    start = rooms[current_x][current_y]

    print(current_x, current_y)
    #종료 조건이 뭘까요?
    for k in range(4):
        next_x = current_x + x_directions[k]
        next_y = current_y + y_directions[k]
        if (0 <= next_x < N and 0 <= next_y < N ) and (rooms[next_x][next_y] ==start-1 or rooms[next_x][next_y] ==start+1) and visited[next_x][next_y] == 0:
            print(rooms[next_x][next_y])
            # print(next_x, next_y)
            print("count", count)
            visited[next_x][next_y] = 1
            search_rooms( rooms, next_x, next_y, count+1, visited )
            visited[next_x][next_y] = 0
        # 백트래킹 조건이 있어야 합니다... 왜냐면 두 갈래 길이 있거등요 
        # 그러면 리턴을 해줘서 계속 리턴리턴리턴리턴 이렇게 할거냐?
        # 그냥 배열 만들어서 특정 지점으로 돌아가게는 못하냐?
        # ex) visited 배열 근데 그건 조건을 달아야하는데 
        # 재귀로 하는데 어떻게 달거냐?
        # 궁금증 : 재귀로 함수가 들어가다보면 리턴이 되는데 그럼 재귀스택이 다 빠지나요?
        # 빠지면서 계속 리턴되나요?
    # 여기서 리턴하면 되나?


for tc in range(1,T+1):
    
    N = int(input())
    # N*N 숫자 배열 생성
    N_room =[]
    for _ in range(N):
        N_room.append(list(map(int,input().split())))
    
    # 이동하려는 방이 현재 방에 적힌 숫자보다 정확히 1이 커야한다. 
    # 처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 것
    # 최대 횟수가 같다면 가장 작은 수 출력
    # 완전 탐색... 해야겠지...?
    # bfs 되나 ? 응 안됨 돌아가 
    # DFS로 풀어야 할 듯? ㅠㅠㅠㅠㅠㅠㅠ


    # 시작하는 숫자
    start = 0
    # 이동횟수를 담을 리스트
    counts = []

    start_list=[]
    
    for i in range(N):
        for j in range(N):
            visited = [[0] * N for _ in range(N)]
            start_list.append([i,j])
            sample_count = 1
            # counts.append(search_rooms(N_room, i, j, sample_count))

            search_rooms(N_room, i, j, sample_count, visited)

    # print(f'#{start} {min(counts)}')