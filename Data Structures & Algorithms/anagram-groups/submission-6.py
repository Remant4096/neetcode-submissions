class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans_map = {}
        ans = []
        for s in strs:
            map_to_key = [0]*26
            for ch in s:
               map_to_key[ord(ch)-ord('a')] += 1

            map_to_key = tuple(map_to_key)

            if (map_to_key in ans_map):
                ans_map[map_to_key].append(s)
            else:
                ans_map[map_to_key] = [s]

        for k,v in ans_map.items():
            ans.append(v)

        return ans