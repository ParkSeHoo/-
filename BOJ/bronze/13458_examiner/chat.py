import math

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

need_people = 0

for students in A:
    # 총감독관 1명은 무조건 필요
    students -= B
    need_people += 1

    # 남은 학생들을 부감독관으로 커버
    if students > 0:
        need_people += math.ceil(students / C)

print(need_people)
