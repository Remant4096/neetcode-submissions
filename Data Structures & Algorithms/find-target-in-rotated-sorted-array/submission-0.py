class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0 , len(nums) -1 
        while(l <= r):
            m = (l+r)//2

            if(nums[m] == target):
                return m

            if(nums[m] > nums[l]):
                #left side is sequential
                if(target == nums[l]):
                    return l
                if(target < nums[m] and target > nums[l]):
                    r = m - 1
                else:
                    l = m + 1

            else:
                #right side is sequantial
                if(target == nums[r]):
                    return r
                if(target > nums[m] and target < nums[r]):
                    l = m + 1
                else:
                    r = m - 1
        return -1