


from typing import List

class Solution:
    """
    Merge Overlapping Sub-intervals

    Given a list of intervals, this function merges all overlapping intervals
    and returns a list of non-overlapping intervals sorted by start time.
    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return []

        # Sort intervals by start time
        intervals.sort()

        ans = []
        i = 0

        while i < n:
            a, b = intervals[i]  # current interval
            j = i + 1

            # Merge all overlapping intervals
            while j < n:
                c, d = intervals[j]
                if c <= b:  # overlap condition
                    b = max(b, d)
                    j += 1
                else:
                    break

            # Add merged interval to result
            ans.append([a, b])
            i = j  # move to next unprocessed interval

        return ans




            



BRUTE FORCE 
from typing import List

class Solution:
    """
    Brute-force approach to merge overlapping intervals.
    
    For each interval, check if it overlaps with any interval in the merged list.
    If it overlaps, merge them. Otherwise, add it as a new interval.
    Time Complexity: O(n^2)
    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        merged = [intervals[0]]  # initialize with first interval

        for i in range(1, len(intervals)):
            a, b = intervals[i]
            merged_flag = False

            # Check overlap with existing merged intervals
            for j in range(len(merged)):
                c, d = merged[j]
                if not (b < c or d < a):  # overlap condition
                    merged[j][0] = min(a, c)
                    merged[j][1] = max(b, d)
                    merged_flag = True
                    break

            # If no overlap found, append interval
            if not merged_flag:
                merged.append([a, b])

        return merged


# Example usage
if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(sol.merge(intervals))  # Output: [[1,6],[8,10],[15,18]]







