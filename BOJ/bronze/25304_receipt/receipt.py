X = int(input())
N = int(input())
price = []
quantity = []
receipt = {}
total_price = 0
for _ in range(N):
    a, b = map(int, input().split())
    price.append(a)
    quantity.append(b)
    receipt[a] = b
    # total_price += a*b
# for price1, quantity1 in receipt.items():
#   /  total_price += price1*quantity1
for i in range(N):
    total_price+=price[i]*quantity[i]

if total_price == X:
    print('Yes')
else:
    print('No')