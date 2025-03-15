from pprint import pprint
## list compresion

# num=5
# data1 = [ [0] * (num) for _ in range(num) ]

# pprint(data1)

# data2 = [[0 for _ in range(num)] for _ in range(num) ]

# pprint(data2)

## packing, unpacking

# numbers =(1,2,3,4,5)
numbers =[1,2,3,4,5]

a, *b = numbers
print(a)
print(b)