

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, left = 0, 0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 1️⃣ Traverse top row
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # 2️⃣ Traverse right column (only if rows remain)
            if top <= bottom:
                for i in range(top, bottom + 1):
                    res.append(matrix[i][right])
                right -= 1

            # 3️⃣ Traverse bottom row (only if both valid)
            if top <= bottom and left <= right:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            # 4️⃣ Traverse left column (only if both valid)
            if left <= right and top <= bottom:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res

Time Complexity=O(m×n)  as i am traversing each element once 
