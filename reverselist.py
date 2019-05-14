def Reverse(li):
   li.reverse()
   return li
n=int(input())
li=list(map(int,input().split()))
print(Reverse(li))
