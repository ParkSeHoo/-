import sys 
sys.stdin = open("input.txt")

T = 5 
directions= [(1,0),(0,1),(-1,0),(0,-1)]

def checktomatoexception(field):
    for i in range(len(field)):
        for j in range(len(field[0])):
            if i==0 and j==0 and field[i][j]==0 and field[i+1][j]==-1 and field[i][j+1]==-1:
                return False
            if i==0 and j==len(field[0])-1 and field[i][j]==0 and field[i+1][j]==-1 and field[i][j+1]==-1:
                return False
            if i==0 and j==0 and field[i][j]==0 and field[i+1][j]==-1 and field[i][j+1]==-1:
                return False
            if i==0 and j==0 and field[i][j]==0 and field[i+1][j]==-1 and field[i][j+1]==-1:
                return False

def check_tomatoes(field, temp_list, x, y):
    if field[x][y] ==1:
        for i in range(4):
            # 조건 걸고 nx, ny 통과되면
            # temp_list 바꿔주면 될듯?
            pass
    
    return temp_list

for tc in range(1,T+1):
    # 가로, 세로
    row, col = map(int, input().split())
    # 1은 익은, 0은 안익은, -1은 토마토가 없는
    # 밭 이름
    field= []
    # 밭 채우기
    for i in range (col) : 
        field.append(list(map(int,input().split())))
    # 총 걸린 날짜
    day = 0
    flag = True
    tomato_field=[]
    while flag:
        day += 1
        for i in range(row):
            for j in range(col):
                temp_list =[ [0]*row for i in range(col)]
                # 밑에 필드 상태 업데이트 하는 것도 로직 틀림 다시 만들어야함
                tomato_field = check_tomatoes(field, temp_list, j, i)
        
        # 종료 조건 : 토마토가 다 익음 -> 예외 처리 못함 -1 나오는 케이스 어떻게 처리할 건지 생각해야함
        if not 0 in tomato_field:
            flag = False