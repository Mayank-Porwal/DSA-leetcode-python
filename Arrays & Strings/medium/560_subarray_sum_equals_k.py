"""
Problem: Subarray Sum Equals K
Link: https://leetcode.com/problems/subarray-sum-equals-k/description/
Pattern: Prefix sum
Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)

Notes:
    - Looked up solution on Leetcode.
    - Prefix Sum technique learnt.
    - Keep calculating prefix sum. For that position, check if the diff(ps - k) exists in the dict.
    - If it does, then add the value to the result.
    - Add the ps with value 1 in the map.
"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        curr_prefix_sum = 0

        # Map to hold the mapping of prefix_sum and its number of occurrences
        # Default to 0:1 to handle the base case.
        # Imagine it to be a prefix sum of 0 before the beginning of the array.
        prefix_sum_map = {0: 1}

        for num in nums:
            curr_prefix_sum += num
            diff = curr_prefix_sum - k

            if diff in prefix_sum_map:
                result += prefix_sum_map[diff]

            prefix_sum_map[curr_prefix_sum] = prefix_sum_map.get(curr_prefix_sum, 0) + 1

        return result


if __name__ == '__main__':
    solution = Solution()
    ans = solution.subarraySum([1, 2, 3], 3)
    print(ans)
