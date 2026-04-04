class Solution:
    def trap(self, height: List[int]) -> int:
        i = 1
        water = 0
        n = len(height)

        while i < n-1:
            max_left = max(height[:i])
            max_right = max(height[i+1:])
            
            water += max(0, min(max_left, max_right) - height[i])
            
            i += 1
        
        return water
