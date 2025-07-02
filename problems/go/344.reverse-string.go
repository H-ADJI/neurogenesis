// Category: algorithms
// Level: Easy
// Percent: 79.694954%

// Write a function that reverses a string. The input string is given as an array of characters s.
//
// You must do this by modifying the input array in-place with O(1) extra memory.
//
//
// Example 1:
// Input: s = ["h","e","l","l","o"]
// Output: ["o","l","l","e","h"]
// Example 2:
// Input: s = ["H","a","n","n","a","h"]
// Output: ["h","a","n","n","a","H"]
//
//
// Constraints:
//
//
// 	1 <= s.length <= 10⁵
// 	s[i] is a printable ascii character.
//
// swaping both ends using two pointers
// O(n) runtime

package main

func reverseString(s []byte) {
	n := len(s)
	for i := range n / 2 {
		s[i], s[n-i-1] = s[n-i-1], s[i]
	}
}
