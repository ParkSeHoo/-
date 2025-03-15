import sys
sys.stdin = open("input.txt")

T = int(input())

def select(benefit_list, end_num, profit, start):
    global max_profit

    end = end_num
    if end > N:
        return
    
    # 종료 조건
    if end == N:
        max_profit = max(max_profit, profit)
        return
    
    # 재귀
    for i in range(start, len(benefit_list)):
        # print(benefit_list[i])
        if end+benefit_list[i][0] > N:
            continue
        select(benefit_list, end+benefit_list[i][0], profit+benefit_list[i][1], i+1)

for tc in range(1, T+1):
    # N+1일 후에 퇴사함
    N = int(input())
    benefit_list =[]
    for _ in range(N):
        benefit_list.append(list(map(int,input().split())))
    
    # 총 이익
    max_profit = 0

    # 못쓰는 거 제거
    x = 1
    for j in range(N-1, -1, -1):
        if benefit_list[j][0] > x :
            benefit_list[j] = [0, 0]
        x += 1
    # 완탐 
    select(benefit_list, 0, 0, 0)
    print(max_profit)