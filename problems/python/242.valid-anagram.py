# Category: algorithms
# Level: Easy
# Percent: 65.98075%


# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
#
# Example 1:
#
#
# Input: s = "anagram", t = "nagaram"
#
# Output: true
#
#
# Example 2:
#
#
# Input: s = "rat", t = "car"
#
# Output: false
#
#
#
# Constraints:
#
#
# 	1 <= s.length, t.length <= 5 * 10⁴
# 	s and t consist of lowercase English letters.
#
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
# Solution :
# binary array to count both strings
# counter dict for characters
# the two sorted strings should be equal

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        base = ord("a")
        map = [0 for _ in range(26)]
        for e in t:
            idx = ord(e) - base
            map[idx] += 1
        for e in s:
            idx = ord(e) - base
            map[idx] -= 1
        for i in map:
            if i != 0:
                return False
        return True
        return sorted(s) == sorted(t)
        return Counter(s) == Counter(t)
