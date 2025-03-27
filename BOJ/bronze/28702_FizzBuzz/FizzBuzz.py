target=0
for j in range(3):
    number = input()
    if target == 0:
        try:
            number = int(number)
            if j == 0:
                target = number+3
            if j == 1:
                target = number + 2
            if j == 2:
                target = number + 1
        except:
            pass
# 조건 순서가 중요함!
if target % 15 == 0:
    print('FizzBuzz')
elif target % 5 == 0:
    print('Buzz')
elif target % 3 == 0:
    print('Fizz')
else:
    print(target)