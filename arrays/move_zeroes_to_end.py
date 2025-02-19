"""

Given an integer array, in-place move all zeros present in it to the end. The solution should maintain the relative order of items in the array and should not use constant space.

Input : [6, 0, 8, 2, 3, 0, 4, 0, 1]
Output: [6, 8, 2, 3, 4, 1, 0, 0, 0]

https://www.techiedelight.com/move-zeros-present-array-end/
"""

from typing import List


class Solution:
    def rearrange(self, nums: List[int]):
        new = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                new.append(nums[i])
        for i in range(count):
            new.append(0)
        return new
