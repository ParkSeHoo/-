# def best_combi(select_list, max_value, temp_list, start):
#     # select_list에서의 조합 최댓값
#     global select_max
#     print(temp_list)
#     print(select_max)
#     # 끝나는 조건
#     if sum(temp_list) > max_value:
#         return select_max
#
#     temp2 = 0
#     for i in range(len(temp_list)):
#         temp2 += temp_list[i] ** 2
#     if select_max < temp2:
#         select_max = temp2
#     # 1번 선택 후 체크, 2번 선택 후 체크
#     # 1번 안선택하고 2번하고 체크
#
#     for le in range(start, len(select_list)):
#         best_combi(select_list, max_value, temp_list, start + 1)
#         temp_list.append(select_list[le])
#         best_combi(select_list, max_value, temp_list, start + 1)
#
#     return

def best_combi(select_list, max_value, temp_list, start, select_max):
    # 현재 조합 출력
    print(temp_list)

    # 합이 max_value를 초과하면 종료
    if sum(temp_list) > max_value:
        return select_max

    # 현재 조합의 제곱합 계산
    temp2 = sum(x ** 2 for x in temp_list)
    select_max = max(select_max, temp2)

    # 조합 생성 (백트래킹 활용)
    for i in range(start, len(select_list)):
        temp_list.append(select_list[i])
        select_max = best_combi(select_list, max_value, temp_list, i + 1, select_max)
        temp_list.pop()  # 원래 상태로 복구 (백트래킹)

    return select_max



select_max = 0
test_list = [5,5,7]
max_val = 10
temp_list = []
start = 0
print(best_combi(test_list, max_val, temp_list, start,select_max))