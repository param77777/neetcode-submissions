from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        store = defaultdict(list)

        for s in strs:
            sorted_s = tuple(sorted(s))
            store[sorted_s].append(s)
        
        res = []

        for values in store.values():
            res.append(values)

        return res




        