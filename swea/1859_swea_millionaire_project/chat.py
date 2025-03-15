import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    stack = []  # 주식을 매수한 가격을 저장할 스택
    total_profit = 0

    for price in numbers:
        while stack and stack[-1] < price:
            total_profit += price - stack.pop()  # 현재 가격이 스택의 최상단보다 크면 매도
        stack.append(price)  # 현재 가격을 스택에 추가

    print(f'#{tc} {total_profit}')
