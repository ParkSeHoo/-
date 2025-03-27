import sys
sys.stdin = open("input1.txt")

T = int(input())

def dfs_width(i, j, count):
    global max_length
    if i >= N or j >= M or ruins[i][j] == 0 or visited_width[i][j]:
        max_length = max(max_length, count)
        return
    
    visited_width[i][j] = True
    dfs_width(i, j + 1, count + 1)

def dfs_length(i, j, count):
    global max_length
    if i >= N or j >= M or ruins[i][j] == 0 or visited_length[i][j]:
        max_length = max(max_length, count)
        return
    
    visited_length[i][j] = True
    dfs_length(i + 1, j, count + 1)

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    
    ruins = [list(map(int, input().split())) for _ in range(N)]
    visited_width = [[False] * M for _ in range(N)]   # 가로 탐색 전용 visited
    visited_length = [[False] * M for _ in range(N)]  # 세로 탐색 전용 visited
    
    max_length = 0

    for i in range(N):
        for j in range(M):
            if ruins[i][j] == 1:
                if not visited_width[i][j]:
                    dfs_width(i, j, 0)
                if not visited_length[i][j]:
                    dfs_length(i, j, 0)
    
    print(f'#{tc} {max_length}')
