class Solution:
    def hammingWeight(self, n: int) -> int:
        digit = 0
        x = 1
        for i in range(31):
            if(n & x):
                digit += 1
        
            x = x << 1
        return digit
