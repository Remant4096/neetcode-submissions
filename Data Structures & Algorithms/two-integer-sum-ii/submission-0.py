class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_ptr = 0
        r_ptr = len(numbers)-1
        l = numbers[l_ptr]
        r = numbers[r_ptr]

        while(r_ptr > l_ptr):
        
            if (l + r < target):
                l_ptr = l_ptr +1
                l = numbers[l_ptr]
            
            elif (l + r > target):
                r_ptr = r_ptr-1
                r = numbers[r_ptr]

            else:
                return [l_ptr + 1,r_ptr + 1]
    
        return [-1]
            