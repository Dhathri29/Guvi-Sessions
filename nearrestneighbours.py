n,m=map(int,input().split()))
l11=input().split()
l=[]
for x in l11:
   l.append(int(x))
l.sort()
for x in range(0,len(l)):
   if(m==l[x]):
      if(x==0):
         print(l[x+1],l[x+2],l[x+3],sep=' ')
      if(x==len(l)-1):
         print(l[x-1],l[x-2],l[x-3],sep=' ')
      if(x>1 and x<len(l)-2):
         print(l[x-1],l[x+1],l[x-2],sep=' ')
      if(x==1):
         print(l[x-1],l[x+1],l[x+2],sep=' ')
