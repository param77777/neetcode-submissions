class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        mapp = {}

        for n in nums:
            mapp[n] = 1 + mapp.get(n, 0)

        for count in mapp.values():

            if count > 1:
                return True

        return False
