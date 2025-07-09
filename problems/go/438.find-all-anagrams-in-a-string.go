// Category: algorithms
// Level: Medium
// Percent: 52.12287%

// Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
//
//
// Example 1:
//
// Input: s = "cbaebabacd", p = "abc"
// Output: [0,6]
// Explanation:
// The substring with start index = 0 is "cba", which is an anagram of "abc".
// The substring with start index = 6 is "bac", which is an anagram of "abc".
//
//
// Example 2:
//
// Input: s = "abab", p = "ab"
// Output: [0,1,2]
// Explanation:
// The substring with start index = 0 is "ab", which is an anagram of "ab".
// The substring with start index = 1 is "ba", which is an anagram of "ab".
// The substring with start index = 2 is "ab", which is an anagram of "ab".
//
//
//
// Constraints:
//
//
// 	1 <= s.length, p.length <= 3 * 10⁴
// 	s and p consist of lowercase English letters.
//
// a sliding window where we compute the frequency vector at each window and compare
// to the target

package main

func findAnagrams(s string, p string) []int {
	HashString := func(str string) [26]int {
		strHash := [26]int{}
		for _, c := range []byte(str) {
			strHash[c-byte('a')]++
		}
		return strHash
	}
	windowSize := len(p)
	targetHash := HashString(p)
	r := []int{}
	for i := range len(s) - windowSize + 1 {
		currentHash := HashString(s[i : i+windowSize])
		if currentHash == targetHash {
			r = append(r, i)
		}
	}
	return r
}
