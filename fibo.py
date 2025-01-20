# 피보나치 수열 만들기 
# fn = fn-1 + fn-2 
# 어떻게 풀었드라...
num = int(input()) 
# def fibo (n):
#     if n ==0:
#         return 0
#     if n ==1:
#         return 1
#     return fibo(n-1)+fibo(n-2)

# print(fibo(num))

sample_list=[0,1,1,2,3]
if num<5:
    print(sample_list[num])
else:
    for i in range(num-4):
        sample_list.append(sample_list[-1]+sample_list[-2])
    print(sample_list[-1])