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
            print('num:',num)
            for i in range(len(res)):
                prev = res[i]
                print('prev before append {}: {}'.format(num, prev))
                prev.append(num)
                print('prev after append {}: {}'.format(num, prev))
                for j in range(len(prev)):
                    print('for {} in: {}:'.format(prev[j], prev))
                    prev[j], prev[-1] = prev[-1], prev[j]
                    new_res.append(prev[:])
                    prev[j], prev[-1] = prev[-1], prev[j]
                    print(new_res)
            res = new_res
        return res


newSolution = Solution()
print(newSolution.permute([1,2,3]))
