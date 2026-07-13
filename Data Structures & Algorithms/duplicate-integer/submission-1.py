class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new1 = set()
        for i in nums:
            if i in new1:
                return True
            new1.add(i)
        else:
            return False