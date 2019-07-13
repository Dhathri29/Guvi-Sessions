n,m=map(int,input().split())
l=list(map(int,input().split()))
p="no"
for i in range(len(l)):
    for j in l[i+1:]:
       if (l[i]+j)==m:
       p="yes"
       break
print(p)       
