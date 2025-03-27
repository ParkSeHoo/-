# 신청자수
N = int(input())
assing_list = list(map(int, input().split()))
T, P = map(int,input().split())
total_set = 0
for i in range(len(assing_list)):
    if assing_list[i]%T == 0:
        total_set += assing_list[i]//T
    else:
        total_set += (assing_list[i] // T)+1
print(total_set)
print(N//P, N%P)