class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0: return False

        array_numbers = {}

        for i in nums:
            if i in array_numbers: return True
            else: array_numbers[i] = 0

        return False