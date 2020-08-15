# Goodrich, Tamassia, Goldwasser (2013) Code Fragment 13.5 on page 596

def matrix_chain(d):
    """d is a list of n+1 numbers such that size of kth matrix is d[k]-by-d[k+1].

    Return an n-by-n table such that N[i][j] represents the minimum number of
    multiplications needed to compute the product of Ai through Aj inclusive.
    """
    n = len(d) - 1                                                 # number of matrices
    N = [[0] * n for i in range(n)]                       # initialize n-by-n result to zero
    for b in range(1, n):                                       # number of products in subchain
        for i in range(n-b):                                    # start of subchain
            j = i + b                                                 # end of subchain
            N[i][j] = min(N[i][k] + N[k+1][j] + d[i]*d[k+1]*d[j+1] for k in range(i, j))
    return N

if __name__ == '__main__':
    # Test 1: Single matrix
    print("Test 1")
    d = [3, 4]
    N = matrix_chain(d)
    for i in range(len(d)-1):
        for j in range(len(d)-1):
            print(N[i][j], end= " ")
        print()

    # Test 2: Two matrices
    print()
    print("Test 2")
    d = [3, 4, 5]
    N = matrix_chain(d)
    for i in range(len(d)-1):
        for j in range(len(d)-1):
            print(N[i][j], end=" ")
        print()

    # Test 3: Three matrices
    print()
    print("Test 3")
    d = [2, 10, 50, 20]
    N = matrix_chain(d)
    for i in range(len(d)-1):
        for j in range(len(d)-1):
            print(N[i][j], end=" ")
        print()

    # Test 4: Four matrices of the same size
    print()
    print("Test 4")
    d = [5, 5, 5, 5, 5]
    N = matrix_chain(d)
    for i in range(len(d)-1):
        for j in range(len(d)-1):
            print(N[i][j], end=" ")
        print()

    # Test 5: Five matrices
    print()
    print("Test 5")
    d = [2, 3, 4, 5, 6, 7]
    N = matrix_chain(d)
    for i in range(len(d)-1):
        for j in range(len(d)-1):
            print(N[i][j], end=" ")
        print()
