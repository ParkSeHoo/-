import sys
sys.stdin = open("input.txt")

T = int(input())

x_directions = [0, 0, 1, -1]
y_directions = [1, -1, 0, 0]

def search_rooms(rooms, current_x, current_y, count, visited):
    start = rooms[current_x][current_y]
    max_count = count  # 최대 방문 횟수 저장

    for k in range(4):
        next_x = current_x + x_directions[k]
        next_y = current_y + y_directions[k]

        if (0 <= next_x < N and 0 <= next_y < N) and \
           (rooms[next_x][next_y] == start - 1 or rooms[next_x][next_y] == start + 1) and \
           visited[next_x][next_y] == 0:  # 방문하지 않은 곳

            visited[next_x][next_y] = 1  # 방문 체크
            max_count = max(max_count, search_rooms(rooms, next_x, next_y, count + 1, visited))  # 최댓값 갱신
            visited[next_x][next_y] = 0  # 백트래킹 (복구)

    return max_count  # 최댓값 반환

# 예제 실행
for tc in range(1, T + 1):
    N = int(input())

    # N*N 숫자 배열 생성
    rooms = [list(map(int, input().split())) for _ in range(N)]

    result = 0  # 최댓값 저장

    for i in range(N):
        for j in range(N):
            visited = [[0] * N for _ in range(N)]  # 방문 체크 배열 초기화
            visited[i][j] = 1  # 시작점 방문 체크
            result = max(result, search_rooms(rooms, i, j, 1, visited))  # 최댓값 갱신

    print(f"#{tc} 최대 방문 횟수: {result}")
