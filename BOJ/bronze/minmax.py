a = int(input())

sample =list(map(int,input().split()))

min_num = sample[0]
max_num = sample[0]

for i in range(len(sample)):
    if min_num>=sample[i]:
        min_num=sample[i]
    if max_num<=sample[i]:
        max_num=sample[i]

print(min_num, max_num)