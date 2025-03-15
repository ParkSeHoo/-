import sys
sys.stdin = open("sample1.txt")

# 보드 잘라야함

def make_perfect_chess_map(chess_map):
    flag = True
    count = 0
    for i in range(len(chess_map)):
        for j in range(len(chess_map)):
            if flag:
                if (j+1)%2!=0 and chess_map[i][j]=='B':
                    count+=1
                elif (j+1)%2==0 and chess_map[i][j]=='W':
                    count+=1
            else:           -
                if (j+1)%2!=0 and chess_map[i][j]=='W':
                    count+=1
                elif (j+1)%2==0 and chess_map[i][j]=='B':
                    count+=1         
        flag = not flag

    return count

N, M = map(int, input().split())

# WBWB
# BWBW
# 체스맵
chess_map =[]
for _ in range(N):
    chess_map.append((str( input().split())))
# print(chess_map)
print(make_perfect_chess_map(chess_map))
