def Repeat(x):
    _size=len(x)
    repeated=[]
    for i in range(_size):
        k=i+1
        for j in range(k,_size):
            if x[i]==x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
    repeated.sort()
    print(repeated)
n=int(input())
list1=list(map(int,input().split()))
print (Repeat(list1))
   
