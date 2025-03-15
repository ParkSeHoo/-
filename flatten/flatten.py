import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1,T+1):
    flatten_count = int(input())
    flatten_list = list(map(int, input().split()))

    # print(flatten_list)
    while flatten_count>0:
        max_val = 0
        min_val = 999999
        max_index = 0
        min_index = 0
        for i in range(len(flatten_list)):
            if max_val < flatten_list[i]:
                max_val = flatten_list[i]
                max_index = i
            if min_val > flatten_list[i]:
                min_val = flatten_list[i]
                min_index = i
        flatten_list[max_index] = max_val-1    
        flatten_list[min_index] = min_val+1    
            
        flatten_count-=1
    
    result = max(flatten_list)-min(flatten_list)
    print(f'#{tc} {result}')
