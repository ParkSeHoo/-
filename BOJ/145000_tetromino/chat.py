N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

tetromino_shapes = [
    [(0,0),(0,1),(0,2),(0,3)],
    [(0,0),(1,0),(2,0),(3,0)],
    [(0,0),(0,1),(1,0),(1,1)],
    [(0,0),(1,0),(2,0),(2,1)],
    [(0,0),(0,1),(1,0),(2,0)],
    [(0,0),(0,1),(0,2),(1,0)],
    [(0,0),(0,1),(0,2),(1,2)],
    [(0,0),(1,0),(1,1),(1,2)],
    [(0,0),(1,0),(2,0),(0,1)],
    [(0,0),(0,1),(1,1),(2,1)],
    [(0,0),(1,0),(2,0),(2,-1)],
    [(0,0),(0,1),(1,0),(1,-1)],
    [(0,0),(1,0),(1,1),(2,1)],
    [(0,0),(0,1),(1,1),(1,2)],
    [(0,0),(0,1),(0,2),(1,1)],
    [(0,0),(1,-1),(1,0),(1,1)],
    [(0,0),(1,0),(2,0),(1,1)],
    [(0,0),(1,0),(2,0),(1,-1)],
]

max_sum = 0

for i in range(N):
    for j in range(M):
        for shape in tetromino_shapes:
            try:
                total = 0
                for dx, dy in shape:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < N and 0 <= nj < M:
                        total += board[ni][nj]
                    else:
                        raise IndexError
                max_sum = max(max_sum, total)
            except IndexError:
                continue

print(max_sum)
