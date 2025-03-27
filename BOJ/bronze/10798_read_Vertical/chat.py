word_list = [input().rstrip() for _ in range(5)]

read_list = []

max_len = max(len(row) for row in word_list)

for j in range(max_len):
    for i in range(5):
        if j < len(word_list[i]):
            read_list.append(word_list[i][j])

print("".join(read_list))
