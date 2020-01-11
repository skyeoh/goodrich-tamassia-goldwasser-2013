# Own implementation of counting sort algorithm
def counting_sort(L):
    """Sort integers in L."""
    if len(L) < 2:      # already sorted
        return L

    minimum = min(L)
    maximum = max(L)
    size_count = maximum-minimum+1

    count =[0] * size_count             # count frequency of each item
    for item in L:
        count[item-minimum] += 1

    next_index = [0] * size_count    # compute placement index
    for i in range(1, size_count):
        next_index[i] = next_index[i-1] + count[i-1]

    sorted_list = [None] * len(L)     # place items in sorted order
    for item in L:
        sorted_list[next_index[item-minimum]] = item
        next_index[item-minimum] += 1

    return sorted_list

if __name__ == "__main__":
    # Empty list
    L = []
    print(counting_sort(L))

    # Single-item list
    L= [2]
    print(counting_sort(L))

    # Randomly-ordered list
    L = [-5, -1, -2, 7, 2, 3, 5, 3, -2, -2, 0]
    print(counting_sort(L))

    # Reverse-ordered list
    L = [7, 5, 3, 2, 2, 1, -2, -3, -3]
    print(counting_sort(L))

    # Correctly-ordered list
    print(counting_sort(L))
