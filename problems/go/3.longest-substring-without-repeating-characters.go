// Category: algorithms
// Level: Medium
// Percent: 36.79358%

// Given a string s, find the length of the longest substring without duplicate characters.
//
//
// Example 1:
//
// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.
//
//
// Example 2:
//
// Input: s = "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.
//
//
// Example 3:
//
// Input: s = "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.
// Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
//
//
//
// Constraints:
//
//
// 	0 <= s.length <= 5 * 10⁴
// 	s consists of English letters, digits, symbols and spaces.
//
// sliding window where we check if a character has been seen at the current window
// seen character are the ones in the map and in the current window

package main

func lengthOfLongestSubstring(s string) int {
	seen := make(map[byte]int)
	maxLen := 0
	left := 0

	for right := 0; right < len(s); right++ {
		ch := s[right]
		if idx, ok := seen[ch]; ok && idx >= left {
			left = idx + 1
		}
		seen[ch] = right
		if right-left+1 > maxLen {
			maxLen = right - left + 1
		}
	}

	return maxLen
}
