n=int(input())
l=lis(map(int,input().split()))
s1=l[1:n:2]
s2=l[0:n:2]
if(sum(s1)>=sum(s2)):
    print(sum(s1))
else:
    print(sum(s2))
