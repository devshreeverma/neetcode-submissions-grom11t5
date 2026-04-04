class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val=-1;
        i=len(arr)-1;
        myarr=[]
        while i>=0:
            myarr.append(max_val);
            if arr[i]>max_val:
                max_val=arr[i]
            i-=1

        myarr.reverse()
        return myarr