import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    # N = 건물 개수, K = 규칙 개수
    N, K = map(int, input().split())

    # 각 건물의 건설 시간
    how_long = [0] + list(map(int, input().split()))  # 인덱스 1부터 사용

    # DP 테이블 (각 건물까지 걸리는 최대 시간)
    dp = how_long[:]

    # 규칙 설명 x -> y (x가 완성되어야 y를 지을 수 있음)
    order = []
    for _ in range(K):
        x, y = map(int, input().split())
        order.append((x, y))

    # 목표 건물 번호
    end_condition = int(input())

    # DP 갱신 (순차적으로 모든 건물 탐색)
    for _ in range(N):  # N번 반복하면서 모든 건물을 갱신
        for x, y in order:
            dp[y] = max(dp[y], dp[x] + how_long[y])  # y 건물의 최장 건설 시간 갱신

    # 결과 출력
    print(dp[end_condition])
