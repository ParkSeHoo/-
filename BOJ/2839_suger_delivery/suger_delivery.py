# 입력받을 설탕 kg
suger = int(input())

# 몇 개로 나누어 옮겼나
count = 0

flag = True

# 처음부터 5로 나눠지면 베스트 케이스
if suger % 5 == 0:
    print(suger//5)
# 안나눠 졌을 떄 최솟값을 찾는 법
else:
    # 5로 나눈 나머지
    temp_suger = suger % 5
    # 5로 나눴을 때 옮긴 횟수
    count = suger // 5

    while flag:
        # 5 + 3 으로 나눠지면 count 반환하고 while 탈출
        if temp_suger % 3 == 0:
            count += temp_suger//3
            flag = False
        # 안나눠졋으면 나머지에 5더하고 count 1 빼면서 반복
        else:
            temp_suger += 5
            count -= 1
        # temp_suger가 원래 무게보다 많이 나가면 찾을 필요가 없음
        if temp_suger > suger:
            flag = False
            count = -1

    print(count)