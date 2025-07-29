# Category: algorithms
# Level: Medium
# Percent: 70.13556%


# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
#
# Example 1:
#
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
#
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Explanation:
#
#
# 	There is no string in strs that can be rearranged to form "bat".
# 	The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# 	The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
#
#
#
# Example 2:
#
#
# Input: strs = [""]
#
# Output: [[""]]
#
#
# Example 3:
#
#
# Input: strs = ["a"]
#
# Output: [["a"]]
#
#
#
# Constraints:
#
#
# 	1 <= strs.length <= 10⁴
# 	0 <= strs[i].length <= 100
# 	strs[i] consists of lowercase English letters.
#


from collections import defaultdict
from typing import List, Tuple


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def hash_string(s: str) -> Tuple[int, ...]:
            h = [0 for _ in range(26)]
            for c in s:
                h[ord(c) - ord("a")] += 1
            return tuple(h)

        groups = defaultdict(list)
        for s in strs:
            h = hash_string(s)
            groups[h].append(s)

        return list(groups.values())
