


Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        sumi,count  = 0,0

        for i in range(n):
            sumi = 0
            for j in range(i,n):
                sumi += nums[j]

                if(sumi == k):
                    count+=1
        return count

## OPTIMAL SOLUTION  TC -- O(N)  SC --- O(N)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        dic = {0:1}  # Stores counts of prefix sums; 0 sum occurs once initially 
        
        prefix_sub_arrays_sum = 0  # Running prefix sum
        count = 0  # Total subarrays with sum = k

        for i in range(n):
            prefix_sub_arrays_sum += nums[i]  # Add current element to prefix sum

            req_sum = prefix_sub_arrays_sum - k  # Needed sum to form a subarray of sum k

            if req_sum in dic:  
                count += dic[req_sum]  # If seen before, add number of occurrences to count

            # Update the count of current prefix sum
            if prefix_sub_arrays_sum in dic:
                dic[prefix_sub_arrays_sum] += 1
            else:
                dic[prefix_sub_arrays_sum] = 1
        
        return count  # Return total number of subarrays


 




IF ONLY NON NEGATIVES ARE PRESENT 
 TC ------ O(N)
  SC ----- -O(1)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        i = 0
        sumi = 0
        count = 0

        for j in range(n):
            sumi += nums[j]

            while sumi > k:
                sumi -= nums[i]
                i += 1

            if sumi == k:
                count += 1  # For counting all such subarrays

        return count







