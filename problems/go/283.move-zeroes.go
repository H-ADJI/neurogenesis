// Category: algorithms
// Level: Easy
// Percent: 62.753616%

// Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
//
// Note that you must do this in-place without making a copy of the array.
//
//
// Example 1:
// Input: nums = [0,1,0,3,12]
// Output: [1,3,12,0,0]
// Example 2:
// Input: nums = [0]
// Output: [0]
//
//
// Constraints:
//
//
// 	1 <= nums.length <= 10⁴
// 	-2³¹ <= nums[i] <= 2³¹ - 1
//
//
//
// Follow up: Could you minimize the total number of operations done?
// two pointers
// one is going trought the list looking for non zero numbers
// the second pointer has the index of element to replace

package main

func moveZeroes(nums []int) {
	lastNonZero := 0
	for i := range nums {
		if nums[i] != 0 {
			nums[i], nums[lastNonZero] = nums[lastNonZero], nums[i]
			lastNonZero++
		}
	}
}
