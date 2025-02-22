# Category: algorithms
# Level: Easy
# Percent: 49.86021%


# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
#
#
# Example 1:
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
#
# Example 2:
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
#
# Example 3:
#
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
#
#
#
# Constraints:
#
#
# 	1 <= s.length <= 2 * 10⁵
# 	s consists only of printable ASCII characters.
#

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r"[^a-zA-Z|0-9]", "", s)
        for i in range(len(s)):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True
