import sys
sys.stdin = open("input.txt")
# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7

# 부모 찾기
def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]

# 합치기
def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
# 노드 수
N = int(input())

# 노드 관계 수
rel_node = int(input())

join_list = []

for _ in range(rel_node):
    join_list.append(tuple(map(int, input().split())))

parent = [0]*(N+1)
for i in range(len(parent)):
    parent[i] = i

for rel in join_list:
    x = rel[0]
    y = rel[1]
    union(x, y)
    # print(parent)

for i in range(N+1):
    find_set(i)

count = 0
for O in parent:
    if O == 1:
        count += 1

print(count-1)