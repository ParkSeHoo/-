# sample = "Mississipi"
sample=input()
sample = sample.upper()
e={}

for i in range(len(sample)):
   e[sample[i]]=0 

for j in sample:
   for k in e.keys():
      if j==k:
         e[j]+=1

e1 =list(e)
e2 = list(e.values())

check = max(e2)
result=""
ch =0
for num in e2:
#    print(num)
   if num==check:
      ch+=1
   if ch==2:
      result="?"
      check=0
      break
# print(result)
# print(ch)
# print(check)

for key in e1:
   if e[key]==check:
      result=key
      break
print(result)


#chatgpt로 최적화 해보았다
# 대문자로 변환 및 초기화
sample = input().upper()

# 등장 횟수를 기록할 딕셔너리 생성
e = {}

# 문자열 한 번 순회하며 등장 횟수 기록
for char in sample:
    if char in e:
        e[char] += 1
    else:
        e[char] = 1

# 등장 횟수 중 가장 큰 값 찾기
check = max(e.values())
result = ""

# 최빈값 확인 및 중복 검사
most_frequent = [key for key, value in e.items() if value == check]

# 결과 처리
if len(most_frequent) > 1:
    result = "?"
else:
    result = most_frequent[0]

print(result)