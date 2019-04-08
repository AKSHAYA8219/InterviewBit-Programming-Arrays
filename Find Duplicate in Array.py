#Given a read only array of n + 1 integers between 1 and n
#find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        sum=0
        n=len(A)
        for i in A:
            sum+=i
        return sum-(n*(n-1)/2)
