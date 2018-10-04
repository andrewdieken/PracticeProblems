#==========================================================
# Permutations
#==========================================================
# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

#==========================================================
# Solution
#==========================================================
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            new_res = []
            for i in range(len(res)):
                print(new_res)
                prev = res[i]
                prev.append(num)
                print(prev)
                for j in range(len(prev)):
                    prev[j], prev[-1] = prev[-1], prev[j]
                    new_res.append(prev[:])
                    prev[j], prev[-1] = prev[-1], prev[j]
            res = new_res
        return res
