# Goodrich, Tamassia, Goldwasser (2013) Code Fragments 12.1, 12.2 on pages 543-544

def merge(S1, S2, S):
    """Merge two sorted Python lists S1 and S2 into properly sized list S."""
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]                       # copy ith element of S1 as next item of S
            i += 1
        else:
            S[i+j] = S2[j]                       # copy jth element of S2 as next item of S
            j += 1

def merge_sort(S):
    """Sort the elements of Python list S using the merge-sort algorithm."""
    n = len(S)
    if n < 2:
        return                                      # list is already sorted
    # divide
    mid = n // 2
    S1 = S[0:mid]                            # copy of first half
    S2 = S[mid:n]                            # copy of second half
    # conquer (with recursion)
    merge_sort(S1)                          # sort copy of first half
    merge_sort(S2)                          # sort copy of second half
    # combine by merging results
    merge(S1, S2, S)                        # merge sorted halves back into S

if __name__ == "__main__":
    # Merge test 1
    S1 = [0, 2, 4, 6, 8, 11, 13, 15, 17, 19, 21, 21]
    S2 = [1, 3, 5, 7, 9, 10, 12, 14, 16, 18, 19, 20, 22, 23]
    S = [None]*(len(S1)+len(S2))
    print('Before merge:')
    print('S1 = ', S1)
    print('S2 = ', S2)
    print('S = ', S)
    merge(S1, S2, S)
    print('After merge:')
    print('S1 = ', S1)
    print('S2 = ', S2)
    print('S = ', S)

    # Merge test 2
    print()
    S1 = [0, 1, 2, 4, 7]
    S2 = [7, 10, 12, 18]
    S = [None]*(len(S1)+len(S2))
    print('Before merge:')
    print('S1 = ', S1)
    print('S2 = ', S2)
    print('S = ', S)
    merge(S1, S2, S)
    print('After merge:')
    print('S1 = ', S1)
    print('S2 = ', S2)
    print('S = ', S)

    # Merge test 3
    print()
    S = [None]*(len(S1)+len(S2))
    print('Before merge:')
    print('S1 = ', S2)
    print('S2 = ', S1)
    print('S = ', S)
    merge(S2, S1, S)
    print('After merge:')
    print('S1 = ', S2)
    print('S2 = ', S1)
    print('S = ', S)

    # Merge sort test 1
    print()
    S = [10, 2, -3, 5, 6, 8, 1, 0, 9, 0, -2, -2, 12, 20]
    print('Before sort:', S)
    merge_sort(S)
    print('After sort:', S)

    # Merge sort test 2
    print()
    S = [10]*8
    print('Before sort:', S)
    merge_sort(S)
    print('After sort:', S)

    # Merge sort test 3
    print()
    S = [10, 9, 8, 8, 7, 4, 2, 2, 0, -1, -9]
    print('Before sort:', S)
    merge_sort(S)
    print('After sort:', S)

    # Merge test 4
    print()
    print('Before sort:', S)
    merge_sort(S)
    print('After sort:', S)
