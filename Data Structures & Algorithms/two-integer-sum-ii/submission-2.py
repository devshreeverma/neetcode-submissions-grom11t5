class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans=[]
        
        for i in range(len(numbers)):
            x = numbers[i]
            
            for j in range(len(numbers)):
                
                if i != j and (numbers[j] + x) == target:
                    ans.append(i+1)
                    ans.append(j+1)
                    ans.sort()
                    return ans
