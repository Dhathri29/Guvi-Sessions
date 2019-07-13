n,m=map(int,input().split())
tem=[]
x=0
for i in range(n):
    tem.append(list(map(int,input().split()))
for i in range(n):
    for j in range(m-1):
        for k in range(j+1,m+1)
            if tem[i][j:k]==[1]*len(tem[i][j:k]):
              if all(tem[p+i][j:k][j:k]==[1]*len(tem[p+i][j:k]) for p in range(len(tem[i][j:k])-1)):
                 if len(tem[p][j:k])>x:
                    x=len(tem[i][j:k])
if len(tem)==1 and len(tem[0])==1 and tem[0][0]==1:
   print(1)
for m in range(x):
   print(*[1]*x)
                    
