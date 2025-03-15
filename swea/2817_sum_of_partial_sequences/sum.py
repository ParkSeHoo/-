import sys
sys.stdin = open("sample_input.txt")

T = int(input())

# 하나씩 뽑으면서 케이스를 구하자
def sumofnum(n_list,K,start,temp_list):
    global num_of_case
    
    # print(temp_list)

    if sum(temp_list)==K:
        return 1

    count= 0
    for i in range(start, len(n_list)):
        temp_list.append(n_list[i])
        count += sumofnum(n_list,K,i+1,temp_list)
        temp_list.pop()
    
    return count

for tc in range(1,T+1):
    # N 은 자연수의 갯수 
    # K 는 넘어야 하는 집합의 합 
    N, K = map(int,input().split())
    # 자연수 모음
    n_list = list(map(int,input().split()))
    #경우의 수 
    num_of_case = 0
    start=0
    temp_list=[]
    num_of_case = sumofnum(n_list, K, start, temp_list)



    print(f'#{tc} {num_of_case}')