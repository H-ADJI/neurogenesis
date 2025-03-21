# Category: algorithms
# Level: Medium
# Percent: 63.91819%


# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#
#
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Constraints:
#
#
# 	1 <= nums.length <= 10⁵
# 	-10⁴ <= nums[i] <= 10⁴
# 	k is in the range [1, the number of unique elements in the array].
# 	It is guaranteed that the answer is unique.
#
#
#
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums))]
        counts = Counter(nums)
        for key, v in counts.items():
            buckets[v - 1].append(key)
        result = []
        for bucket in buckets[::-1]:
            for e in bucket:
                result.append(e)
                if len(result) == k:
                    return result
        return result
