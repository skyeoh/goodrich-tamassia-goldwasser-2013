def array_binary_search(A, element):
    """Search for element in an array using binary search."""

    n = len(A)
    sorted_array = sorted(A)    # sort array
    start = 0
    end = n-1
    mid = (start + end) // 2
    while start <= end:
        if sorted_array[mid] == element:
            return True                 # search is successful
        elif sorted_array[mid] < element:   # element can only be present in right subarray
            start = mid+1
        else:                                                 # element can only be present in left subarray
            end = mid-1
        mid = (start + end) // 2
    return False                        # search is unsuccessful

if __name__ == "__main__":
    A = [1]
    print(array_binary_search(A, 0))
    print(array_binary_search(A, 1))
    print(array_binary_search(A, 200))
    print(A)

    print()
    A = [-20, 8]
    print(array_binary_search(A, 8))
    print(array_binary_search(A, -20))
    print(array_binary_search(A, 14))
    print(array_binary_search(A, -22))
    print(array_binary_search(A, 2))
    print(A)

    print()
    A = [4, 1, 7, 9, 5, -100, 20, -200, -200, 300]
    print(array_binary_search(A, 8))
    print(array_binary_search(A, -200))
    print(array_binary_search(A, -209))
    print(array_binary_search(A, 9))
    print(array_binary_search(A, 300))
    print(array_binary_search(A, -100))
    print(array_binary_search(A, -302))
    print(array_binary_search(A, 1002))
    print(A)
