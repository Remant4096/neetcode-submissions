class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if(len(s) == 0):
            return 0
        
        l  = 0
        map = {}
        map[s[l]] = 0
        max_length = 1

        for r in range(1,len(s)):

            if(s[r] in map and map[s[r]] >= l):

                Length = r - l
                max_length = max(max_length,Length)
                l = map[s[r]] + 1
                map[s[r]] = r

            else:
               
                if(r != len(s) -1):
                    map[s[r]] = r
                else:
                    Length = r - l + 1
                    max_length = max(max_length,Length)
                
        return max_length