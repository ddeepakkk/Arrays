

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        break_point = -1

        # Step 1: Find the first decreasing element from the right
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break_point = i
                break  # stop at the first such element

        # Step 2: If no such element, array is highest permutation → reverse
        if break_point == -1:
            nums.reverse()
            return

        # Step 3: Find the next greater element to swap with break_point
        for j in range(n - 1, break_point, -1):
            if nums[j] > nums[break_point]:
                nums[break_point], nums[j] = nums[j], nums[break_point]
                break

        # Step 4: Reverse the suffix after break_point
        left, right = break_point + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


## nums[idx + 1:] = reversed(nums[idx + 1:])  update multile values at a time
## O(n)+O(n)+O(n)=O(3n)
