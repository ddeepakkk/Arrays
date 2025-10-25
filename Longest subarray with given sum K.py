
def longestSubarray(arr, k):
    ans = 0

    for i in range(len(arr)):
        
        # Sum of subarray from i to j
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
          
            # If subarray sum is equal to k
            if sum == k:
              
                # find subarray length and update result
                subLen = j - i + 1
                ans = max(ans, subLen)
    
    return res      


optimal for ARRAT CONTAITONG POSITIVES AND NEGATIVES 

class Solution:
    def longestSubarray(self, nums, k):
        n = len(nums)
        ans  = 0
        sumi = 0
        dic={0:-1}  ## IF(SUMI == K ) IT IS ALSO A SUB ARRAY  whie traversing  

        for i in range(n):
            sumi += nums[i]

            req_sum = sumi - k

            if(req_sum in dic ):
                sub_arr_len = i - dic[req_sum]
                ans = max(ans,sub_arr_len)

            if(sumi not in dic):      ## IF PREFIX SUM IS REPEATED IT UPDATES WHEN ADDED WE NNED OUR SUBARRAY AS LONG AS POSSIBLE SO THIS IS IMP 
                dic[sumi] = i

        return ans 

Time: O(n) → single pass through array.

Space: O(n) → hashmap stores at most n prefix sums.




OPTIMAL soln if only nonnegatives are there  in arr given 

class Solution:
    def longestSubarray(self, nums, k):
        n = len(nums)
        ans  = 0
        sumi = 0

        i = 0
        for j in range(n):                           --------  O(N)
            sumi += nums[j]

            while(sumi>k): -------                    ------  no of time it executes is maximum how many times i can go its total O(N) for j--- from 1 to n
                sumi -= nums[i]
                i+=1

            if(sumi == k):
                ans= max(ans,j-i+1)

        return ans





                


                
            


            
            



                
        


          





                
            


            
            



                
        


          






