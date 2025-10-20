"""
Problem: Contiguous Array
Link: https://leetcode.com/problems/contiguous-array/
Pattern: Prefix sum
Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)

Notes:
    - Looked up solution on YouTube(https://www.youtube.com/watch?v=9ZyLjjk536U).
    - Prefix Sum technique with a twist.
    - Keep a variable to track prefix_sum. Also, have a map to hold prefix_sum to index mapping
    - Increment it when 1 comes, and decrement it when 0 comes.
    - Special case: if prefix_sum == 0, then just update result = max(result, i - 0 + 1)
    - If above doesn't hold true, then lookup the prefix_sum in the map.
    - If found, result = max(result, i - map[prefix_sum])
    - If not found, update the map with prefix_sum and its index.
    - Return result
"""

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum, result = 0, 0
        prefix_sum_index_map = {}

        for i, num in enumerate(nums):
            if num == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1

            if prefix_sum == 0:
                result = max(result, i - 0 + 1)
            elif prefix_sum in prefix_sum_index_map:
                result = max(result, i - prefix_sum_index_map[prefix_sum])
            elif prefix_sum not in prefix_sum_index_map:
                prefix_sum_index_map[prefix_sum] = i

        return result


if __name__ == '__main__':
    solution = Solution()
    ans = solution.findMaxLength([0, 1, 1, 1, 1, 1, 0, 0, 0])
    print(ans)
