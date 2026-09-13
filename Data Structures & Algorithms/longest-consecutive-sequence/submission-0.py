class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set()

        for n in nums:
            hash_set.add(n)
        max_sequence = 0

        for n in nums:
            
            if(n in hash_set):
                sequence = 0

                temp = n
                while(True):
                    if(temp in hash_set):
                        sequence += 1
                        hash_set.remove(temp)
                    else:
                        break
                    temp -= 1
                        
                temp = n+1
                while(True):
                    if(temp in hash_set):
                        sequence += 1
                        hash_set.remove(temp)
                    else:
                        break
                    temp += 1
                    
                max_sequence = max(sequence,max_sequence)

        return max_sequence