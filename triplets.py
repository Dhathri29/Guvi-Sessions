s=int(input())
m=input().split()
d=0
for i in range(0,len(m)):
    m.insert(i,int(m[i]))
    m.remove(m[i+1])
for i in range(0,len(m)-2):
   for j in range(1,len(m)-1):
      for k in range(2,len(m)):
         if(m[i]<m[j]<m[k]])and(i<j<k):
            d=d+1
print(d)            
            
            
