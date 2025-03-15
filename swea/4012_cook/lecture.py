import sys
sys.stdin = open("sample_input.txt")

T = int(input())


# def perm(idx):
#     if idx ==R:
#         print(out)
#         return
#
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = True
#             out[idx] = arr[i]
#             perm(idx+1)
#             visited[i] = False
def comb(idx, start_i):
    global min_diff
    if idx ==R:
        # 두 요리의 시너지 계산
        sum_a = sum(arr[i][j] for i in range(N) for j in range(N) if selected[i] and selected[j])
        sum_b = sum(arr[i][j] for i in range(N) for j in range(N) if not selected[i] and not selected[j])
        diff = abs(sum_a - sum_b)
        min_diff = min(min_diff, diff)
        return
    for i in range(start_i, N):
        selected[i] = True
        comb(idx+1, i+1)
        selected[i] = False


for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 필살기가 있어야 된다.
    # 자기가 외우는 코드
    R = N//2
    # 재귀로 조합 구하기 <- 순열
    selected = [False] * N
    min_diff = 2 ** 22
    comb( 0, 0 )

    print(f'#{tc} {min_diff}')