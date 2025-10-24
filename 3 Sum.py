class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        # Brute-force: check every triplet                                       
        for i in range(n):                                                                                                             
            for j in range(i + 1, n):                                                                
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])   
                        if triplet not in res:
                            res.append(triplet)
        
        return res

"""
Summary of Time Complexity:

- Three nested loops: O(n^3) → checks all triplets  ## POSSIBLE NUMBER OF TRIPLETS n c 3 = order of n"3
- 'triplet not in res': O(n^3) worst-case → membership check in list of stored triplets  
- Total worst-case: O(n^6)
- Space complexity: O(n^3) → storing all unique triplets
"""

## BETTER


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        dic = {}
        ans = []

        for i in range(n):
            dic[nums[i]] = i

        for i in range(n):
            for j in range(i+1,n):
                sumi = nums[i] + nums[j]

                if(-sumi in dic and dic[-sumi] != i and dic[-sumi] != j):
                    triplet = [nums[i],nums[j],nums[dic[-sumi]]]
                    triplet.sort()
                    if(triplet not in ans ):
                        ans.append(triplet)


        return ans



"""
Summary of Time Complexity:

- Dictionary creation: O(n) → store last index of each number
- Two nested loops: O(n^2) → check all pairs (i, j)
- Dictionary lookup: O(1) per pair
- Sorting triplet: O(1) (3 elements)
- Membership check 'triplet not in res': O(n^3) worst-case
- Total worst-case time: O(n^5)
- Space complexity: O(n^3) → storing all unique triplets
"""



## OPTIMAL


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()  # O(n log n) for sorting
        ans = []     # O(1) extra space (ignoring output)

        for i in range(n):  # O(n) outer loop
            if i > 0 and nums[i] == nums[i - 1]:  # skip duplicates
                continue

            j = i + 1
            k = n - 1
            while j < k:  # O(n) two-pointer inner loop
                sumi = nums[i] + nums[j] + nums[k]

                if sumi == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:  # skip duplicates
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:  # skip duplicates
                        k -= 1

                elif sumi > 0:
                    k -= 1
                else:
                    j += 1

        return ans

"""
Summary of Time and Space Complexity:

- Sorting: O(n log n)
- Outer loop: O(n)
- Two-pointer inner loop: O(n) per outer iteration
- Total time: O(n^2)
- Space complexity: O(1) extra (excluding output list)
- Duplicate handling: skips repeated elements in outer and inner loops
"""





