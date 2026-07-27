class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        storeVal = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in storeVal:
                return [storeVal[diff] + 1, i + 1]
            storeVal[numbers[i]] = i
        return []
        