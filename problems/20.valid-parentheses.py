# Category: algorithms
# Level: Easy
# Percent: 41.82534%


# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# 	Open brackets must be closed by the same type of brackets.
# 	Open brackets must be closed in the correct order.
# 	Every close bracket has a corresponding open bracket of the same type.
#
#
#
# Example 1:
#
#
# Input: s = "()"
#
# Output: true
#
#
# Example 2:
#
#
# Input: s = "()[]{}"
#
# Output: true
#
#
# Example 3:
#
#
# Input: s = "(]"
#
# Output: false
#
#
# Example 4:
#
#
# Input: s = "([])"
#
# Output: true
#
#
#
# Constraints:
#
#
# 	1 <= s.length <= 10⁴
# 	s consists of parentheses only '()[]{}'.
#


class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        open = ("(", "{", "[")
        stack = []
        for c in s:
            if c in open:
                stack.append(c)
            else:
                if not stack:
                    return False
                e = stack.pop()
                if mapping[e] != c:
                    return False
        return True if not stack else False
