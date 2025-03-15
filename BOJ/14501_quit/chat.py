import sys

sys.stdin = open("input.txt")

T = int(input())


def select(day, profit):
    global max_profit

    # 퇴사일을 넘으면 종료
    if day > N:
        return

    # 최대 이익 갱신
    max_profit = max(max_profit, profit)

    # day 이후 상담을 선택
    for i in range(day, N):
        time, price = benefit_list[i]

    # 상담을 진행할 수 있는 경우만 진행
        if i + time <= N:
            select(i + time, profit + price)


for _ in range(T):
    N = int(input())
    benefit_list = [list(map(int, input().split())) for _ in range(N)]

    max_profit = 0
    select(0, 0)
    print(max_profit)
