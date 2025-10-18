"""
Problem: Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/description/
Pattern: Hashing, Frequency Array
Difficulty: Medium

Time Complexity: O(n * k), where k is the length of the string
Space Complexity: O(nk)

Notes:
    - Solved it using Brute-force approach but the TC was O(n * n * m).
    - Looked up solution on Leetcode.
    - First was applying sorting on each word. Better but TC was still O(n * m logm)
    - Using a frequency array did the job.
    - Tuple(count) trick saves sorting cost and uses constant alphabet size.
    - Need to use tuple because it's hashable and can be stored as key in dict. List is unhashable.
"""


from typing import List


# Brute-force approach
# TC: O(n*n*m)
# SC: O(n + m) if only english alphabets, otherwise O(n * m) if all strings
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        if not strs:
            return []

        groups = []
        visited = {}

        for i in range(len(strs)):
            anagrams = [strs[i]]
            if strs[i] not in visited:
                for j in range(i + 1, len(strs)):
                    if self.check_anagram(strs[i], strs[j]):
                        anagrams.append(strs[j])
                        visited[strs[j]] = True

                visited[strs[i]] = True
                groups.append(anagrams)

        return groups

    def check_anagram(self, s1: str, s2: str) -> bool:
        hashMap = {}

        if (s1 and not s2) or (s2 and not s1) or len(s1) != len(s2):
            return False

        for i in s1:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1

        for i in s2:
            if i not in hashMap or hashMap[i] == 0:
                return False
            hashMap[i] -= 1

        return True


# Optimized solution using frequency array
# TC: O(n*m)
# SC: O(nm)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}

        for s in strs:
            freq_array = [0] * 26

            for c in s:
                freq_array[ord(c) - ord('a')] += 1

            key = tuple(freq_array)
            if key in output:
                output[key].append(s)
            else:
                output[key] = [s]

        return list(output.values())


if __name__ == '__main__':
    solution1 = Solution1()
    ans = solution1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(ans)

    solution = Solution()
    ans = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(ans)
