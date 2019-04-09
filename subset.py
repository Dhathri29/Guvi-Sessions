a,b=map(int,input().split())
a1=list(map(int,input().split()))
b1=list(map(int,input().split()))
flag=0
if(set(b1).issubset(set(a1))):
   flag=1
if (flag) :
   print("YES")
else:
   print("NO")
