import sys
sys.stdin = open("input1.txt")

T = int(input())

def check_width(ruins, visited, i, j, count):
    global max_length
    count1 = count
    if 0 <= i < N and 0 <= j < M and ruins[i][j] == 1 and visited[i][j]:
        count1 += 1
        visited[i][j] = False

        # 오른쪽으로 이동
        check_width(ruins, visited, i, j + 1, count1)

        # 방문초기화
        visited[i][j] = True
    else:
        max_length = max(max_length, count1)
        return

def check_length(ruins, visited, i, j, count):
    global max_length
    count1 = count
    if 0 <= i < N and 0 <= j < M and ruins[i][j] == 1 and visited[i][j]:
        count1 += 1
        visited[i][j] = False

        # 아래쪽으로 이동
        check_length(ruins, visited, i + 1, j, count1)

        # 방문초기화
        visited[i][j] = True
    else:
        max_length = max(max_length, count1)
        return

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    ruins = [list(map(int, input().split())) for _ in range(N)]
    visited = [[True] * M for _ in range(N)]
    max_length = 0

    for i in range(N):
        for j in range(M):
            if ruins[i][j] == 1 and visited[i][j]:
                check_length(ruins, visited, i, j, 0)
                check_width(ruins, visited, i, j, 0)
    print(f'#{tc} {max_length}')
