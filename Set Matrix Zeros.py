#Given an m x n matrix of 0s and 1s, if an element is 0, set its entire row and column to 0.

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        ''' Three passes approach:
               - flag each row and col to be cleaned
               - clean by row, then by col.
               
            Time = O(size(A))   Space = constant.
        '''
        
        # bitmask
        FLAG_ROW = 2
        FLAG_COL = 4
        
        if not A:
            return A
        m, n = len(A), len(A[0])

        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    # flag row and col
                    A[i][0] |= FLAG_ROW
                    A[0][j] |= FLAG_COL
        
        for i in range(m):
            if A[i][0] & FLAG_ROW:
                for j in range(n):
                    A[i][j] &= FLAG_COL  # Clear but keep this flag
        
        for j in range(n):
            if A[0][j] & FLAG_COL:
                for i in range(m):
                    A[i][j] = 0
        
        return A
