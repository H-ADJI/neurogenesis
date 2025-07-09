// Category: algorithms
// Level: Medium
// Percent: 73.96178%

// Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
//
// Return the sorted string. If there are multiple answers, return any of them.
//
//
// Example 1:
//
// Input: s = "tree"
// Output: "eert"
// Explanation: 'e' appears twice while 'r' and 't' both appear once.
// So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
//
//
// Example 2:
//
// Input: s = "cccaaa"
// Output: "aaaccc"
// Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
// Note that "cacaca" is incorrect, as the same characters must be together.
//
//
// Example 3:
//
// Input: s = "Aabb"
// Output: "bbAa"
// Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
// Note that 'A' and 'a' are treated as two different characters.
//
//
//
// Constraints:
//
//
// 	1 <= s.length <= 5 * 10⁵
// 	s consists of uppercase and lowercase English letters and digits.
//
// sorting by frequency by grouping i-frequent chars into the i-th bucket
// then going through the buckets and repeating each char i times

package main

import (
	"slices"
	"strings"
)

func frequencySort(s string) string {
	counter := make(map[rune]uint)
	for _, r := range s {
		counter[r]++
	}
	buckets := make([][]rune, len(s))
	for k, v := range counter {
		buckets[v-1] = append(buckets[v-1], k)
	}
	b := strings.Builder{}
	slices.Reverse(buckets)
	for i, bucket := range buckets {
		for _, r := range bucket {
			b.WriteString(strings.Repeat(string(r), len(s)-i))
		}
	}
	return b.String()
}
