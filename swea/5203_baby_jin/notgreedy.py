
def baby_gin(numbers):
    digits = [int(char) for char in numbers]
    count = 0 # 트리플 or 렁니 나온 횟수 만큼 1씩 증가 하도록 할 것.
    '''
        digits =[666776]
        만들 수 있는 모든 경우의 수
        667767 -> 667 트리플인지 런읹지 확인 
        667776
        667677
        666777
        ... 완전탐색
    '''

    '''
        같은 숫자가 3번 이상 나왔는가?
        점차 증가하는 숫자가 1번씩 나왔는가?
        [0,0,0,0,0,0,0,0,0]
        666777
        6
        arr[6]+=1
        6
        arr[6]+=1
        6
        arr[6]+=1
        7
        arr[7]+=1
        [0,0,0,0,0,3,3,0,0]
        123456
        [1,1,1,1,1,1,0,0,0]
        
    '''
def check_run(cards):
    # 7+1 7+2가 마지막 index
    for i in range(8):
        if cards[i] >= 1 and cards[i+1] >= 1 and cards[i+2] >= 1:
            return 1
        else:
            return 0


cases =['667767','123123','111456','111156']

for tc in cases:
    if baby_gin(tc):
        print("baby gin")
    else:
        print('not baby')