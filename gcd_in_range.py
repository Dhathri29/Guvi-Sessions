import math
lis1=[]
a,b=map(int,input().split())
lis=list(map(int,input().split()))
for i in range(0,b):
    c,d=map(int,input().split())
    lis1.append([c,d])
for i in lis1:
    c=i[0]-1
    d=i[1]-1
    print(math.gcd(lis[c],lis[d]))
