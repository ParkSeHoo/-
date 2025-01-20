a = int(input())
b = int(input())
c = int(input())

d = a*b*c

e = str(d)

f = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
for i in range(len(e)):
    f[e[i:i+1]]+=1

for val in f.values():
    print(val)
# a = "hello"
# print(a[0:1])
# print(len(a))
# for i in range(len(a)):
#     print(a[i:i+1])