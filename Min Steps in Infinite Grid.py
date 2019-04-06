#You are in an infinite 2D grid where you can move in any of the 8 directions :
#You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        prev_x, prev_y, total = A[0], B[0], 0
        for curr_x, curr_y in zip(A, B):
            dx, dy = abs(curr_x - prev_x), abs(curr_y - prev_y)
            if dx < dy:
                total += dy
            else:
                total += dx
            prev_x, prev_y = curr_x, curr_y
        return total
