class Solution:

    def encode(self, strs: List[str]) -> str:
        output_string = ""
        for i in range(len(strs)):
            length = str(len(strs[i]))
            output_string =  output_string + length + "#" + strs[i]
        
        return output_string

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0 
        while(i<len(s)):

            starting_i = i
            while(s[i] != "#"):
                i+=1
            length = int(s[starting_i:i])

            ans.append(s[i+1:i+length+1])

            i = i + length + 1
        return ans