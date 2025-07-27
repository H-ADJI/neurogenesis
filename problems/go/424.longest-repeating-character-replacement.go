// Category: algorithms
// Level: Medium
// Percent: 57.009506%

// You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character.
// You can perform this operation at most k times.
//
// Return the length of the longest substring containing the same letter you can get after performing the above operations.
//
//
// Example 1:
//
// Input: s = "ABACBBB", k = 2
// Output: 4
// Explanation: Replace the two 'A's with two 'B's or vice versa.
//
//
// Example 2:
//
// Input: s = "AABACBA", k = 1
// Output: 4
// Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
// The substring "BBBB" has the longest repeating letters, which is 4.
// There may exists other ways to achieve this answer too.
//
//
// Constraints:
//
//
// 	1 <= s.length <= 10⁵
// 	s consists of only uppercase English letters.
// 	0 <= k <= s.length
//
// idea : map each char to its first appearance and how many breaks until its other appearance

package main

func characterReplacement(s string, k int) int {
	count := make([]int, 26)
	left := 0
	maxCount := 0
	res := 0

	for right := 0; right < len(s); right++ {
		count[s[right]-'A']++
		maxCount = max(maxCount, count[s[right]-'A'])

		// if we need to replace more than k chars, shrink window
		if (right - left + 1 - maxCount) > k {
			count[s[left]-'A']--
			left++
		}
		res = max(res, right-left+1)
	}
	return res
}
