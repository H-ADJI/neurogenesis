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
// since characters are ascii there are 26 possible characters
// we create a 26 long slice and for one string we increase the ith slice element
// when we find the ith alphabet character for the other string we decrease
// every element of slice should be 0 if they are anagram
// for unicode characters we use a map and we increase decrease count as before
// O(s + p)

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
