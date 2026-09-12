class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans_map = {}
        for s in strs:
            count = [0]*26
            for ch in s:
                count[ord(ch) -ord('a')] += 1
            tuple_key = tuple(count)

            if(tuple_key in ans_map):
                ans_map[tuple_key].append(s)
            else:
                ans_map[tuple_key] = [s]

        ans = list(ans_map.values())

        return ans