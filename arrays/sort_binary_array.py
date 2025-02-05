"""

Given a binary array, in-place sort it in linear time and constant space. The output should contain all zeroes, followed by all ones.

Input : [1, 0, 1, 0, 1, 0, 0, 1]
Output: [0, 0, 0, 0, 1, 1, 1, 1]

Input : [1, 1]
Output: [1, 1]
[1, 0, 1, 0, 1, 0, 0, 1]

https://www.techiedelight.com/sort-binary-array-linear-time/
"""

from typing import List


class Solution:
    def sortArray(self, nums: List[int]):
        ones = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                nums[i] = 0
                ones += 1
        for i in range(ones):
            nums[len(nums) - i - 1] = 1
        return nums
