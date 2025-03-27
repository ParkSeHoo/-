start = [[i for i in range(1, 15)]]
for _ in range(14):
    start.append([1])
# 1층부터 사람 넣음
for i in range(1, 15):
    #2 호부터 사람넣음
    for j in range(1, 14):
        start[i].append(start[i][j-1]+start[i-1][j])

T = int(input())
for _ in range(T):
    K = int(input())
    N = int(input())
    # K층에 N호에 몇명이 사나요?
    print(start[K][N-1])