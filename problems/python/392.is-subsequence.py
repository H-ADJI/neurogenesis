# Category: algorithms
# Level: Easy
# Percent: 48.158325%


# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
#
#
# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
#
#
# Constraints:
#
#
# 	0 <= s.length <= 100
# 	0 <= t.length <= 10⁴
# 	s and t consist only of lowercase English letters.
#
#
#
# Solution:
# two pointers in the same direction
# we go through t chars until we find them in s
# if found we increment a counter
# and we increment the pointer of t since we consumed a char


class Solution(object):
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # pointer for s
        for char in t:
            if i < len(s) and s[i] == char:
                i += 1
        return i == len(s)


# Follow up: Suppose there are lots of incoming s, say s₁, s₂, ..., sk where k >= 10⁹, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
# cache the indexes of each char in t in an char -> list[indeces in  t]
# each string we look if chars from s exist in t and are not consumed yet
# import bisect
# from collections import defaultdict


# class SubsequenceChecker:
#     def __init__(self, t: str):
#         self.char_indices = defaultdict(list)
#         for index, char in enumerate(t):
#             self.char_indices[char].append(index)
#
# Input: s = "abc", t = "ahbhgdc"
# {
# 'a': [0]
# 'h': [1,3]
# 'b': [2]
# 'g': [4]
# 'd': [5]
# 'c': [6]
# }
# def isSubsequence(self, s: str) -> bool:
#     prev_index = -1
#     for char in s:
#         if char not in self.char_indices:
#             return False
#         indices = self.char_indices[char]
#         pos = bisect.bisect_right(indices, prev_index)
#         if pos == len(indices):
#             return False
#         prev_index = indices[pos]
#     return True
