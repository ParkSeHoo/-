import sys
sys.stdin = open("sample_input.txt")

T = int(input())

def find_combi(synergy, temp_list, start):
    if len(temp_list) == 4:
        combi.append(temp_list[:])  # 깊은 복사 추가
        return
    for i in range(start, N):
        temp_list.append(i)
        find_combi(synergy, temp_list, i+1)
        temp_list.pop()  # 백트래킹 추가

def find_min_diff(combi, i):
    global min_diff
    temp_combi = combi[i]
    min_diff =min(min_diff,abs(synergy[temp_combi[0]][temp_combi[1]]+synergy[temp_combi[1]][temp_combi[0]] - synergy[temp_combi[2]][temp_combi[3]]-synergy[temp_combi[3]][temp_combi[2]]))

    min_diff =min(min_diff,abs(synergy[temp_combi[0]][temp_combi[2]]+synergy[temp_combi[2]][temp_combi[0]] - synergy[temp_combi[1]][temp_combi[3]]-synergy[temp_combi[3]][temp_combi[1]]))
    min_diff =min(min_diff,abs(synergy[temp_combi[0]][temp_combi[3]]+synergy[temp_combi[3]][temp_combi[0]] - synergy[temp_combi[2]][temp_combi[1]]+synergy[temp_combi[1]][temp_combi[2]]))


for tc in range(1, T+1):
    N = int(input())
    synergy = []
    min_diff = 999999
    for _ in range(N):
        synergy.append(list(map(int, input().split())))
    combi = []
    temp_list = []
    find_combi(synergy, temp_list, 0)
    for i in range(len(combi)):
        find_min_diff(combi, i)
    print(f'#{tc} {min_diff}')