# Goodrich, Tamassia, Goldwasser (2013) Code Fragment 5.10 on page 215

def insertion_sort(A):
    """Sort list of comparable elements into nondecreasing order."""
    for k in range(1, len(A)):                     # from 1 to n-1
        cur = A[k]                                        # current element to be inserted
        j = k                                                  # find correct index j for current
        while j > 0 and A[j-1] > cur:            # element A[j-1] must be after current
            A[j] = A[j-1]
            j -= 1
        A[j] = cur                                          # cur is now in the right place

if __name__ == "__main__":
    # Insertion sort test 1
    S = [10, 2, -3, 5, 6, 20, 1, 0, 9, 0, -2, -2, 12, 8]
    print('Before sort:', S)
    insertion_sort(S)
    print('After sort:', S)

    # Insertion sort test 2
    print()
    S = [10]*8
    print('Before sort:', S)
    insertion_sort(S)
    print('After sort:', S)

    # Insertion sort test 3
    print()
    S = [10, 9, 8, 8, 7, 4, 2, 2, 0, -1, -9]
    print('Before sort:', S)
    insertion_sort(S)
    print('After sort:', S)

    # Insertion sort test 4
    print()
    print('Before sort:', S)
    insertion_sort(S)
    print('After sort:', S)
