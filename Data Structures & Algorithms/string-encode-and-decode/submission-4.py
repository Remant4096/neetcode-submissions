class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded_string = ""

        for s in strs:
            encoded_string  =  encoded_string + s + ":x,a"
        return encoded_string

    def decode(self, s: str) -> list[str]:
        decoded_string = []
        temp = ""
        i = 0
        while(i<len(s)):
        
            if(s[i] == ':' and i+3<len(s) and s[i+1] == "x" and s[i+2] == "," and s[i+3] == "a"):
                
                decoded_string.append(temp)
                temp = ""
                i = i + 4
            else:
                temp += s[i]
                i = i + 1

            
        return decoded_string