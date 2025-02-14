# Category: algorithms
# Level: Easy
# Percent: 47.771072%


# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
#
#
# Example 1:
#
# Input: nums = [1,2,3,1], k = 3
# Output: true
#
#
# Example 2:
#
# Input: nums = [1,0,1,1], k = 1
# Output: true
#
#
# Example 3:
#
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
#
#
#
# Constraints:
#
#
# 	1 <= nums.length <= 10⁵
# 	-10⁹ <= nums[i] <= 10⁹
# 	0 <= k <= 10⁵
#


from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}
        for i, e in enumerate(nums):
            if e in map:
                if abs(map[e] - i) <= k:
                    return True
            map[e] = i
        return False
