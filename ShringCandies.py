n=int(input())
l=list(map(int,input().split()))
c1=[1]*n
for i in range(n-1):
   if(l[i]<l[i+1] and c1[i]>=c1[i+1]):
      c1[i+1]=c1[i]+1
for i in range(n-1,0,-1):
   if l[i]<l[i-1] and c1[i]>=c1[i-1]:
       c1[i-1]=c1[i]+1
print(sum(c1))       
