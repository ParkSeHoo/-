# a = int(input())

# for i in range(a):
#     b, c= map(str,input().split())
#     b = int(b)
#     charlist=""
#     for j in range(len(c)):
#         # print(,end="")
#         charlist+=(b*c[j:j+1])
#     print(charlist)

a = int(input())  # 테스트 케이스 개수 입력

for i in range(a):
    b, c = map(str, input().split())
    b = int(b)  # 문자열 반복 횟수
    charlist = ""
    for j in range(len(c)):  # `c`의 모든 문자에 대해 반복
        charlist += c[j] * b  # `c[j]`를 `b`번 반복
    print(charlist)