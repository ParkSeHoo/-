N = int(input())
start = 2
while N != 1:
    # print('?')
    if N == 1:
        break
    if N % start == 0:
        print(start)

        N = N/start
        # print(N)
    else:
        start += 1
