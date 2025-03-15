# 0,0 -> 0,1 -> 0,2 -> 0,3 -> 숫자를 만날때 까지 while 만나면,  숫자를 바꿔준다. 
# 
import copy
import sys
from pprint import pprint
sys.stdin = open("sample_input.txt")

T = int(input())

T = 1



def serch_start(block_list, break_count, count_start):
    global sum_reserve
    # 종료조건
    if break_count == 0:
        sum1 = 0
        for i in range(len(block_list)):
            sum1 +=sum(block_list[i])
            sum_reserve.append(sum)
        return

    # 어차피 완전탐색이라 같은 곳 몇 번 뒤져도 상관없음
    break_block(block_list, count_start)
    print("break끝남")
    # 한 자리 에서만 구멍팜
    serch_start(block_list, break_count-1, count_start)
    # 돌아 가면서 팜
    serch_start(block_list, break_count-1, count_start+1)
    # 다음 자리 부터 팜
    serch_start(block_list, break_count, count_start+1)




# 블럭이 사라진 후 행렬을 반환하는 함수
def break_block(block_list, count_start):
    #y좌표
    down_col = 0
    while True:
        # print(count_start)
        # print(down_col)
        # print(block_list[down_col][count_start])
        if block_list[down_col][count_start] == 1:
            block_list[down_col][count_start]=0
            break

        if block_list[down_col][count_start] > 1:
            boom = block_list[down_col][count_start]
            row = count_start
            col = down_col
            block_erase(boom, block_list, row, col)
            break
        down_col+=1

    pprint(block_list)
    return


def block_erase(boom, break_block, row, col):
    i=0
    print("1 이상이 들어왔다. ")
    while i < boom:
        #좌우 범위 초과 조건 달아야함 
        # 1일 때 어떻게 바꿀지 생각해야함
        if break_block[row+i][col+i]>1:
            boom = break_block[row+i][col+i] 
            row = row+i
            col = col+i
            break_block[row+i][col+i] = 0
            print(block_list)
            block_erase(boom, break_block, row, col)

        if break_block[row+i][col+i]>1:
            boom = break_block[row+i][col+i] 
            row = row+i
            col = col+i
            break_block[row+i][col+i] = 0
            print(block_list)
            block_erase(boom, break_block, row, col)

        if break_block[row+i][col-i]>1:
            boom = break_block[row+i][col-i] 
            row = row+i
            col = col-i
            break_block[row+i][col-i] = 0
            print(block_list)
            block_erase(boom, break_block, row, col)

        if break_block[row-i][col-i]>1:
            boom = break_block[row-i][col-i] 
            row = row - i
            col = col - i
            break_block[row-i][col-i]=0
            print(block_list)
            block_erase(boom, break_block, row, col)
            

        



for tc in range(1,T+1):
    
    break_count, row, col =  map( int, input().split() )
    # block 생긴 모양
    block_list =[]
    
    #시작 row
    count_start = 2

    # block_count
    block_count = 0
    for i in range(col):
        block_list.append(list(map(int, input().split())))
    
    sum_reserve =[]

    pprint(block_list)

    # print(sum(block_list[1]))

    # for _ in range(break_count):
    
    serch_start(block_list, break_count, count_start)

    
