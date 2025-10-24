

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.    (DONT USE SAME ELEMNT TWICE)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1, n):
                sumi = nums[i] + nums[j]
                if sumi == target:
                    return [i, j]

        return [-1, -1]

 Time Complexity: O(n^2) because of the nested loops checking all pairs
 Space Complexity: O(1) because no extra space is used besides variables

## GIVEN UNIQUE SOLUTION EDXITS DONT WORRY ABOUT DUPLICATES 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dic = {}

        for i in range(n):
            req = target - nums[i]
            if req in dic:
                return [i, dic[req]]
            dic[nums[i]] = i

        return [-1, -1]

Time Complexity: O(n) because we traverse the list once and dictionary operations are O(1) on average
 Space Complexity: O(n) because we store elements in a dictionary to track indices


## 2 POINTER ONLY GIVES YES OR NO THAT IF PIR IS PRESENT OR NOT 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        nums.sort()  # Sort the array to use two-pointer technique

        i, j = 0, n - 1  # Initialize two pointers at start and end

        while i < j:
            sumi = nums[i] + nums[j]

            if sumi == target:
                return "YES"  # Found a pair that sums to target
            elif sumi > target:
                j -= 1  # Decrease sum by moving right pointer left
            else:
                i += 1  # Increase sum by moving left pointer right

        return "NO"  # No pair found that sums to target

Time Complexity: O(n log n) → because of sorting (original indices positions changes)

Space Complexity: O(1) to return yes or no that pair exits or not 
                  O(n) → to store original indices along with numbers  (we have to 1st store initially the indices )





