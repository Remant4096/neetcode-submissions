class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        ch_map = {}

        for n in nums:
            ch_map[n] = ch_map.get(n,0) +1
       
        f_map = [[] for _ in range(len(nums))]

        for ks,v in ch_map.items():
            f_map[v-1].append(ks)


        
        i = len(f_map)-1

        ans = []
        for _ in range(len(f_map)):

            if len(f_map[i]) > 0:
                for items in f_map[i]:
                    if len(ans) == k:
                        return ans
                    ans.append(items)
            i = i -1 

        return ans