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


from typing import List, Tuple


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        def anagram_hash(s: str) -> Tuple[int, ...]:
            init_hash = [0 for _ in range(26)]
            base = ord("a")
            for e in s:
                init_hash[ord(e) - base] += 1
            return tuple(init_hash)

        for s in strs:
            hash = anagram_hash(s)
            if hash in map:
                map[hash].append(s)
            else:
                map[hash] = [s]
        return list(map.values())
