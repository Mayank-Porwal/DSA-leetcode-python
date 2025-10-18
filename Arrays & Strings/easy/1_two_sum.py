"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum
Pattern: Hash table
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ele_map = {}
        output = []

        for ix, ele in enumerate(nums):
            potential_match = target - ele
            if potential_match not in ele_map:
                ele_map[ele] = ix
            else:
                return [ix, ele_map[potential_match]]


if __name__ == '__main__':
    solution = Solution()
    op = solution.twoSum([2, 7, 11, 15], 9)
    print(op)
