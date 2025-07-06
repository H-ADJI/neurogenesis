// Category: algorithms
// Level: Easy
// Percent: 63.580948%

// Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
//
//
// Example 1:
//
//
// Input: s = "leetcode"
//
// Output: 0
//
// Explanation:
//
// The character 'l' at index 0 is the first character that does not occur at any other index.
//
//
// Example 2:
//
//
// Input: s = "loveleetcode"
//
// Output: 2
//
//
// Example 3:
//
//
// Input: s = "aabb"
//
// Output: -1
//
//
//
// Constraints:
//
//
// 	1 <= s.length <= 10⁵
// 	s consists of only lowercase English letters.
//
// naive solution go through the string and for each char re-scan string to see if there are duplicates O(n^2)
// better approach is to create a char counter map and look for first char with count == 1 O(n) runtime but more memory
// best approach is to use a fixed 26-sized array to count freq of chars and check the first char that have count=1 O(n) and less memory

package main

func firstUniqChar(s string) int {
	count := [26]int{}
	for _, ch := range s {
		count[ch-'a']++
	}
	for i, ch := range s {
		if count[ch-'a'] == 1 {
			return i
		}
	}
	return -1
}
