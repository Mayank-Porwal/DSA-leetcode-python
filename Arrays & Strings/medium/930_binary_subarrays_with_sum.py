"""
Problem: Binary Subarrays With Sum
Link: https://leetcode.com/problems/binary-subarrays-with-sum/description/
Pattern: Prefix sum
Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)

Notes:
    ** If the condition in the question is loose, like < or > some value, then think about SLIDING WINDOW**
    ** If the condition is exact, like == target, then think about prefix_sum.

    - Prefix Sum technique.
    - Keep a variable to track prefix_sum. Also, have a map to hold prefix_sum to its occurrences mapping
    - Keep incrementing prefix_sum in every iteration by adding the curr number to it.
    - Find diff, i.e., diff = ps - goal
    - If diff in map, increment result by map[diff]
    - Update map to store prefix_sum with its occurrences. Either add 1 to already existing one, or make a new entry.
    - Return result
"""

from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ps, result = 0, 0
        ps_occurrences_map = {0: 1}

        for num in nums:
            ps += num
            diff = ps - goal

            if diff in ps_occurrences_map:
                result += ps_occurrences_map[diff]

            ps_occurrences_map[ps] = ps_occurrences_map.get(ps, 0) + 1

        return result


if __name__ == '__main__':
    solution = Solution()
    ans = solution.numSubarraysWithSum([1, 0, 1, 0, 1], goal=2)
    print(ans)
