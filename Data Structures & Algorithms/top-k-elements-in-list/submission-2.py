class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)

        freq = [[] for _ in range(len(nums) + 1)]

        for v, c in count.items():
            freq[c].append(v)

        res = []

        for i in range(len(freq) - 1, -1, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res

        
