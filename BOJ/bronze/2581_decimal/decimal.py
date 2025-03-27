M = int(input())
N = int(input())

#소수 리스트
if N>2:
    decimal_list = [2, 3]
elif N == 2:
    decimal_list =[2]
else:
    decimal_list = []
# 소수합
decimal_sum = 0
min_decimal=[]

for i in range(4, N+1):
    flag = True
    start = 2
    while start**2 <= i:
        if i % start == 0:
            flag = False
            break
        # print(start,i)
        start += 1
    if flag:
        decimal_list.append(i)

for j in range(len(decimal_list)):
    if decimal_list[j] >= M:
        decimal_sum += decimal_list[j]
        min_decimal.append(decimal_list[j])
if decimal_sum == 0:
    print(-1)
else:
    print(decimal_sum)
    print(min(min_decimal))