

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans,sumi = -99991 ,-99001

        for i in range(n):
            sumi += nums[i]
            sumi = max(sumi,nums[i])
            
            ans = max(sumi,ans)
            


        return ans


### but to print the sub array also we must store start of subarray end of subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans, sumi = -99991, -99001

        start = 0          # potential start of current subarray
        end = 0            # end of max subarray
        temp_start = 0     # temp start index for new subarray

        for i in range(n):
            sumi += nums[i]

            # if starting new subarray gives better sum
            if nums[i] > sumi:
                sumi = nums[i]
                temp_start = i  # new potential start index

            # update overall best
            if sumi > ans:
                ans = sumi
                start = temp_start
                end = i

        # print the subarray
        print("Maximum Subarray:", nums[start:end+1])

        return ans

