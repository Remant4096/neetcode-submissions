class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans_map = {}
        ans = []
        for s in strs:
            map = {}
            for ch in s:
                map[ch] = map.get(ch,0) + 1
            map_to_key = tuple(sorted(map.items()))

            if (map_to_key in ans_map):
                ans_map[map_to_key].append(s)
            else:
                ans_map[map_to_key] = [s]

        for k,v in ans_map.items():
            ans.append(v)

        return ans