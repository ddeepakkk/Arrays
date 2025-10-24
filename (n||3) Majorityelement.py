

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans = []

        for i in range(n):
            count =0
            for j in range(n):
                if(nums[i] == nums[j]):
                    count +=1
             if(count > n// 3):
                if(nums[i] not in ans):
                  ans.append(nums[i])

        return ans


Time Complexity: O(n^2) 
                      The check if nums[i] not in ans is effectively O(1) because at most 2 elements can appear more than n/3 times
 Space Complexity: O(1) 
                       ans stores at most 2 elements


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dic = {}
        ans = []

        # Count frequencies of each element
        for i in range(n):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1

        # Check which elements appear more than n//3 times
        for key in dic:
            if dic[key] > n // 3:
                ans.append(key)

        return ans


Time Complexity: O(n)
 One pass to build the frequency dictionary + one pass to check keys.

Space Complexity: O(n)
 Dictionary stores counts of up to n unique elements; answer list is constant size (≤ 2).


from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []

        maj1, maj2 = 0, 0  # initialize differently
        cnt1, cnt2 = 0, 0
        l = []

        # Step 1: Find potential candidates
        for i in range(n):
            if cnt1 == 0 and nums[i] != maj2:
                maj1 = nums[i]
                cnt1 = 1
            elif cnt2 == 0 and nums[i] != maj1:
                maj2 = nums[i]
                cnt2 = 1
            elif nums[i] == maj1:
                cnt1 += 1
            elif nums[i] == maj2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        # Step 2: Verify the candidates
        freq1, freq2 = 0, 0
        for num in nums:
            if num == maj1:
                freq1 += 1
            elif num == maj2:
                freq2 += 1

        if freq1 > n // 3:
            l.append(maj1)
        if freq2 > n // 3:
            l.append(maj2)

        return l



edge cases ---- [0,0,0,0] , [2,2] , [0,0]

