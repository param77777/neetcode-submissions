class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                summ = n + nums[l] + nums[r]
                if summ == 0:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
                elif summ < 0:
                    l += 1
                else:
                    r -= 1
        return res


                

        
        