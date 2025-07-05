// Category: algorithms
// Level: Easy
// Percent: 62.343956%

// Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
//
//
// Example 1:
// Input: nums = [4,3,2,7,8,2,3,1]
// Output: [5,6]
// Example 2:
// Input: nums = [1,1]
// Output: [2]
//
//
// Constraints:
//
//
// 	n == nums.length
// 	1 <= n <= 10⁵
// 	1 <= nums[i] <= n
//
//
//
// Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
// with extra space :
// create new array that will mark existing numbers indeces O(n) space and time
// without extra space :
// inplace mark existing number by going to the respective index - 1 and negating the number
// non negated numbers are the missing ones O(n) time and constant space

package main

func findDisappearedNumbers(nums []int) []int {
	missing := make([]int, len(nums))
	res := []int{}
	for _, v := range nums {
		missing[v-1] = 1
	}
	for i, v := range missing {
		if v == 0 {
			res = append(res, i+1)
		}
	}
	return res
}
