a=int(input("input"))
b=int(input())
c=[]
d=0
for i in range(0,a):
    c.append(int(input()))
for i in range(0,b):
    d=d+c[i]
print("output",d)
