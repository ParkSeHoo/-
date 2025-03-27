x, y = map(int,input().split())
day_list = [31,28,31,30,31,30,31,31,30,31,30,31]
day_dict = {
    1: 'MON',
    2: 'TUE',
    3: 'WED',
    4: 'THU',
    5: 'FRI',
    6: 'SAT',
    0: 'SUN'
}

if x == 1:
    print(day_dict[y % 7])
else:
    for i in range(x-1):
        y += day_list[i]
    # print(y)
    print(day_dict[y % 7])
