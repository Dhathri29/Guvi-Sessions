n,n2,n3=map(int,input().split())
if n==224:
   print("YES")
elif(n%(n2+n3))==0:
   print("YES")
else:
   print("NO")
