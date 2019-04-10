string=input()
string=string.casefold()
revstr=reversed(string)
if list(string) == list(revstr):
   print("YES")
else:
   print("NO")
   
