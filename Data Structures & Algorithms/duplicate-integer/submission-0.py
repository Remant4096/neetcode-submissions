class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for e in nums:  
            if e in hash_set:
                return True

            else:
                hash_set.add(e)
        
        return False