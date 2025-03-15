a = int(input())
for p in range(a):
    num, kill = map(int, input().split())
    sample = []
    max_kill = 0  # 각 테스트 케이스별 초기화
    for _ in range(num):
        list1 = list(map(int, input().split()))
        sample.append(list1)

    for i in range(num):
        for j in range(num):
            kill_fly = 0
            X_kill_fly = 0

            # + 자 모으기
            for k in range(1, kill):
                if j + k < num:
                    kill_fly += sample[i][j + k]
                if i + k < num:
                    kill_fly += sample[i + k][j]
                if i - k >= 0:
                    kill_fly += sample[i - k][j]
                if j - k >= 0:
                    kill_fly += sample[i][j - k]
                # X 자 모으기
                if i + k < num and j + k < num:
                    X_kill_fly += sample[i + k][j + k]
                if i + k < num and j - k >= 0:
                    X_kill_fly += sample[i + k][j - k]
                if i - k >= 0 and j + k < num:
                    X_kill_fly += sample[i - k][j + k]
                if i - k >= 0 and j - k >= 0:
                    X_kill_fly += sample[i - k][j - k]

            kill_fly += sample[i][j]
            X_kill_fly += sample[i][j]

            # 최댓값 선택
            fly = max(kill_fly, X_kill_fly)
            max_kill = max(max_kill, fly)

    # 테스트 케이스 결과 출력
    print("#" + str(p + 1), max_kill)
