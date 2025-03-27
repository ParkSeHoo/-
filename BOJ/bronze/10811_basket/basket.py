def swapping(start, end, basket):
    start -= 1
    end -= 1

    if start == end:
        return basket
    if abs(start-end) == 1:
        c = basket[start]
        basket[start] = basket[end]
        basket[end] = c
        # basket[start], basket[end] = basket[end], basket[start]
        return basket
    else:
        temp_list = []
        for i in range(end, start-1, -1):
            temp_list.append(basket[i])
        return basket[:start]+temp_list+basket[end+1:]

N, M = map(int, input().split())
basket = [i for i in range(1, N+1)]
change = []
for _ in range(M):
    change.append(tuple(map(int, input().split())))

for a, b in change:
    basket = swapping(a, b, basket)

print(" ".join(map(str, basket)))