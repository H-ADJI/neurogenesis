// Category: algorithms
// Level: Medium
// Percent: 70.808205%

// Given an array of strings strs, group the anagrams together. You can return the answer in any order.
//
//
// Example 1:
//
//
// Input: strs = ["eat","tea","tan","ate","nat","bat"]
//
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
//
// Explanation:
//
//
// 	There is no string in strs that can be rearranged to form "bat".
// 	The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
// 	The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
//
//
//
// Example 2:
//
//
// Input: strs = [""]
//
// Output: [[""]]
//
//
// Example 3:
//
//
// Input: strs = ["a"]
//
// Output: [["a"]]
//
//
//
// Constraints:
//
//
// 	1 <= strs.length <= 10⁴
// 	0 <= strs[i].length <= 100
// 	strs[i] consists of lowercase English letters.
//

package main

func HashString(str string) [26]int {
	strHash := [26]int{}
	for _, c := range []byte(str) {
		strHash[c-byte('a')]++
	}
	return strHash
}
func groupAnagrams(strs []string) [][]string {
	groups := make(map[[26]int][]string)
	for _, s := range strs {
		strHash := HashString(s)
		groups[strHash] = append(groups[strHash], s)
	}
	r := make([][]string, 0)
	for _, v := range groups {
		r = append(r, v)
	}
	return r
}
