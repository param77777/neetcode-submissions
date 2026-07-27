class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        count = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in count:
                return [count[diff] + 1, i + 1]
            count[numbers[i]] = i
        return []
        