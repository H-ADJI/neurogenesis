// Category: algorithms
// Level: Easy
// Percent: 69.89439%

// Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
//
//
// Example 1:
//
//
// Input: nums = [3,0,1]
//
// Output: 2
//
// Explanation:
//
// n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
//
//
// Example 2:
//
//
// Input: nums = [0,1]
//
// Output: 2
//
// Explanation:
//
// n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
//
//
// Example 3:
//
//
// Input: nums = [9,6,4,2,3,5,7,0,1]
//
// Output: 8
//
// Explanation:
//
// n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
// Constraints:
//
//
// 	n == nums.length
// 	1 <= n <= 10⁴
// 	0 <= nums[i] <= n
// 	All the numbers of nums are unique.
//
//
//
// Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
// naive solution is hash map and iterate and check missing O(n) space + runtime
// optimized is to use sum of concecutive integers formula or XOR operation O(n) runtime and constant space

package main

func missingNumber(nums []int) int {
	xor2 := 0
	xor1 := 0
	for i, v := range nums {
		xor1 ^= v
		xor2 ^= i
	}
	return xor2 ^ xor1
}
