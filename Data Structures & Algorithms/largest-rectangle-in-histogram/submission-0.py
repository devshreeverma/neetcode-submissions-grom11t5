class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []              # will store indices
        max_area = 0
        heights.append(0)      # sentinel to flush stack

        for i in range(len(heights)):

            # If current bar is smaller, calculate area for taller bars
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]   # height of rectangle

                if not stack:
                    width = i              # rectangle extends to index 0
                else:
                    width = i - stack[-1] - 1

                area = h * width
                max_area = max(max_area, area)

            stack.append(i)

        return max_area
