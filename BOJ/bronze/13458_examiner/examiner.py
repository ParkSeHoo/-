# 시험장 갯수
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
need_people = N
# too greedy
# total_A = sum(A)
# total_A -= N*A
# if total_A>0:
#     while total_A > 0:
#         total_A -= C
#         need_people += 1
#     total_A//C

for i in range(N):
    temp = A[i]-B
    if temp <= 0:
        continue
    if temp <= C:
        need_people += 1
        continue
    if temp % C == 0:
        need_people += temp//C
    else:
        need_people += (temp // C)+1
print(need_people)