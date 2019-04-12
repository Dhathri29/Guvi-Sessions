n=int(input())
li=list(map(int,input().split()))
left=[]
right=[]
for i in range(0,n-1):
    left=li[:i+1]
    right=li[i+1:]
    if sum(left)//len(left) == sum(right)//len(right):
        print("yes")
    else:
        print("no")
