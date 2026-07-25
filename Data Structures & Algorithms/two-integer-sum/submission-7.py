class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, n in enumerate(nums):

            compliment = target - n

            if compliment in indices:

                return [indices[compliment], i]

            indices[n] = i