from collections import deque
import sys
from pprint import pprint
sys.stdin =open('jar.txt')
# N * N 행렬 만들 N을 입력 받는다. 
N = int(input())

# 상하좌우 가는 것
direction =[ (1, 0), (-1, 0), (0,1), (0,-1)]
# 시작 지점 부터 끝까지 순회하는 것
def bfs(jar, i, j):
    global count
    queue = deque([(i,j)])
    # print(i,j)
    jar_count = 1
    jar[i][j]=0
    # queue가 없으면 다 돌았다는 뜻
    while queue:
        x, y = queue.pop()
        for nx, ny in direction:
            next_x = x + nx
            next_y = y + ny
            #queue에 추가 되는 조건 
            if 0<= next_x <= N-1 and 0 <= next_y <= N-1 and jar[next_x][next_y]==1:
                # print(next_x, next_y)
                queue.append((next_x,next_y))
                jar[next_x][next_y]=0
                jar_count+=1
    count += 1
    return jar_count
    
jar = []

for _ in range(N):
    jar.append(list(map(int,input().strip())))

# 몇 개의 항아리 단지가 있는지 확인
count = 0
jar_list=[]
# 전체 순회 
for i in range(N):
    for j in range(N):
        # 숫자가 있다면 순회 시작
        if jar[i][j]==1:
            jar_list.append(bfs(jar, i, j))
# 항아리 갯수
print(count)
# 오름 차순 정렬
jar_list.sort()
# 출력
for jar in jar_list:
    print(jar)