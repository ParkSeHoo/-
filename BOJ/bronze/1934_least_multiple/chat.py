def prime_factorization(n):
    factor_dict = {}
    start = 2
    while start * start <= n:
        while n % start == 0:
            factor_dict[start] = factor_dict.get(start, 0) + 1
            n = n // start
        start += 1
    if n > 1:
        factor_dict[n] = factor_dict.get(n, 0) + 1
    return factor_dict

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())

    if A == 1:
        print(B)
        continue
    if B == 1:
        print(A)
        continue

    A_dict = prime_factorization(A)
    B_dict = prime_factorization(B)

    all_primes = set(A_dict) | set(B_dict)
    lcm = 1
    for prime in all_primes:
        exponent = max(A_dict.get(prime, 0), B_dict.get(prime, 0))
        lcm *= prime ** exponent

    print(lcm)
