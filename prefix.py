m=int(input())
l=[]
for i in range(0,m):
    s=input()
    l.append(s)
prefix=[]
for i in zip(*l):
    if i.count(i[0])==len(i):
       prefix.append(i[0])
    else:
       break
prefixx=''.join(prefix)    
print(prefixx)
    
