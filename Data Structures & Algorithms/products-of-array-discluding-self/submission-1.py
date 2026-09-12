class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [0]*len(nums)
        suffix_product = [0]*len(nums)

        prefix_product[0] = nums[0]
        suffix_product[len(nums)-1]= nums[len(nums) -1]

        for i in range(1,len(nums)):
            prefix_product[i] = prefix_product[i-1]*nums[i]

        for i in range(len(nums)-2,-1,-1):
            suffix_product[i] = suffix_product[i+1]*nums[i]

        
        output = [0]*len(nums)
        output[0] = suffix_product[1]
        output[len(nums)-1] = prefix_product[len(nums)-2]

        for i in range(1,len(nums)-1):
            output[i] = prefix_product[i-1]*suffix_product[i+1]

        return output