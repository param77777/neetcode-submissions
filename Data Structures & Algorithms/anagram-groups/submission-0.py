from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        mapp = defaultdict(list)
        result = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            mapp[sorted_s].append(s)
        
        for val in mapp.values():
            result.append(val)

        return result
        