# Category: algorithms
# Level: Medium
# Percent: 57.009506%


# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
#
# Return the length of the longest substring containing the same letter you can get after performing the above operations.
#
#
# Example 1:
#
# Input: s = "AACBBDCBE", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
#
#
# Example 2:
#
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
#
#
# Constraints:
#
#
# 	1 <= s.length <= 10⁵
# 	s consists of only uppercase English letters.
# 	0 <= k <= s.length
#


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 1
        left = right = 0
        replacement = k
        last_idx = {}
        while right < len(s):
            last_idx[s[left]] = last_idx.get(s[left]) or left
            if s[left] == s[right]:
                right += 1
            elif replacement > 0:
                replacement -= 1
                right += 1
            else:
                pass
            longest = max(longest, right - left + 1)
        return longest
