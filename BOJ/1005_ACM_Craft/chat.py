import sys
import time
sys.stdin = open('input.txt')

def check_parent(x):
    if dp[x] != -1:  # 이미 계산된 값이면 반환
        return dp[x]

    if not parent[x]:  # 부모가 없는 경우
        dp[x] = how_long[x-1]
        return dp[x]

    max_time = 0
    for p in parent[x]:
        max_time = max(max_time, check_parent(p))

    dp[x] = max_time + how_long[x-1]
    return dp[x]

# 첫줄에 TC
T = int(input())

start_time = time.time()  # 실행 시간 측정 시작

for tc in range(1, T+1):
    N, K = map(int, input().split())
    how_long = list(map(int, input().split()))
    order = [tuple(map(int, input().split())) for _ in range(K)]
    end_condition = int(input())

    parent = [[] for _ in range(N+1)]
    for x, y in order:
        parent[y].append(x)

    dp = [-1] * (N + 1)  # DP 테이블 초기화
    result = check_parent(end_condition)

    print(f"Test Case #{tc}: {result}")

# end_time = time.time()  # 실행 시간 측정 종료
# print(f"🚀 최적화된 코드 실행 시간: {end_time - start_time:.5f} 초")
