# Goodrich, Tamassia, Goldwasser (2013) Code Fragment 9.7 on page 385
from positional_list import PositionalList
from positional_list_utility_functions import print_positional_list, clear_positional_list
from heap_priority_queue import HeapPriorityQueue

def pq_sort(C):
    """Sort a collection of elements stored in a positional list."""
    n = len(C)
    P = HeapPriorityQueue()               # use heap implementation
    for j in range(n):
        element = C.delete(C.first())
        P.add(element, element)             # use element as key and value
    for j in range(n):
        (k, v) = P.remove_min()
        C.add_last(v)                              # store smallest remaining element in C

if __name__ == "__main__":
    C = PositionalList()
    C.add_first(1)
    C.add_first(3)
    C.add_first(2)
    C.add_first(20)
    C.add_last(-50)
    C.add_last(-50)
    C.add_last(1)
    C.add_last(4)
    print(len(C))
    print("Before sort:")
    print_positional_list(C)
    pq_sort(C)
    print("After sort:")
    print_positional_list(C)
    clear_positional_list(C)
    print_positional_list(C)

    C.add_first('B')
    C.add_first('P')
    C.add_first('C')
    C.add_first('Z')
    C.add_last('A')
    C.add_last('A')
    C.add_last('B')
    C.add_last('X')
    print(len(C))
    print("Before sort:")
    print_positional_list(C)
    pq_sort(C)
    print("After sort:")
    print_positional_list(C)
