class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dictt = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in dictt:
                return [dictt[diff], i]
            dictt[n] = i
        return []
