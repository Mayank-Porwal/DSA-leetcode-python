"""
Problem: Subarray Sums Divisible by K
Link: https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
Pattern: Prefix sum
Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)

Notes:
    ** If the condition in the question is loose, like < or > some value, then think about SLIDING WINDOW**
    ** If the condition is exact, like == target, then think about prefix_sum.

    - Prefix Sum technique.
    - Keep a variable to track prefix_sum. Also, have a map to hold modulus of prefix_sum and k to its occurrences
    mapping
    - Keep incrementing prefix_sum in every iteration by adding the curr number to it.
    - Find remainder, i.e., rem = ps % k
    - If rem in map, increment result by map[rem]
    - Update map to store rem with its occurrences. Either add 1 to already existing one, or make a new entry.
    - Return result
"""

from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ps, result = 0, 0
        ps_map = {0: 1}  # ps % k : no of occurrences

        for num in nums:
            ps += num
            remainder = ps % k

            if remainder in ps_map:
                result += ps_map[remainder]

            ps_map[remainder] = ps_map.get(remainder, 0) + 1

        return result


if __name__ == '__main__':
    solution = Solution()
    ans = solution.subarraysDivByK([4, 5, 0, -2, -3, 1], 5)
    print(ans)
