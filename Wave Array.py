#Given an array of integers, sort the array into a wave like array and return it, 
#In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()
        i=0
        while((i+1)<len(A)):
            A[i],A[i+1]=A[i+1],A[i]
            i+=2
        return A
