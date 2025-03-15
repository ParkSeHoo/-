import sys
sys.stdin = open("Sample_input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    Tree_list = list(map(int, input().split()))

    max_tree = max(Tree_list)
    growth_needed = [max_tree - h for h in Tree_list]  # 나무가 자라야 하는 높이 계산

    even_growth = 0  # 2씩 증가해야 하는 횟수
    odd_growth = 0   # 1씩 증가해야 하는 횟수

    for grow in growth_needed:
        even_growth += grow // 2 # 몫은 짝수로 간다. 
        odd_growth += grow % 2  # 1이 남는 경우 카운트 

    if even_growth ==0 and odd_growth ==0:
        print(f'#{tc} {0}')
        continue

    # 최소 일수 계산
    while even_growth > odd_growth+1:
        even_growth -= 1
        odd_growth += 2

    # print("짝수 횟수", even_growth, "홀수 횟수", odd_growth)
    total_day = 0
    min_day = min(even_growth,odd_growth)
    # print(min_day)
    total_day += min_day * 2
    
    even_growth -= min_day
    odd_growth -= min_day
    
    if even_growth>odd_growth:
        total_day+=2
    elif even_growth<odd_growth :
        total_day += (odd_growth*2) -1
    print(f'#{tc} {total_day}')
