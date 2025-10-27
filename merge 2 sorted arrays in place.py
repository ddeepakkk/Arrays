def merge_arrays(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Merge two sorted arrays into a new sorted array.

    Args:
    nums1 (List[int]): First sorted array.
    nums2 (List[int]): Second sorted array.

    Returns:
    List[int]: A new sorted array containing all elements from nums1 and nums2.
    """




  
    n = len(nums1)
    m = len(nums2)
    
    i, j = 0, 0
    merged = []

    # Merge elements from both arrays
    while i < n and j < m:
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Add remaining elements from nums1
    while i < n:
        merged.append(nums1[i])
        i += 1

    # Add remaining elements from nums2
    while j < m:
        merged.append(nums2[j])
        j += 1

    return merged





## MERGING IN PLACE 

class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1  # pointer for nums1
        j = n - 1  # pointer for nums2
        k = m + n - 1  # pointer for merged result (end of nums1)

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # if nums2 still has elements left
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
