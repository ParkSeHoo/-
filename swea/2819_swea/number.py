import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    numberlist = []
    for _ in range(4):
        numberlist.append(list(map(int, input().split())))
    print(numberlist)