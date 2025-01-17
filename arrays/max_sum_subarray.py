"""

Given an integer array, find the maximum sum among all its subarrays.

Input : [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The maximum sum subarray is [4, -1, 2, 1]

Input : [-7, -3, -2, -4]
Output: -2
Explanation: The maximum sum subarray is [-2]

Input : [-2, 2, -1, 2, 1, 6, -10, 6, 4, -8]
Output: 10
Explanation: The maximum sum subarray is [2, -1, 2, 1, 6] or [6, 4] or [2, -1, 2, 1, 6, -10, 6, 4]

https://www.techiedelight.com/maximum-subarray-problem-kadanes-algorithm/
"""

from typing import List


class Solution:
    def findMaxSubarraySum(self, nums: List[int]) -> int:
        max = nums[0]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                sub_array_sum = sum(nums[i:j])
                if sub_array_sum > max:
                    max = sub_array_sum
        return max
