num = int(input())


for i in range(num):
    score=0
    ox = input()
    plus=0
    for j in range(len(ox)):
        if ox[j:j+1]=='O':
            plus+=1
            score+=plus
        elif ox[j:j+1]=='X':
            plus=0
    
    print(score)