Given an integer n, return all the  n rows of of Pascal's triangle


## first let us detremine nth row of  pascal triangle  (0 - based indexed )

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l = []                               # SC: O(n) to store the row
        n = rowIndex 
        res = 1
        l.append(1)

        for i in range(1, n + 1):            # Loop runs n times → TC: O(n)
            res = res * (n - i + 1) // i     # O(1) each iteration
            l.append(res)

        return l                             # TC: O(n), SC: O(n)

Time Complexity: O(n)

Space Complexity: O(n) (for the output list only — no extra space used)


## to print traingale upto n rows (1-based indexing)



def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):            # 0 to numRows-1
            result.append(self.getRow(i))   # get each row
        return result  










