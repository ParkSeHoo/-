import copy
import sys

sys.stdin = open("sample_input.txt")

# TC 2번 9번 해결 해야함
def cal_honey(honey_map, count):
    # 2개를 선택 해야함
    # 하나 선택하고 숫자 0으로 만들고 중복 선택 안되게 만들면 되나?
    # 첫번째 선택이 끝까지 가면 더 이상 진행 안되도록 만듬
    # 종료조건 두개 선택 되서 최댓값이랑 비교하고 리턴?
    # for 문이랑 재귀랑 섞어서 쓰면 어떨까?

    # global max_hoeny
    #
    # count+=1
    # if count==2:
    #     return
    #
    # for i in range(col):
    #     for j in range(len(honey_map[0])-select+1):
    #         select_honey = honey_map[i][j:j+select]
    #         honey_map[i][j:j+select]=0
    #
    pass

def best_combi(select_list, max_value, temp_list,start):
    # select_list에서의 조합 최댓값
    select_max = 0

    # 끝나는 조건
    if sum(temp_list) > max_value:
        temp2 = 0
        for i in range(len(temp_list)):
            temp2 += temp_list[i]**2
        if select_max < i:
            select_max = i
            return select_max
    # 1번 선택 후 체크, 2번 선택 후 체크
    # 1번 안선택하고 2번하고 체크

    for le in range(start,len(select_list)):
        best_combi(select_list, max_value, temp_list, start + 1)
        temp_list.append(select_list[start])
        best_combi(select_list, max_value, temp_list, start + 1)
    
    return

T = int(input())

T = 10
for tc in range(1, T + 1):
    condition = list(map(int, input().split()))
    col, select, select_max_val = condition

    honey_map = []
    for _ in range(col):
        honey_map.append(list(map(int, input().split())))

    # 꿀을 모은 경우 모음집
    hoeny_list = []

    # 꿀을 제일 많이 모은 경우
    max_hoeny = 0

    # 3개에서 3개 뽑는거는 1번
    # 4개에서 2개 뽑는거는 3번
    # 4개에서 3개 뽑는거는 2번

    # 2개를 뽑는거임

    for i in range(col):
        for j in range(len(honey_map[0]) - select + 1):
            select_first = honey_map[i][j:j + select]
            # honey_map[i][j:j+select]=0
            temp = copy.deepcopy(honey_map)
            for l in range(select):
                temp[i][j + l] = 0
            # print(temp)
            # print(select_first)
            # 조건 수정 해야 함
            # 5 5 7 , max_val =10 인 경우 49 보다 50이 더 큼
            # 주어진 숫자 리스트에서 제곱 값이 가장 큰 조합을 찾아야 한다.
            # 주어진 select_max_val 보다 크면 제일 작은 값부터 삭제
            while sum(select_first) > select_max_val:
                if sum(select_first) > select_max_val:
                    select_first = sorted(select_first, reverse=True)
                    select_first.pop()

            # 안에 있는 값 제곱으로 변경
            for pp in range(len(select_first)):
                select_first[pp] = select_first[pp] ** 2

            # 두 번째 집합 선택
            for e in range(col):
                # print("두번째 시작")
                for k in range(len(honey_map[0]) - select + 1):
                    # 조건 고쳐야함
                    second_select = temp[e][k:k + select]
                    if 0 in second_select:
                        continue
                    else:
                        pass
                    # print("while문 돌아간다. ")
                    # print(second_select)
                    while sum(second_select) > select_max_val:
                        # print(sum(second_select))
                        if sum(second_select) > select_max_val:
                            second_select = sorted(second_select, reverse=True)
                            second_select.pop()
                    # print("두번째 제곱한다.")
                    for pp in range(len(second_select)):
                        second_select[pp] = second_select[pp] ** 2
                    # print(select_first, second_select)

                    temp1 = sum(select_first) + sum(second_select)
                    if len(hoeny_list) == 0:
                        hoeny_list.append(temp1)
                    elif max(hoeny_list) < temp1:
                        hoeny_list.append(temp1)

    print(f'#{tc} {max(hoeny_list)}')
