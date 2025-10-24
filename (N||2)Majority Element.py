>N//2


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            count = 0
            for j in range(n):
                if(nums[i] == nums[j]):
                    count+=1
            if(count > n//2):
                return  nums[i]

TC --- O(n2) 10¹⁰ operations in Python ≈ 16–17 minutes

Definitely much more than 1–2 seconds allowed on LeetCode → causes TLE.
SC ---- 0(1)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        nums.sort()

        return nums[n//2]

TC----- O(nlogn)

## COUNT OF MAJORITY ELEMENTS ALWAYS WINS 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        count,maj_el = 0,0

        for i in range(n):
            if(count == 0):
                maj_el = nums[i]
            
            if(nums[i] == maj_el):
                count+=1
            else:
                count-=1
            
        return maj_el

TC ----- O(n)
        
