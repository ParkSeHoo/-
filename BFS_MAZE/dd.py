from collections import deque
import sys

sys.stdin = open("input1.txt")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def FIND_MAZE(queue, maze):
    # 길 못 찾으면 -1
    if not queue:
        return -1 

    current_x, current_y, count = queue.popleft()

    # 도착하면 최소 거리 반환
    if current_x == len(maze) - 1 and current_y == len(maze[0]) - 1:
        return count  

    for i in range(4):
        next_x = current_x + dx[i]
        next_y = current_y + dy[i]

        if 0 <= next_x < len(maze) and 0 <= next_y < len(maze[0]) and maze[next_x][next_y] == 1:
            maze[next_x][next_y] = 0  # 방문 처리
            queue.append((next_x, next_y, count + 1))
            # for i in maze:
                # print(i)
            # print("")
    return FIND_MAZE(queue, maze)  # 재귀적으로 호출

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 미로
    maze = []
    for i in range(N):
        maze.append(list(map(int, input().strip())))
    count=1
    queue = deque([(0, 0, count)])  # 시작 위치와 이동 횟수
    maze[0][0]=0
    result = FIND_MAZE(queue, maze)
    print(result)  # 결과 출력
