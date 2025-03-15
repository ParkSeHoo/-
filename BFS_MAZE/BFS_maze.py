from collections import deque
import sys

sys.stdin = open("input1.txt")

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def FIND_MAZE(queue, maze):
    # 길 못 찾으면 -1
    if not queue:
        
        return -1 
    
    current_x, current_y, count = queue.popleft()
     
    # 찾으면 최단거리 리턴
    if current_x==len(maze)-1 and current_y == len(maze[0])-1 :
        
        return count
    
    for i in range(4):
        next_x = current_x + dx[i]
        next_y = current_y + dy[i]

        if 0<= next_x < len(maze) and 0<= next_y < len(maze[0]) and maze[next_x][next_y] == 1:
            maze[next_x][next_y]=0  
            queue.append([next_x, next_y, count+1])

    # if 0<= current_x <= M-1 and 0<= current_y <= N-1:
        # maze[current_x][current_y]=0
        # FIND_MAZE(queue,maze)

    return FIND_MAZE(queue,maze)

T = int(input())

for tc in range(1,T+1):

    N, M = map(int, input().split() )

    # 이중리스트로 미로 만들기 
    maze =[]
    # 도착지까지 최소로 간것은 몇 번만에 갔나?
    count = 1

    # distance = [[0] * M for _ in range(N)]
    # distance[0][0] = 1  # 시작점 거리 1

    for i in range(N):
        maze.append(list ( map( int,input().split() ) ) )

    to_go_queue = deque()
    to_go_queue.append([0, 0, count])
    result = FIND_MAZE(to_go_queue, maze)
    print(result)

