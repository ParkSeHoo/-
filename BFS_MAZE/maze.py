from collections import deque
import sys

sys.stdin = open("input1.txt")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def FIND_MAZE(queue, maze):
    N = len(maze)
    M = len(maze[0])
    distance = [[0] * M for _ in range(N)]
    distance[0][0] = 1  # 시작 지점은 1로 설정

    while queue:
        current_x, current_y = queue.popleft()

        if current_x == N - 1 and current_y == M - 1:
            return distance[current_x][current_y]  # 최단 거리 반환
        
        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]
            
            if 0 <= next_x < N and 0 <= next_y < M and maze[next_x][next_y] == 1:
                queue.append((next_x, next_y))
                maze[next_x][next_y] = 0  # 방문 처리
                distance[next_x][next_y] = distance[current_x][current_y] + 1
    
    return -1  # 도달 불가능한 경우

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    maze = []
    for i in range(N):
        maze.append(list(map(int, input().strip())))

    to_go_queue = deque()
    to_go_queue.append((0, 0))

    print(FIND_MAZE(to_go_queue, maze))