

class Solution:
    def maxLen(self, nums):
        # Your code goes here
        ans,sumi = 0,0
        n = len(nums)
        for i in range(n):          -------------- O(N)
            sumi = 0
            for j in range(i,n):-                 -----       O(N)
                sumi+= nums[j]

                if(sumi == 0):
                    ans = max(ans,j-i+1)
                
        return ans 




## OPTIMAL

class Solution:
    def maxLen(self, nums):
        # Your code goes here
        

        n =  len(nums)
        sumi,ans = 0,0
        dic= {0:-1}  ## for empty sub array

        for i in range(n):
            sumi+= nums[i]

            if(sumi in dic):   ## check for x-k in prefix sum to get x-(x-k) k sum subarray
                ans =  max(ans,i-dic[-sumi])

            if(sumi not in dic):
                dic[sumi] = i

        return ans






