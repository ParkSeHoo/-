import sys
from collections import deque

T = int(input().strip())

# 방향 벡터 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 운영비용 리스트 미리 계산 (최대 25까지)
KLst = [k*k + (k-1)*(k-1) for k in range(26)]

def search(sr, sc):
    global maxCnt
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1
    Q = deque([(sr, sc)])

    home = home_map[sr][sc]  # 현재 위치의 집 개수
    dis = 1  # 거리 초기값

    # 초기 K=1일 때도 검사
    if home * M - KLst[dis] >= 0:
        maxCnt = max(home, maxCnt)

    while dis < N + 2:
        qlen = len(Q)
        for _ in range(qlen):
            r, c = Q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if not visited[nr][nc]:
                    visited[nr][nc] = 1
                    Q.append((nr, nc))
                    if home_map[nr][nc]:  # 집이 있는 경우
                        home += 1

        # 보안회사의 이익이 0 이상이면 최댓값 갱신
        if home * M - KLst[dis + 1] >= 0:
            maxCnt = max(home, maxCnt)

        dis += 1  # 거리 증가

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    home_map = [list(map(int, input().split())) for _ in range(N)]

    maxCnt = 0  # 최대 보호 가능한 집 개수

    for i in range(N):
        for j in range(N):
            search(i, j)  # 모든 위치에서 검사

    print(f"#{tc} {maxCnt}")
