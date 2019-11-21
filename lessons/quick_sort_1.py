# Goodrich, Tamassia, Goldwasser (2013) Section 12.3 on page 550
# Own implementation of the quick-sort algorithm

def quick_sort(S):
    """Sort elements of Python list S using the quick-sort algorithm."""
    n = len(S)
    if n < 2:
        return                                      # list is already sorted
    # divide
    p = S[n-1]                                   # using last element as arbitrary pivot
    L = []
    E = []
    G = []
    for i in range(n):                          # divide S into L, E and G
        if  S[i] < p:
            L.append(S[i])
        elif S[i] > p:
            G.append(S[i])
        else:                                         # last element must equal pivot
            E.append(S[i])
    # conquer (with recursion)
    quick_sort(L)                           # sort elements less than p
    quick_sort(G)                           # sort elements greater than p
    # combine by concatenating the results
    S[:] = L + E + G

if __name__ == "__main__":
    # Quick sort test 1
    S = [10, 2, -3, 5, 6, 20, 1, 0, 9, 0, -2, -2, 12, 8]
    print('Before sort:', S)
    quick_sort(S)
    print('After sort:', S)

    # Quick sort test 2
    print()
    S = [10]*8
    print('Before sort:', S)
    quick_sort(S)
    print('After sort:', S)

    # Quick sort test 3
    print()
    S = [10, 9, 8, 8, 7, 4, 2, 2, 0, -1, -9]
    print('Before sort:', S)
    quick_sort(S)
    print('After sort:', S)

    # Quick sort test 4
    print()
    print('Before sort:', S)
    quick_sort(S)
    print('After sort:', S)
