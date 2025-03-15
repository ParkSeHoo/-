#반례  2 0 
#      0 0
#     A: 2
#       3 0
#       -1 1 0
#     A:3
# 하나씩 뽑으면서 케이스를 구하자
def sumofnum(n_list,K,start,temp_list):
    global num_of_case

    # 현재 리스트의 합이 정확히 K이면 경우의 수 증가
    
    if sum(temp_list)==K and temp_list:
        num_of_case+=1

    
    for i in range(start, len(n_list)):
        temp_list.append(n_list[i])
        # print(temp_list)
        sumofnum(n_list, K, i+1, temp_list)
        temp_list.pop()
        
    return

    # N 은 자연수의 갯수 
    # K 는 넘어야 하는 집합의 합 
N, K = map(int,input().split())
# 자연수 모음
n_list = list(map(int,input().split()))
#경우의 수 
num_of_case = 0
start=0
temp_list=[]
n_list.sort()
sumofnum(n_list, K, start, temp_list)
print(num_of_case)
