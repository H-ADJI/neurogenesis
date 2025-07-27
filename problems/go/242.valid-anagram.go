// Category: algorithms
// Level: Easy
// Percent: 66.54548%

// Given two strings s and t, return true if t is an anagram of s, and false otherwise.
//
//
// Example 1:
//
//
// Input: s = "anagram", t = "nagaram"
//
// Output: true
//
//
// Example 2:
//
//
// Input: s = "rat", t = "car"
//
// Output: false
//
//
//
// Constraints:
//
//
// 	1 <= s.length, t.length <= 5 * 10⁴
// 	s and t consist of lowercase English letters.
//
//
//
// Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
//
// use a bit vector to compare that s and p has same chars count
// for unicode characters we use a map and we increase decrease count as before
// O(s + p)
//
// sort the two strings alphabetically and then should be equal

package main

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	counter := make([]int, 26)
	base := byte('a')
	for _, c := range []byte(s) {
		counter[c-base] += 1
	}
	for _, c := range []byte(t) {
		counter[c-base] -= 1
	}
	for _, v := range counter {
		if v != 0 {
			return false
		}
	}
	return true
}
