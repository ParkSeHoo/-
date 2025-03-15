# 리스트로 받는다. 
# 앞에 숫자가 작은 순서대로 정렬한다. 
# 딕셔너리 을 만들어서 도착지점에 도착하는 최소 이동횟수를 구한다. 사다리, 뱀 둘 다 구함  
# 딕셔너리 키가 가장 높은 숫자가 적힌 곳으로 이동
# 이동한 위치에서 100까지 가는데에 최소 횟수를 구하면 된다. 
# 뱀 위치 확인 하면서 6이하의 최대 숫자 가면서 100이 되면 멈춤

import sys
sys.stdin = open("sample1.txt")

# N -> 사다리 갯수 # M -> 뱀 갯수
N, M = map(int,input().split())
# 사다리 # 뱀
ladders, snakes, total_short_cut = [], [],[]
# 지름길
short_cut =[]
# 시작점 # 끝점 
start, end = 1, 100

for _ in range(N):
    temp_ladder = tuple(map(int, input().split()))
    ladders.append(temp_ladder)
    total_short_cut.append(temp_ladder)
for _ in range(M):
    temp_snake= tuple(map(int, input().split()))
    snakes.append(temp_snake)
    total_short_cut.append(temp_snake)

ladders.sort()
snakes.sort()
total_short_cut.sort()

for i in range(len(total_short_cut)):
    temp_start=1
    count=0
    # 가는길에 지름길을 쓸 수 있으면 지름길로 가라?
    # if not short_cut:
    #     for k in range(len(short_cut)):
    #         if short_cut[k].key>total_short_cut[i][0]:
    #             temp_start = short_cut[k-1].key
    #             count = short_cut[k-1].value
    #             break
    # 최소치 넘을 때까지 더함
    while temp_start < total_short_cut[i][0]:
        go = 6
        #가는 길에 뱀 있나 확인
        for j in range(M):
            if temp_start+go == snakes[j][0]:
                go -= 1
        temp_start+=go
        count += 1
    # 리스트에 딕셔너리로 지름길에 걸리는 최소 횟수 추가 
    short_cut.append({ 'value':total_short_cut[i][1], 'count': count})
    if len(short_cut)>1:
        short_cut.sort( key = lambda x : x['value'])

    print(short_cut)

print(short_cut)

print(ladders)
print(snakes)