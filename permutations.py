from itertools import permutations
l=list(input())
p1 = permutations(l)
b=[]
for i in list(p1):
    s=''
    for j in i:
       s+=j
    if s not in b:
       b.append(s)
       print(s)
