# Goodrich, Tamassia, Goldwasser (2013) Code Fragment 7.17 on page 285
# Own implementation
from positional_list_utility_functions import print_positional_list, clear_positional_list
from positional_list import PositionalList

def insertion_sort(L):
    """Sort PositionalList of comparable elements into nondecreasing order."""
    if len(L) < 2:                                  # list contains no or only one element
        return
    marker = L.first()                           # list contains more than one element
    pivot = L.after(marker)
    while pivot is not None:
        walk = marker
        cur = pivot.element()
        while walk is not None and cur < walk.element():
            L.replace(L.after(walk), walk.element())
            walk = L.before(walk)
        if walk is not None:
            L.replace(L.after(walk), cur)
        else:                                           #  insert as first element
            L.replace(L.first(), cur)
        marker = L.after(marker)
        pivot = L.after(marker)

if __name__ == "__main__":
    PL = PositionalList()

    # Insertion sort test 1
    S = [10, 2, -3, 5, 6, 20, 1, 0, 9, 0, -2, -2, 12, 8]
    for elem in S:
        PL.add_last(elem)
    print('Before sort:')
    print_positional_list(PL)
    insertion_sort(PL)
    print('After sort:')
    print_positional_list(PL)

    # Insertion sort test 2
    print()
    clear_positional_list(PL)
    for i in range(8):
        PL.add_last(10)
    print('Before sort:')
    print_positional_list(PL)
    insertion_sort(PL)
    print('After sort:')
    print_positional_list(PL)

    # Insertion sort test 3
    print()
    clear_positional_list(PL)
    S = [10, 9, 8, 8, 7, 4, 2, 2, 0, -1, -9]
    for elem in S:
        PL.add_last(elem)
    print('Before sort:')
    print_positional_list(PL)
    insertion_sort(PL)
    print('After sort:')
    print_positional_list(PL)

    # Insertion sort test 4
    print()
    print('Before sort:')
    print_positional_list(PL)
    insertion_sort(PL)
    print('After sort:')
    print_positional_list(PL)

    # Insertion sort test 5
    print()
    clear_positional_list(PL)
    PL.add_first(10)
    print('Before sort:')
    print_positional_list(PL)
    insertion_sort(PL)
    print('After sort:')
    print_positional_list(PL)

    # Insertion sort test 6: Empty list
    print()
    clear_positional_list(PL)
    print('Before sort:')
    print_positional_list(PL)
    insertion_sort(PL)
    print('After sort:')
    print_positional_list(PL)
