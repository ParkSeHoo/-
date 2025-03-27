music = list(map(int, input().split()))

asc = True
desc = True

for i in range(7):
    if music[i] < music[i + 1]:
        desc = False
    elif music[i] > music[i + 1]:
        asc = False

if asc:
    print("ascending")
elif desc:
    print("descending")
else:
    print("mixed")
