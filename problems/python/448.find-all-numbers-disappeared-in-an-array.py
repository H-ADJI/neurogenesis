# Category: algorithms
# Level: Easy
# Percent: 61.8083%


# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
#
#
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Input: nums = [4,3,-2,-7,8,2,3,1]
# Output: [5,6]
# Example 2:
# Input: nums = [1,1]
# Output: [2]
#
#
# Constraints:
#
#
# 	n == nums.length
# 	1 <= n <= 10⁵
# 	1 <= nums[i] <= n
#
#
#
# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res
