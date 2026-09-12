class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) -1    
        max_water_level = 0

        while(r > l):
            water_level = min(heights[l],heights[r])*(r-l)
            if (water_level > max_water_level):
                max_water_level = water_level
            
            if(heights[l] > heights[r]):
                r = r -1
            else:
                l = l + 1        
        return max_water_level
