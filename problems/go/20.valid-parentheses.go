// Category: algorithms
// Level: Easy
// Percent: 42.22436%
// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
//
// An input string is valid if:
//
//
// 	Open brackets must be closed by the same type of brackets.
// 	Open brackets must be closed in the correct order.
// 	Every close bracket has a corresponding open bracket of the same type.
//
//
//
// Example 1:
//
//
// Input: s = "()"
//
// Output: true
//
//
// Example 2:
//
//
// Input: s = "()[]{}"
//
// Output: true
//
//
// Example 3:
//
//
// Input: s = "(]"
//
// Output: false
//
//
// Example 4:
//
//
// Input: s = "([])"
//
// Output: true
//
//
//
// Constraints:
//
//
// 	1 <= s.length <= 10⁴
// 	s consists of parentheses only '()[]{}'.
//

package main

func isValid(s string) bool {
	stack := []rune{}
	close := map[rune]rune{')': '(', ']': '[', '}': '{'}
	if len(s)%2 != 0 {
		return false
	}
	for _, c := range s {
		ln := len(stack)
		if cp, ok := close[c]; !ok {
			stack = append(stack, c)
		} else {
			if ln > 0 && stack[ln-1] == cp {
				stack = stack[:ln-1]
			} else {
				return false
			}
		}
	}
	if len(stack) > 0 {
		return false
	}
	return true
}
