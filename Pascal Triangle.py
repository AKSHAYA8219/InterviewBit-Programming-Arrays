#Given numRows, generate the first numRows of Pascal’s triangle.

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        P = []
        i = 0;
        while i < A:
            row = []
            for j in range(i + 1):
                if j == 0:
                    row.append(1)
                elif j == i:
                    row.append(1);
                else:
                    row.append(P[i - 1][j-1] + P[i - 1][j])
            P.append(row)
            i += 1;
        return P
