def reduce(n,k):
   if k<=0:
     return n
   if n==0:
     return 10
   p=reduce(n//10,k)*10+n%10
   p1=reduce(n//10,k-1)
   if p<p1:
     return p
   else: 
     return p1
n,k=input().split()
n,k=int(n),int(k)
print(reduce(n,k))
     
