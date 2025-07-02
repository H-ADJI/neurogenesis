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
// Using a stack and a maping of closing to opening brackets
// verify that then length of the string is even.
// we fill the stack with opening brackets until we find a closing one
// then check if its the correct one if so pop from the stack otherwise
// return false, at the end verify that stack is empty to be sure all opening brackets
// were closed
// O(n)

package main

func isValid(s string) bool {
	stack := []rune{}
	closeOpenBrackets := map[rune]rune{')': '(', ']': '[', '}': '{'}
	if len(s)%2 != 0 {
		return false
	}
	for _, r := range s {
		ln := len(stack)
		if openingBracket, ok := closeOpenBrackets[r]; ok {
			if ln > 0 && stack[ln-1] == openingBracket {
				stack = stack[:ln-1]
			} else {
				return false
			}
		} else {
			stack = append(stack, r)
		}
	}
	return len(stack) == 0
}
