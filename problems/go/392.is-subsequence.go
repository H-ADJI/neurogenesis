// Category: algorithms
// Level: Easy
// Percent: 48.34701%

// Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
//
// A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
//
//
// Example 1:
// Input: s = "abc", t = "ahbgdc"
// Output: true
// Example 2:
// Input: s = "axc", t = "ahbgdc"
// Output: false
//
//
// Constraints:
//
//
// 	0 <= s.length <= 100
// 	0 <= t.length <= 10⁴
// 	s and t consist only of lowercase English letters.
//
//
//
// Follow up: Suppose there are lots of incoming s, say s₁, s₂, ..., sk where k >= 10⁹, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
//
// fast and slow pointer strategy
// one slow pointer go throught the source string and for each match we increment pointer
// the fast pointer increments in both cases we match a char for s to t or not
// O(s + t) runtime complexity

package main

func isSubsequence(s string, t string) bool {
	i, j := 0, 0
	for i < len(s) && j < len(t) {
		if s[i] == t[j] {
			i++
		}
		j++
	}
	return i == len(s)
}
