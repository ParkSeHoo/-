fibo=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
N = int(input())
for j in range(18,99):
    fibo.append(fibo[j-1]+fibo[j-2])
print(fibo[N])