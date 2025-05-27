# Category: algorithms
# Level: Hard
# Percent: 64.028534%


# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
#
#
# Example 1:
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
#
#
# Example 2:
#
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
#
#
# Constraints:
#
#
# 	n == height.length
# 	1 <= n <= 2 * 10⁴
# 	0 <= height[i] <= 10⁵
#


from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        lp, rp = 0, len(height) - 1
        leftMax, rightMax = height[lp], height[rp]
        res = 0
        while lp < rp:
            if leftMax < rightMax:
                lp += 1
                leftMax = max(leftMax, height[lp])
                res += leftMax - height[lp]
            else:
                rp -= 1
                rightMax = max(rightMax, height[rp])
                res += rightMax - height[rp]
        return res
