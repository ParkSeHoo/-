import sys
sys.stdin = open("sample_input.txt")

T = int(input())

def sumofnum(n_list, K, start, temp_list, memo):
    temp_tuple = tuple(temp_list)  # 리스트를 튜플로 변환하여 메모이제이션
    # print(temp_list)

    # 이미 계산한 조합이면 중복 방지
    if temp_tuple in memo:
        return 0
    memo.add(temp_tuple)

    # 현재 선택된 리스트의 합이 K 이상이면 경우의 수 증가
    if sum(temp_list) == K:
        # print(temp_list)
        return 1

    count = 0
    for i in range(start, len(n_list)):
        temp_list.append(n_list[i])
        count += sumofnum(n_list, K, i+1, temp_list, memo)  # i+1을 넘겨 중복 방지
        temp_list.pop()
    
    return count

for tc in range(1, T+1):
    N, K = map(int, input().split())
    n_list = list(map(int, input().split()))

    memo = set()  # 튜플을 저장할 set 사용
    num_of_case = sumofnum(n_list, K, 0, [], memo)

    print(f'#{tc} {num_of_case}')
