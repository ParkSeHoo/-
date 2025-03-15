# a = "start"
# b= []
# for i in a:
#     b.append(i)

# alpahbet = [-1]*26


# 입력받은 문자열을 대문자로 변환
sample = input().upper()

# A부터 Z까지의 알파벳을 리스트로 생성
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 알파벳 빈도수를 저장할 리스트 초기화
counts = [-1] * 26
# 문자별 빈도수 계산
# for char in sample:
#     index = alphabet.index(char)
#     counts[index] += 1

for i in range(len(sample)):
    index = alphabet.index(sample[i:i+1])
    if counts[index] == -1:
        counts[index] = i
    else:
        continue
# print(sample)
# print(counts)
for count in counts:
    print(count ,end=" ")
# 최빈값과 중복 여부 확인
