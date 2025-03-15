import sys
from collections import deque
sys.stdin = open("sample_input.txt")

T = int(input())

def MT_len(starti, startj):
    # 동 서 남 북
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    queue = deque([starti,startj])

    while queue:
        current_x, current_y = queue.pop()
        for x ,y in directions:
            # 다음 좌표
            nx =current_x+directions[x]
            ny = current_y+directions[y]
            if N-1 >= nx > 0 and N-1 >= ny > 0:
                queue.append([nx,ny])


T = 1

for tc in range(1,T+1):
    N, K = map(int,input().split())
    MT = []
    for _ in range(N):
        MT.append(list(map(int, input().split())))

    MT_start = max(MT)
    for i in range(N):
        for j in range(N):
            if MT[i][j] == MT_start:
                MT_len(i,j)