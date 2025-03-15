from collections import deque
import sys
sys.stdin = open("input.txt")

T = int(input())



for tc in range(1, T+1):
    # 입력받을 숫자
    N = int(input())
    numbers = deque(map(int, input().split()))
    # print(numbers)
    profit = 0
    profit_count = 0
    repeat = len(numbers)
    total_profit = 0
    temp_max = max(numbers)
    while numbers:
        if numbers[0] == temp_max:
            total_profit += profit_count*numbers[0]-profit
            profit = 0
            profit_count = 0
            numbers.popleft()
            if numbers:
                temp_max = max(numbers)
        else:
            profit += numbers.popleft()
            profit_count += 1
    print(f'#{tc } {total_profit}')


