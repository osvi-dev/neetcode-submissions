class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rest_numbers = {}

        for i in range(len(nums)):
            if nums[i] in rest_numbers:
                return [rest_numbers[nums[i]], i]
            else:
                rest_numbers[target-nums[i]] = i