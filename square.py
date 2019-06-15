a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
g,h=map(int,input().split())
te1=d-b
te2=e-g
te3=e-c
te4=g-a
if te1==te2==te3==te4:
  print("yes")
else:
  print("no")
