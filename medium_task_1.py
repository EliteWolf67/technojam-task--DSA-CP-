
# Online IDE - Code Editor, Compiler, Interpreter

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        result = 0
        l = 0
        r = len(height) - 1
        
        while l < r:
            area = (r-l) * min(height[l], height[r])
            result = max(result, area)
            
        if height[l] < height[r]:
            l += 1
        
        else:
            r -= 1
            
        return result
