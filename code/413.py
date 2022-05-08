from typing import List

"""
413. Arithmetic Slices
https://leetcode.com/problems/arithmetic-slices/
One-dimension dynamic programming
"""

# Zhongyi Lu 2022-05-05


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # if length < 3, impossible
        if len(nums) < 3:
            return 0

        # dp[i] is the number of arithmetic slices ending with index i
        dp = [0] * len(nums)

        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                # All arithmetic slices ending with index i-1 can be still arithmetic with nums[i]
                dp[i] = dp[i-1] + 1

        return sum(dp)
