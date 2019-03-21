class merge:
 def mergeSort(self,nlist):
      self.nlist=nlist
      print("Splitting ",nlist)
     
      if len(nlist)>1:
         mid = len(nlist)//2
         left = nlist[:mid]
         right =nlist[mid:]

         self.mergeSort(left)
         self.mergeSort(right)
         i=j=k=0         
         while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nlist[k]=left[i]
                i=i+1
                
            else:
                nlist[k]=right[j]
                j=j+1
            k=k+1

         while i < len(left):
            nlist[k]=left[i]
            i=i+1
            k=k+1
            

         while j < len(right):
            nlist[k]=right[j]
            j=j+1
            k=k+1
         
      print("Merging ",nlist)
mm=merge()
nlist=list(map(str,input().split()))
mm.mergeSort(nlist)
