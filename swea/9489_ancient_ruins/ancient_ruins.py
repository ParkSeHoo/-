import sys
sys.stdin = open("input1.txt")

T = int(input())

def check_width(ruins, visited, i, j, count):
    global max_length
    count1 = count
    if 0<=i<N and 0<=j<M and ruins[i][j]==1 and visited[i][j]:
        count1+=1 
        visited[i][j]=False

        # if 0<=i+1<N and 0<=j+1<M and ruins[i+1][j]==1 and ruins[i][j+1]==1:
            # visited[i][j]=True

        check_length(ruins,visited, i,j+1,count1)
        visited[i][j]=True
    else:
        max_length = max(max_length, count1)
        return
def check_length(ruins, visited, i, j, count):
    global max_length
    count1 = count
    if 0<=i<N and 0<=j<M and ruins[i][j]==1 and visited[i][j]:
        count1+=1 
        visited[i][j]=False
        # 여러방향으로 갈 수 있으면 True
        # if 0<=i+1<N and 0<=j+1<M and ruins[i+1][j]==1 and visited[i+1][j] and ruins[i][j+1]==1 and visited[i][j+1]:
            # visited[i][j]=True

        check_length(ruins,visited, i+1,j,count1)
        visited[i][j]=True
    else:
        max_length = max(max_length, count1)
        return
for tc in range(1, T+1):

    N, M = map(int,input().split())
    # 유물지도
    ruins=[]
    # 유물 최대 길이
    max_length=0
    visited= [[True] * M  for _ in range(N)]


    for _ in range(N):
        ruins.append(list(map(int,input().split())))

    print(ruins)

    for i in range(N):
        for j in range(M):
            if ruins[i][j]==1 and visited[i][j]:
                check_length(ruins, visited, i, j, 0)
                check_width(ruins, visited, i, j, 0)
    print(max_length)