x1=input()
z1=x1.split()
n=len(z1)
b=''
for a in range(0,n):
    y=list(reversed(z1[a]))
    b=b+''.join(y)+' '
print(b)    
