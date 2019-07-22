a,b=map(int,input().split())
for i in range(a,b+1):
    sum=0;
    temp=i
    while temp>0:
        digit=temp % 10
        sum +=digit ** 3
        temp //=10
    if num ==sum:
        print(num)
