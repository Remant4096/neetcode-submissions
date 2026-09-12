class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s)-1

        while(r>l):

            invalid_char = False

            if not (s[l] >= 'A' and s[l] <= 'Z' or s[l] >= 'a' and s[l] <= 'z' or s[l] >= '0' and s[l]<='9'):
              invalid_char = True
              l = l + 1

            if not (s[r] >= 'A' and s[r] <= 'Z' or s[r] >= 'a' and s[r] <= 'z' or s[r] >= '0' and s[r]<='9'):
              invalid_char = True
              r = r - 1
            
            if (not invalid_char):
                if(s[l].upper() != s[r].upper()):
                            return False
                l = l+1
                r = r-1
                
        return True

        