import sys
from collections import deque
sys.stdin = open("sample_input.txt")

T = int(input())

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def search(current_x, current_y):
    visited = [[False] * N for _ in range(N)]
    queue = deque([(current_x, current_y)])
    visited[current_x][current_y] = True

    protected_house = 0
    count = 1
    protect_cost = count * count + (count - 1) * (count - 1)
    consumer_cost = 0
    max_valid_houses = 0  # 손해를 보지 않는 최대 집 수 저장

    if home_map[current_x][current_y] == 1:
        protected_house += 1
        consumer_cost += M

    while queue:
        for _ in range(len(queue)):  # 현재 depth에서 확장
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

                    if home_map[nx][ny] == 1:
                        protected_house += 1
                        consumer_cost += M

        count += 1
        protect_cost = count * count + (count - 1) * (count - 1)

        # 손해를 보지 않는 최대값 저장
        if consumer_cost - protect_cost > 0:
            max_valid_houses = max(max_valid_houses, protected_house)

    return max_valid_houses

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    home_map = [list(map(int, input().split())) for _ in range(N)]

    max_protected_houses = 0

    for i in range(N):
        for j in range(N):
            max_protected_houses = max(max_protected_houses, search(i, j))

    print(f'#{tc} {max_protected_houses}')
