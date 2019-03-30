def firstNonRepeating(arr,n):
  for i in range(n):
     j=0
     while(j < n):
        if(i != j and arr[i]==arr[j]):
          break
        j+=1  
     if(j == n):
        return arr[j]
  return -1
arr=list(map(int,input().split()))
n=len(arr)
print(firstNonReapiting(arr,n))
  
  
