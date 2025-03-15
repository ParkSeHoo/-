# 컨셉
# 깎는것을 생각하기 어렵다
# 그래서 미리 깎고 가야한다.
# 1. 모든 정상 찾기
# 임의로 N*N에 대해 모든 경우에 K번 산을 깎아야 한다.
# 완전 탐색 접근법

import sys
from collections import deque
sys.stdin = open("sample_input.txt")

T = int(input())

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def find_peaks(arr,N):
    max_val = max(map(max, arr))
    peaks= []
    for r in range(N):
        for c in range(N):
            if arr[r][c]==max_val:
                peaks.append((r,c))
    return peaks

def bfs(pr, pc,N):
    # 방문처리 배열
    visited = [[False]*N for _ in range(N)]
    # 이 문제는 작은 쪽으로만 간다.

    queue = deque()
    visited[pr][pc] = True
    queue.append((pr, pc,1))

    length=0
    while queue:
        r,c = queue.popleft()
        length= max(length, cnt)
        for d in range(4):
            nr, nc = r+ dr[d], c+dc[d]
            if 0<=nr<N and 0 <= nc <N:
                if arr[nr][nc] < arr[r][c] and not visited[nr][nc]:
                    queue.append((nr, nc, cnt+1))
    return length
for tc in range(1,T+1):
    N, K = list(map(int,input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가장 높은 봉우리 찾기
    peaks = find_peaks(arr, N)

    # 3중 for문 사용 N*N*K
    # 완전 탐색
    for k in range(K+1):
        for r in range(N):
            for c in range(N):
                # 음수 일 경우
                # if arr[r][c]-k < 0:
                #     continue

                arr[r][c] -= k
                for pr, pc in peaks:
                    length = bfs(pr,pc,N)
                    max
                arr[r][c]+=k #복원