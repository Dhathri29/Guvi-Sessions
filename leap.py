def year(n):
   if (n%4==0) and (n%100!=0) or (n%400==0):
      print("Yes")
   else:
      print("No")
      
year(2013)
year(2048)

      
