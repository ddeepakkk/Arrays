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
class Solution:
    """
    Brute-force-ish approach for 4Sum using a dictionary for lookup.
    Finds all unique quadruplets that sum to target.
    """

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        dic = {}
        ans = []

        # Store the last index of each number
        for i in range(n):
            dic[nums[i]] = i

        # Triple nested loops to pick three numbers
        for j in range(n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    sumi = nums[j] + nums[k] + nums[l]
                    remaining = target - sumi

                    # Check if remaining number exists and indices are different
                    if remaining in dic and dic[remaining] != j and dic[remaining] != k and dic[remaining] != l:
                        quad = [remaining, nums[j], nums[k], nums[l]]
                        quad.sort()  # sort to avoid duplicates
                        if quad not in ans:
                            ans.append(quad)

        return ans


Optimal
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        i = 0
        while i < n - 3:
            # skip duplicates for i
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue

            j = i + 1
            while j < n - 2:
                # skip duplicates for j
                if j > i + 1 and nums[j] == nums[j-1]:
                    j += 1
                    continue

                k, l = j + 1, n - 1
                while k < l:
                    sumi = nums[i] + nums[j] + nums[k] + nums[l]

                    if sumi == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        # skip duplicates for k and l
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1
                    elif sumi < target:
                        k += 1
                    else:
                        l -= 1

                j += 1
            i += 1

        return ans


## using 2 for loops 
       from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n - 3):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicates for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                k, l = j + 1, n - 1
                while k < l:
                    sumi = nums[i] + nums[j] + nums[k] + nums[l]

                    if sumi == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        # Skip duplicates for the third and fourth numbers
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    elif sumi < target:
                        k += 1
                    else:
                        l -= 1

        return ans
        





        




