from collections import deque
import sys


def bfs(grid, start, target=None):
    """
    BFS를 이용해 최단 거리를 찾는 함수
    start에서 target까지의 거리를 반환하거나, 모든 승객까지의 거리를 찾는다.
    """
    n = len(grid)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start[0], start[1], 0)])  # (row, col, distance)
    visited = set()
    visited.add((start[0], start[1]))

    while queue:
        r, c, dist = queue.popleft()
        if target and (r, c) == target:
            return dist  # 목적지에 도착하면 거리 반환

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

    return -1  # 도달 불가능할 경우


def find_nearest_passenger(grid, taxi, passengers):
    """ 가장 가까운 승객을 찾는 함수 """
    n = len(grid)
    queue = deque([(taxi[0], taxi[1], 0)])  # (row, col, distance)
    visited = set()
    visited.add((taxi[0], taxi[1]))

    candidates = []
    while queue:
        r, c, dist = queue.popleft()
        if (r, c) in passengers:
            candidates.append((dist, r, c))

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

    if not candidates:
        return None, -1  # 승객을 찾을 수 없는 경우

    candidates.sort()  # (거리, 행, 열) 기준으로 정렬
    return (candidates[0][1], candidates[0][2]), candidates[0][0]


def taxi_simulation(n, m, fuel, grid, taxi, passengers):
    """ 택시 시뮬레이션을 실행하는 메인 함수 """
    for _ in range(m):
        # 1. 가장 가까운 승객 찾기
        nearest, distance = find_nearest_passenger(grid, taxi, passengers)
        if nearest is None or fuel < distance:
            return -1  # 이동할 연료가 없거나 승객을 찾을 수 없는 경우

        # 2. 승객을 태우러 이동
        fuel -= distance
        passenger_dest = passengers.pop(nearest)
        taxi = nearest

        # 3. 목적지로 이동
        distance_to_dest = bfs(grid, taxi, passenger_dest)
        if distance_to_dest == -1 or fuel < distance_to_dest:
            return -1  # 목적지까지 갈 수 없는 경우

        # 4. 목적지 도착 및 연료 충전
        fuel += distance_to_dest  # 이동한 연료의 두 배 충전
        taxi = passenger_dest  # 택시 위치 업데이트

    return fuel  # 모든 승객을 태우고 남은 연료 반환


# 입력 처리
input = sys.stdin.read

data = input().split("\n")
n, m, fuel = map(int, data[0].split())
grid = [list(map(int, data[i + 1].split())) for i in range(n)]
taxi = tuple(map(lambda x: int(x) - 1, data[n + 1].split()))  # 0-index 변환
passengers = {}
for i in range(m):
    sr, sc, dr, dc = map(lambda x: int(x) - 1, data[n + 2 + i].split())
    passengers[(sr, sc)] = (dr, dc)

# 실행 및 출력
print(taxi_simulation(n, m, fuel, grid, taxi, passengers))
