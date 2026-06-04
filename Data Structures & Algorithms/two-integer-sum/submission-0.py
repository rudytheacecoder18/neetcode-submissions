from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [0, 0]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # avoid using same element twice
                if nums[i] + nums[j] == target:
                    arr[0] = i
                    arr[1] = j
                    return arr

        return arr