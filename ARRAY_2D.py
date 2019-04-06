#Predict the output of the following program :

#The pgm reverses each sublist of the main list A

def performOps(A):
    m = len(A)
    n = len(A[0])
    B = []
    for i in xrange(len(A)):
        B.append([0] * n)
        for j in xrange(len(A[i])):
            B[i][n - 1 - j] = A[i][j]
    return B
    
B = performOps(A)
for i in xrange(len(B)):
    for j in xrange(len(B[i])):
        print B[i][j],
        
# output :4 3 2 1 8 7 6 5 12 11 10 9
