# Goodrich, Tamassia, Goldwasser (2013) Code Fragments 3.2, 3.3, 3.4 on pages 132-133

# ==== O(n**2) algorithms ====
def prefix_average1(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    n = len(S)
    A = [0]*n                                       # create new list of n zeros
    for j in range(n):
        total = 0                                     # begin computing S[0] + ... + S[j]
        for i in range(j+1):
            total += S[i]
        A[j] = total/(j+1)                       # record the average
    return A

def prefix_average2(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    n = len(S)
    A = [0]*n                                      # create new list of n zeros
    for j in range(n):
        A[j] = sum(S[0:j+1])/(j+1)       # record the average
    return A

# ==== O(n) algorithm ====
def prefix_average3(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    n = len(S)
    A = [0]*n                                      # create new list of n zeros
    total = 0                                        # compute prefix sum as S[0] + S[1] + ...
    for j in range(n):
        total += S[j]                              # update prefix sum to include S[j]
        A[j] = total/(j+1)                      # compute average based on current sum
    return A

if __name__ == "__main__":
    S = [1, 2, 3, 4, 5, 6,  7, 8, 9, 10]
    print('prefix_average1:', prefix_average1(S))
    print('prefix_average2:', prefix_average2(S))
    print('prefix_average3:', prefix_average3(S))
