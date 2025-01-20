a = int(input())
max_kill = 0
for p in range(a):
    num, kill = map(int, input().split())
    sample=[]
    for _ in range(num):
        list1 = list(map(int,input().split()))
        sample.append(list1)
    for i in range(num):
        for j in range(num):
            kill_fly = 0
            X_kill_fly = 0
            fly = 0

        # print(i,j)

        for k in range(1, kill):
            # + 자 모으기
            if j + k < num:
                kill_fly += sample[i][j + k]
                # print(sample[i][j+k])
            if i + k < num:
                kill_fly += sample[i + k][j]
                # print(sample[i+k][j])
            if i - k >= 0:
                kill_fly += sample[i - k][j]
                # print(sample[i-k][j])
            if j - k >= 0:
                kill_fly += sample[i][j - k]
                # print(sample[i][j-k])
            # X 자 모으기
            if i + k < num and j + k < num:
                X_kill_fly += sample[i + k][j + k]
            if i + k < num and j - k >= 0:
                X_kill_fly += sample[i + k][j - k]
            if i - k >= 0 and j + k < num:
                X_kill_fly += sample[i - k][j + k]
            if i - k >= 0 and j - k >= 0 :
                X_kill_fly += sample[i - k][j - k]

        kill_fly += sample[i][j]
        X_kill_fly += sample[i][j]
        # print(kill_fly)
        # print(X_kill_fly)
        if X_kill_fly >= kill_fly:
            fly = X_kill_fly
        else:
            fly = kill_fly
        if max_kill <= fly:
            max_kill = fly
print("#"+str(p+1),end=" ")
print(max_kill)


