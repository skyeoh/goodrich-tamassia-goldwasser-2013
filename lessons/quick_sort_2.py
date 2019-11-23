# Goodrich, Tamassia, Goldwasser (2013) Code Fragment 12.6 on page 559

def inplace_quick_sort(S, a, b):
    """Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm."""
    if a >= b: return                                           # range is trivially sorted
    pivot = S[b]                                                 # last element of range is pivot
    left = a                                                         # will scan rightward
    right = b-1                                                   # will scan leftward
    while left <= right:
        # scan until reaching value equal or larger than pivot (or right marker)
        while left <= right and S[left] < pivot:
            left += 1
        # scan until reaching value equal or smaller than pivot (or left marker)
        while left <= right and pivot < S[right] :
            right -= 1
        if left <= right:                                        # scans did not strictly cross
            S[left], S[right] = S[right], S[left]                             # swap values
            left , right = left + 1, right  - 1                                   # shrink range

    # put pivot into its final place (currently marked by left index)
    S[left], S[b] = S[b], S[left]
    # make recursive calls
    inplace_quick_sort(S, a, left - 1)
    inplace_quick_sort(S, left + 1, b)

if __name__ == "__main__":
    # Quick sort test 1
    S = [10, 2, -3, 5, 6, 20, 1, 0, 9, 0, -2, -2, 12, 8]
    print('Before sort:', S)
    inplace_quick_sort(S, 0, len(S)-1)
    print('After sort:', S)

    # Quick sort test 2
    print()
    S = [10]*8
    print('Before sort:', S)
    inplace_quick_sort(S, 0, len(S)-1)
    print('After sort:', S)

    # Quick sort test 3
    print()
    S = [10, 9, 8, 8, 7, 4, 2, 2, 0, -1, -9]
    print('Before sort:', S)
    inplace_quick_sort(S, 0, len(S)-1)
    print('After sort:', S)

    # Quick sort test 4
    print()
    print('Before sort:', S)
    inplace_quick_sort(S, 0, len(S)-1)
    print('After sort:', S)
