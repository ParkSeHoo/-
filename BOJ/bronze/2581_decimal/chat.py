M = int(input())
N = int(input())

decimal_sum = 0
min_decimal = -1

for num in range(M, N + 1):
    if num < 2:
        continue
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        decimal_sum += num
        if min_decimal == -1:
            min_decimal = num

if decimal_sum == 0:
    print(-1)
else:
    print(decimal_sum)
    print(min_decimal)
