class Solution:
    """
    Brute-force approach for 4Sum problem.
    
    Given an array `nums` and a target, find all unique quadruplets [a,b,c,d] 
    such that a + b + c + d == target.
    Time Complexity: O(n^4)
    The O(n⁸) arises not from the loops themselves (O(n⁴)), but from the quad not in ans duplicate check
    """

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []

        # Check all quadruplets
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        sumi = nums[i] + nums[j] + nums[k] + nums[l]
                        if sumi == target:
                            quad = [nums[i], nums[j], nums[k], nums[l]]
                            quad.sort()  # sort to avoid duplicates
                            if quad not in ans:  # check uniqueness
                                ans.append(quad)

        return ans

## BETTER




