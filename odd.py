num=input()
n1=[num[i] for i in range(len(num)) if i%2==0]
n4=[num[i] for i in range(len(num)) if i%2!=0]
for j in range(len(num)//2):
  print(n4[j]+n1[j],end="")
