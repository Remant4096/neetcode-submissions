class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        j = 0
        while(j<=n):
            temp = 0
            x = 1
            for i in range(31):
                if(x & j):
                    temp += 1
                x = x<<1
            
            ans.append(temp)
            j = j + 1
        
        return ans
                
