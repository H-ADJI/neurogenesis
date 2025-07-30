# Category: algorithms
# Level: Medium
# Percent: 36.79358%


# Given a string s, find the length of the longest substring without duplicate characters.
#
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
#
#
# Constraints:
#
#
# 	0 <= s.length <= 5 * 10⁴
# 	s consists of English letters, digits, symbols and spaces.
#


from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left, right = 0, 1
        length = 1
        counter = defaultdict(int)
        counter[s[0]] += 1
        while right < len(s):
            counter[s[right]] += 1
            while counter[s[right]] > 1:
                counter[s[left]] -= 1
                left += 1

            length = max(length, right - left + 1)
            right += 1
        return length
