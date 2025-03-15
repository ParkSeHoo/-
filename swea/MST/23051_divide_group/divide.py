import sys
sys.stdin = open("input.txt")

def find_set(node):
    # 나 자산이 대표자인지를 확인
    if node == parent[node]:
        return node
    else:
        # 내가 대표자가 아닌 경우
        return find_set(parent[node])

def union(x, y):
#     양쪽 노드의 대표자가 동일 한지 확인
    x = find_set(x)
    y = find_set(y)
    # 일단 특별한 기준 없이
    # 각 노드의 값이 정수니까 크기 비교가 가능해서
# 그냥 그 번호가 큰쪽을 대표자로 설정해보자
    if x > y:
        parent[y] = x
    else:
        parent[x] = y

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    data = list(map(int,input().split()))

    # 트리형태를 만들어서 -> 집합으로 처리할 것
        # 두 노드의 대표자가 동일한지 확인하고
        # 이미 두 대표자가 동일하면 무시
        # 두 노드의 집합의 대표자가 다르다면 합치기
    # 대표자 설정
    # 기본적으로 단독으로 조를 구성할 수 있다. -> 최악의 경우 각 노드가 서로 완전히 배타적인 집단들이 N개만큼 만들어 질 수 있다.
    parent =  list(range(N+1)) # 0번 노드 없음
    print(parent)
    for i in range(M):
        # print(data[i])
        x = data[i*2] # 시작노드
        y = data[i*2+1] # 끝 노드
        union(x, y)
    print(parent)
    # 집합의 갯수 구하기
    # stack
    # 사람이 1억명이면 1억번을 조사해야 할 수도 있음
