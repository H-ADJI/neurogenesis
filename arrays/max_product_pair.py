"""

Given an integer array, find a pair with the maximum product in it.

Each input can have multiple solutions. The output should match with either one of them.

Input : [-10, -3, 5, 6, -2]
Output: (-10, -3) or (-3, -10) or (5, 6) or (6, 5)

Input : [-4, 3, 2, 7, -5]
Output: (3, 7) or (7, 3)

If no pair exists, the solution should return an empty tuple.

Input : [1]
Output: ()

https://www.techiedelight.com/find-maximum-product-two-integers-array/
"""

from typing import Tuple, List


class Solution:
    def findPair(self, nums: List[int]) -> Tuple[int, int]:
        positive1 = positive2 = negative1 = negative2 = 0
        if len(nums) < 2:
            return tuple()
        if len(nums) == 2:
            return nums[0], nums[1]
        for e in nums:
            if e > 0:
                if e > positive1:
                    positive2 = positive1
                    positive1 = e
                elif e > positive2:
                    positive2 = e
            else:
                if e < negative1:
                    negative2 = negative1
                    negative1 = e
                elif e < negative2:
                    negative2 = e
        if negative2 * negative1 > positive2 * positive1:
            return negative1, negative2
        return positive1, positive2
