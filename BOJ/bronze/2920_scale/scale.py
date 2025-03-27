# c,d,e,f,g,a,b,C 8 개음
music = list(map(int,input().split()))
temp = music[0]
start = music[0]
flag = True
for i in range(1, len(music)):
    if start <= music[i]:
        start = music[i]
        flag = True
    else:
        start = -1
        flag = False
        break

# print(music[-1])
# print(start)
if start == music[-1] and start >= temp:
    print('ascending')
start = music[0]
for i in range(1, len(music)):
    if start >= music[i]:
        start = music[i]
    else:
        start = -1
        break
# print(start)
# print(music[-1])
if start == music[-1] and start <= temp:
    print('descending')
else:
    if not flag:
        print('mixed')