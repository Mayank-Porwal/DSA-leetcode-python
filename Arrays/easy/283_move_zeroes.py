"""
Problem: Move Zeroes
Link: https://leetcode.com/problems/move-zeroes
Pattern: Two pointers
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            lp, rp = 0, 1

            while rp < len(nums):
                if nums[lp] == 0 and nums[rp] != 0:
                    self.swap_values(nums, lp, rp)
                    lp += 1
                    rp += 1
                elif nums[lp] == 0 and nums[rp] == 0:
                    rp += 1
                else:
                    lp += 1
                    rp += 1

        print(nums)

    def swap_values(self, nums: List[int], a: int, b: int):
        nums[a], nums[b] = nums[b], nums[a]


if __name__ == '__main__':
    solution = Solution()
    solution.moveZeroes([0, 1, 0, 3, 12])
