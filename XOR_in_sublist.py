a,b=map(int,input().split())
l1=[]
lis=list(map(int,input().split()))
for i in range(b):
   u,v=map(int,input().split())
   y=0
   for i in range(u-1,v):
       y=y^lis[i]
   l1.append(y)
print(*l1,sep="\n")   
