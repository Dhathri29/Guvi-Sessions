n=int(input())
arr=[int(n) for n in input().split()]
li=[]
for i in arr:
   if arr.count(i)==1:
     if i not in li:
       li.append(i)
print(*li)       
       
