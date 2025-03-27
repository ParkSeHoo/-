import sys
sys.stdin = open("input.txt")

# 주변 4칸 확인용
next_direction =[(1, 0),(-1, 0),(0, -1),(0, 1)]
# 방향에 맞게 가는 경로
d_dict ={0:(-1,0), 1:(0, 1), 2:(1,0), 3:(0,-1)}  
# 북 서 남 동
d_list = [0,3,2,1]
def cleaning(r, c, d):
    global total_clean
    # 청소가 되지 않은 경우 현재 칸을 청소
    if visited[r][c]:
        visited[r][c] = False
        total_clean+=1

    Flag = False
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈칸이 있는 경우 
    for nr,nc in next_direction:
        if 0 <= nr+r < N and 0 <= nc+c < M and visited[r+nr][c+nc]:
            Flag = True
            break
    
    # 청소 할 공간이 있으면 첫번째 조건,
    if Flag:
        idx = d_list.index(d)
        for i in range(4):
            # 90도 돌리기
            idx += 1
            if idx > 3:
                idx = 0
            nd = d_list[idx]  # 회전한 방향
            tr, tc = d_dict[nd]  # 이동할 방향 델타
            nr, nc = r + tr, c + tc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and start_map[nr][nc] == 0:
                cleaning(nr, nc, nd)
                return
    # 청소가 불가능 하면 else
    else:
        tr,tc = d_dict[d]
        nr, nc = r - tr, c - tc
        # 후진 가능할 때
        if 0 <= nr < N and 0 <= nc < M and start_map[nr][nc] == 0:
            cleaning(nr, nc, d)
            

N,M = map(int,input().split())
r,c,d = map(int,(input().split()))

start_map =[]
for _ in range(N):
    start_map.append(list(map(int,input().split())))

# 0 이면 청소가 안된 것이고 1이면 벽이다. 
visited = [ [True]*M for _ in range(N) ]
total_clean=0
cleaning(r,c,d)
print(total_clean)