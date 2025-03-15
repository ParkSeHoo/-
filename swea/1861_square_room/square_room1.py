import sys
sys.stdin = open("input.txt")

T = int(input())

# 가로가 row x로 해야 하나?
# 그럼 list를 만들었을때 list[y][x]가 됨 
# 강사님 코드 한번 봐야겠다. 
x_directions = [0, 0, 1, -1]
y_directions = [1, -1, 0, 0]
def search_rooms(rooms, current_x, current_y, count, visited):
    start = rooms[current_x][current_y]
    print("현재 위치:", current_x, current_y, "값:", start, "count:", count)
    visited[current_x][current_y] = 1  # 방문 체크
    for k in range(4):
        next_x = current_x + x_directions[k]
        next_y = current_y + y_directions[k]

        if (0 <= next_x < N and 0 <= next_y < N) and \
           (rooms[next_x][next_y] == start - 1 or rooms[next_x][next_y] == start + 1) and \
           visited[next_x][next_y] == 0:  # 방문하지 않은 경우만 이동

            print("이동 ->", next_x, next_y, "값:", rooms[next_x][next_y])
            print("count 증가:", count + 1)
            search_rooms(rooms, next_x, next_y, count + 1, visited)  # 재귀 호출

for tc in range(1,T+1):
    
    N = int(input())
    # N*N 숫자 배열 생성
    N_room =[]
    for _ in range(N):
        N_room.append(list(map(int,input().split())))
    
    # 시작하는 숫자
    start = 0
    # 이동횟수를 담을 리스트
    counts = []

    start_list=[]
    visited = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            start_list.append([i,j])
            sample_count = 1
            # counts.append(search_rooms(N_room, i, j, sample_count))
            search_rooms(N_room, i, j, sample_count, visited)

    # print(f'#{start} {min(counts)}')