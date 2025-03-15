import sys
sys.stdin = open("Sample_input.txt")

T = int(input())

for tc in range (1, T+1):

    N = int(input())

    Tree_list = list(map(int,input().split()))

    max_tree= max(Tree_list)
    
    tree_flag = True

    total_day= 0

    for i in range(N):
        Tree_list[i]= max_tree-Tree_list[i]

    for j in range(N):
        while True:
            if Tree_list[j]==0:
                break
            if Tree_list[j] ==2 or Tree_list[j]==1:
                break
            if tree_flag :
                Tree_list[j]-=1
                total_day += 1
                tree_flag = not tree_flag
            else:
                Tree_list[j]-=2
                total_day += 1
                tree_flag = not tree_flag
    print(Tree_list)
    print(total_day,tree_flag)
    two_count = Tree_list.count(2)
    one_count = Tree_list.count(1)
    while two_count!=0 and one_count!=0 :
        if tree_flag:
            one_count-=1
            total_day+=1
            tree_flag = not tree_flag
        else:
            two_count-=1
            total_day+=1
            tree_flag = not tree_flag
    
    print("total_day", total_day, "left_two", two_count,"left_one", one_count, "tree_flag", tree_flag)

    # 여기서 케이스 쪼개기
    # 1이 많이남고 tree_flag가 true, 1이 많이 남고 tree_flag가 false
    # 2가 많이남고 tree_flag가 true, 2가 많이 남고 tree_flag가 false
    # 2가 1남고 tree_flag가 true, 2가 1남고 tree_flag가 false
    # 똑같으면?
    # 1이 많은 케이스 처리
    if tree_flag and one_count>two_count:
        one_count -= 1
        total_day += 1
        tree_flag = not tree_flag
             
    if one_count > two_count:
        while one_count > 0:
            # print("여기서 걸려요..",one_count)
            
            one_count-=1
            total_day+=2
    
    # 2가 더 많은 케이스 
    # tree_flag 관리
    if not tree_flag and two_count>one_count:
        two_count-=1
        total_day+=1
        tree_flag = not tree_flag

    while two_count>1:
        two_count-=2
        total_day+=3

    if tree_flag and two_count==1:
        two_count-=1
        total_day+=2
    elif not tree_flag and two_count==1:
        two_count-=1
        total_day+=1
    
    print("total_day", total_day, "left_two", two_count,"left_one", one_count, "tree_flag", tree_flag)
    # print(f'#{tc} {total_day}')
