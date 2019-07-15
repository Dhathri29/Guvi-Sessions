n=int(input())
for i in range(n):
    l.extend(list(map(int,input().split())))
print(*sorted(l))    
