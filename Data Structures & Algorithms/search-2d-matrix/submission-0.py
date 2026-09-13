class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        row = len(matrix)
        col = len(matrix[0])
        l = 0 
        r = row*col - 1
        
        while(l<=r):
            m = (l+r)//2
            val = matrix[m//col][m%col]

            if(val > target):
                r = m - 1

            elif(val < target):
                l = m + 1
            else:
                return True
                
        return False 
    
    
    
    
