class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:


        Max_value = max(piles)
        Min_value = 1

        while (Min_value <= Max_value):
            
            k = (Max_value + Min_value)//2
            hour = 0

            for val in piles:
                hour += math.ceil(val/k)

                if(hour > h):
                    break
            if(hour > h):
                Min_value = k + 1
            
            if(hour <= h):
                Max_value = k - 1
                last_k = k

        
        return last_k