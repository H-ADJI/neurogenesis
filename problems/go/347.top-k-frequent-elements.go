// Category: algorithms
// Level: Medium
// Percent: 64.45056%

// Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
//
//
// Example 1:
// Input: nums = [1,1,1,2,2,3], k = 2
// Output: [1,2]
// Example 2:
// Input: nums = [1], k = 1
// Output: [1]
//
//
// Constraints:
//
//
// 	1 <= nums.length <= 10⁵
// 	-10⁴ <= nums[i] <= 10⁴
// 	k is in the range [1, the number of unique elements in the array].
// 	It is guaranteed that the answer is unique.
//
//
//
// Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
// naive solution : sorting the array and iteratively adding most frequent elements O(n.log n)
// optimized solution O(n) runtime + memory
// bucketing elements with frequency f at the f-th bucket
// the getting most frequent elements from each bucket until reaching k element limit

package main

import (
	"slices"
)

func topKFrequent(nums []int, k int) []int {
	counter := make(map[int]int)
	for _, v := range nums {
		counter[v]++
	}
	buckets := make([][]int, len(nums))
	for k, v := range counter {
		buckets[v-1] = append(buckets[v-1], k)
	}

	result := []int{}
	slices.Reverse(buckets)
	for _, b := range buckets {
		for _, v := range b {
			result = append(result, v)
			if len(result) == k {
				return result
			}
		}
	}
	return result
}
