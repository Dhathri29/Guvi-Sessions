n=int(input())
l=[]
for i in range(n):
    l.extend(list(map(int,input().split())))
print(*sorted(l))    
