#Given an index k, return the kth row of the Pascal’s triangle.
#Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        ans = [1]*(A+1)
        for i in range(2,A+1):
            pre =ans[0]
            for j in range(1,i):
                temp = ans[j]
                ans[j] = pre+ans[j]
                pre = temp
        return(ans)
