class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = nums[0]
        l , r = 0, len(nums) -1

        while(l<=r):
            m = (l+r)//2

            if(nums[m] <= nums[r]):
                r = m - 1
            else:
                l = m + 1
            min_val = min(nums[m],min_val)

        return min_val

