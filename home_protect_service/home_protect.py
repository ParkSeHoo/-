import sys
from collections import deque
sys.stdin = open("sample_input.txt")

T = int(input())

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def search(current_x, current_y, protected_house):
    visited = [[False] * N for _ in range(N)]
    protected_house += 1
    count = 1
    protect_cost = count*count + (count-1)*(count-1)
    consumer_cost = M
    benefit = consumer_cost - protect_cost
    queue = deque([(current_x, current_y)])

    while queue:
        if benefit < 0:
            break
        queue.popleft()
        visited[current_x][current_y] = True
        for x, y in directions:
            nx = current_x + x
            ny = current_y + y
            if not visited[nx][ny] and 0 <= nx < N and 0 <= ny < N:
                visited[nx][ny] = True
                queue.append((nx, ny))
                consumer_cost += M
            count += 1
            protect_cost = count*count+(count-1)*(count-1)
            benefit = consumer_cost-protect_cost
        protected_house += 1

    return protected_house



for tc in range(1, T+1):
    # 운영 비용 = K * K + (K - 1) * (K - 1)
    # N은 도시의 크기 M은 한 집의 지불하는 비용
    # 답은 손해보지 않으면서 가장 많은 집들에 제공하는 서비스 영역을 찾아야 함
    N, M = map(int, input().split())
    home_map = []
    # visited = [0]*N for _ in range(N)
    protected_house1 = 0
    for _ in range(N):
        home_map.append(list(map(int, input().split())))
    for i in range(N):
        for j in range(N):
            if home_map[i][j] == 1:
                protected_house1 = search(i, j, protected_house1)

    print(f'#{tc} {protected_house1}')