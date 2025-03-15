import sys
sys.stdin = open("sample_input.txt")

T=10

for tc in range(1,T+1):
    # 건물 높이
    N = int(input())
    # 아파트 리스트
    apt_n = list(map(int,input().split()))
    # 조망가능한 총 층수
    sum_view = 0
    # 층 수가 있는 것만 순회 
    for i in range(2,N-2):
        # 비교 대상 리스트
        temp_list = [apt_n[i-2], apt_n[i-1], apt_n[i+1],apt_n[i+2]] 
        # 비교
        if (apt_n[i]-max(temp_list))>0:
            sum_view += apt_n[i]-max(temp_list)
    
    print(f'#{tc} {sum_view}')