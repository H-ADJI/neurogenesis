// Category: algorithms
// Level: Easy
// Percent: 55.652203%

// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
//
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
//
// You can return the answer in any order.
//
//
// Example 1:
//
// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
//
//
// Example 2:
//
// Input: nums = [3,2,4], target = 6
// Output: [1,2]
//
//
// Example 3:
//
// Input: nums = [3,3], target = 6
// Output: [0,1]
//
//
//
// Constraints:
//
//
// 	2 <= nums.length <= 10⁴
// 	-10⁹ <= nums[i] <= 10⁹
// 	-10⁹ <= target <= 10⁹
// 	Only one valid answer exists.
//
//
//
// Follow-up: Can you come up with an algorithm that is less than O(n²) time complexity?
// naive solution : try all combinations and calculate the sum to find the indices O(n^2)
// optimal solution : go trought the list, and for each iteration store in a hashmap
// the index of the current number so for future iteration we check if target - current_element
// already exists in the cache and return the two indeces O(n) runtime + O(n) memory

package main

func twoSum(nums []int, target int) []int {
	cache := make(map[int]int)
	for i, n := range nums {
		diff := target - n
		if j, ok := cache[diff]; ok {
			return []int{j, i}
		} else {
			cache[n] = i
		}
	}
	return []int{}
}
