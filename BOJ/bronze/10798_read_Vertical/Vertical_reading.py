word_list = [list(map(str, input())) for _ in range(5)]
read_list = []

max1 = 0
for i in range(len(word_list)):
    if len(word_list[i]) >= max1:
        max1 = len(word_list[i])

for j in range(max1):
    for i in range(len(word_list)):
        if word_list[i] != []:
            read_list.append(word_list[i].pop(0))

print("".join(map(str, read_list)))