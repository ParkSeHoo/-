'''
베이진 게임란게 뭐냐?
6개의 숫자를 가지고 triple 혹은 run이 각각 2번 나오거나 , 혹은 한번씩 번갈아 나오면 베이비진
triple -> 동일한 숫자가 6번
run -> 숫자 3개가 차례로 증가 하는 형태

0~9중에서 6개를 중복 포함 해서 뽑는다
123123 -> run2번
667767 -> 트리플 2번
111456 -> 런, 트리플 1번씩 베이비 진
'''

# 함수를 통해서 얻고자하는 바가 무엇인가?
# 어떤 지엽적인 문제를 핵뎔해 나가면서 큰 문제를 모두 해결 가능한가?
# 어떤 아주 특이한 케이스 하나만을 위한 if문을 작성 하는데에는 신중한 고민 끝에 결론을 내야한다. (검증)
def baby_gin(numbers):
    '''
    numbers : 정수 6개가 문자열로 주어짐
    숫자 3개씩 끊어서 트리플인지 보기 런인지 보기 2번 나오면 베이비진

    일단 정렬을 해  -> 트리플 체크

    '''
    # if run run
    # if 트리플 런
    # if 런 트리플
    # if 트리플 트리플
    # 이렇게 만들거면 왜 알고리즘 하냐;;

    digits = [int(char) for char in numbers]


    count = 0 # 트리플 or 렁니 나온 횟수 만큼 1씩 증가 하도록 할 것.
    # 조사는 총 몇 번 해야 할까?
    for _ in range(2): # 이번 회차에 숫자 3개 끊어서 트리플인지 런인지 볼거임
        digits.sort()
        # if triple?
        #     count+=1
        # 트리플인지 먼저 확인
        # 앞에서부터 연속된 3개가 같은 숫자인지 확인
        for i in range(len(digits)-2): #0 1 2 3
            if digits[i]==digits[i+1] ==digits[i+2]:
                triple_val = digits[i]
                digits.remove(triple_val)
                digits.remove(triple_val)
                digits.remove(triple_val)
                # digits.remove(i) # 이렇게 직접적으로 digits 제거 해버리면 곤란할지도..?
                count += 1
                break


        # if run?
        #     count+=1
        for i in range(len(digits)-2):
            # 내 값보다 1큰 값과 내 값보다 2큰 값이 배열에 있나확인
            # if digits[i]== digits[i+1]-1
            if digits[i]+1 in digits and digits[i]+2 in digits:
                run_val = digits[i]
                digits.remove(run_val)
                digits.remove(run_val+1)
                digits.remove(run_val+2)
                count += 1
                break

    if count == 2:
        return True


cases =['667767','123123','111456','111156']

for tc in cases:
    if baby_gin(tc):
        print("baby gin")
    else:
        print('not baby')