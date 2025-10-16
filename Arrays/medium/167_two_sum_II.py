"""
Problem: Two Sum II - Input Array Is Sorted
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
Pattern: Two pointers + Binary search
Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left <= right:
            potential_match = numbers[left] + numbers[right]
            if potential_match > target:
                right -= 1
            elif potential_match < target:
                left += 1
            else:
                return [left + 1, right + 1]


if __name__ == '__main__':
    solution = Solution()
    op = solution.twoSum([2, 7, 11, 15], 9)
    print(op)
