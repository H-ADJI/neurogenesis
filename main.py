from typing import List


class Solution:
    @staticmethod
    def rearrange(nums: List[int]):
        new = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                new.append(nums[i])
        for i in range(count):
            new.append(0)
        return new


print(Solution.rearrange([6, 0, 8, 2, 3, 0, 4, 0, 1]))
