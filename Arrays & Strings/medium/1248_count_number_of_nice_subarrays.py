"""
Problem: Count Number of Nice Subarrays
Link: https://leetcode.com/problems/count-number-of-nice-subarrays/description/
Pattern: Prefix sum
Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)

Notes:
    ** If the condition in the question is loose, like < or > some value, then think about SLIDING WINDOW**
    ** If the condition is exact, like == target, then think about prefix_sum.

    - Convert odd numbers to 1, and even numbers to 0.
    - Then this problem will be same as "930. Binary sub-arrays with sum"
"""

from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ps, result = 0, 0
        ps_occ_map = {0: 1}

        for num in nums:
            ps += num % 2

            diff = ps - k
            if diff in ps_occ_map:
                result += ps_occ_map[diff]

            ps_occ_map[ps] = ps_occ_map.get(ps, 0) + 1

        return result


if __name__ == '__main__':
    solution = Solution()
    ans = solution.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2)
    print(ans)
