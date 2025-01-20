sample = int(input())
sample_list=[sample]
num=0
# flag = True
# while flag:
#     sample_list.append((sample%10)*10+sample%10+sample//10)
#     print("nn")
#     num+=1
#     if sample_list[-1]==sample_list[0]:
#         flag = False
for i in range(1000):
    sample_list.append((sample_list[i]%10)*10+(sample_list[i]%10+sample_list[i]//10)%10)
    num+=1
    if sample_list[-1]==sample_list[0]:
       break
# print(sample_list)    
print(num)