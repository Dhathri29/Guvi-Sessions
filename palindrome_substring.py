n=input()
x=[]
x1=""
if(n==n[::-1]):
    x.append(0)
for i in range(0,len(n)-1):
    for j in range(i+1,len(n)):
         x1=n[i:j+1]
         if x1==x1[::-1]:
            x.append(len(n)-len(x1))
print(min(x))  
   
         
   
