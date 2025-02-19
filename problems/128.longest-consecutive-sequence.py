# Category: algorithms
# Level: Medium
# Percent: 47.35687%


# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
#
#
# Example 1:
#
# Input: nums = [100,4,200,1,3,2]
# Input: map = {100 : -1, 4: -1, 200:-1, 1:-1, 3:-1, 2:-1]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
#
#
# Example 2:
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#
#
# Example 3:
#
# Input: nums = [1,0,1,2]
# Output: 3
#
#
#
# Constraints:
#
#
# 	0 <= nums.length <= 10⁵
# 	-10⁹ <= nums[i] <= 10⁹
#


from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        current_max = 0
        for e in s:
            if e - 1 not in s:
                k = 1
                while e + k in s:
                    k += 1
                current_max = max(current_max, k)

        return current_max
