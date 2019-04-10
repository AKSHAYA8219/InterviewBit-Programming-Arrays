# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        A = intervals
        A.sort(key=lambda x: x.start)
        N = len(A)
        S = []
        if A:
            S.append(A[0])
            for i in range(1, N):
                B = A[i]
                if B.start <= S[-1].end:
                    S[-1].end = max(S[-1].end, B.end)
                else:
                    S.append(B)
        return S
