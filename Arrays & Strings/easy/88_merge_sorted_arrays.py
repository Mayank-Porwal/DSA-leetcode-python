"""
Problem: Merge Sorted Arrays & Strings
Link: https://leetcode.com/problems/merge-sorted-array
Pattern: Two pointers
Difficulty: Easy

Time Complexity: O(m + n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        m_idx = m - 1
        n_idx = n - 1

        while n_idx >= 0:
            if m_idx >= 0 and nums1[m_idx] > nums2[n_idx]:
                nums1[last] = nums1[m_idx]
                m_idx -= 1
            else:
                nums1[last] = nums2[n_idx]
                n_idx -= 1

            last -= 1

        print(nums1)


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution.merge(nums1, m, nums2, n)
