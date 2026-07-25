class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i in range(len(nums)):

            complement = target - nums[i]

            if complement in indices:
                return [indices[complement], i]

            indices[nums[i]] = i