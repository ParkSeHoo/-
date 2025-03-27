import sys
sys.stdin = open("input.txt")


T = 4

# 정사각형 1개
# 직사각형 2개
# ㅗ 4개
# z 4개
# L 4개 *2

# 종료 조건 길이가 4면 끝임 4가 되는 어느 모양이든 커버가능
# 500 * 500 -> 250,000 * 19 -> 약 500만번?
for tc in range(1,T+1):
    N, M = map(int, input().split())
    map_list = [list(map(int,input().split())) for _ in range(N)]
    
    tetrominos = [
    # 직사각형
    [(0,0),(0,1),(0,2),(0,3)], 
    [(0,0),(1,0),(2,0),(3,0)],
    # 정사각형
    [(0,0),(0,1),(1,0),(1,1)],
    # L 8개
    [(0,0),(1,0),(2,0),(2,1)],
    [(0,0),(0,1),(0,2),(1,0)],
    [(0,0),(0,1),(1,1),(2,1)],
    [(0,0),(1,0),(1,1),(1,2)],
    [(0,0),(1,0),(2,0),(0,1)],
    [(0,0),(0,1),(1,0),(2,0)],
    [(0,0),(0,1),(0,2),(1,2)],
    [(0,0),(1,0),(1,-1),(1,-2)],
    # z 4개
    [(0,0),(0,1),(1,1),(1,2)],
    [(0,1),(1,0),(1,1),(2,0)],
    [(0,1),(0,2),(1,0),(1,1)],
    [(0,0),(1,0),(1,1),(2,1)],
    # ㅗ 4개
    [(0,0),(0,1),(0,2),(1,1)],
    [(0,0),(1,-1),(1,0),(1,1)],
    [(0,0),(1,0),(2,0),(1,1)], 
    [(0,0),(1,0),(2,0),(1,-1)] 
    ]
    #최대값
    max_sum = 0

    for i in range(N):
        for j in range(M):
            for tetromino in tetrominos:
                try:
                    temp_total = 0
                    for dx, dy in tetromino:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < N and 0 <= nj < M:
                            temp_total += map_list[ni][nj]
                        else:
                            raise IndexError
                    max_sum = max(max_sum, temp_total)
                except IndexError:
                    continue

    print(max_sum)