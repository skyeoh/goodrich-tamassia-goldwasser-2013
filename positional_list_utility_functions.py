# Utility functions to manipulate PositionalList objects
from positional_list import PositionalList

def print_positional_list(L):
    """Print all elements of PositionalList as a string."""
    print(", ".join([str(elem) for elem in L]))

def clear_positional_list(L):
    """Delete all elements from PositionalList."""
    pos1 = L.first()
    while len(L) > 0:
        pos2 = L.after(pos1)
        L.delete(pos1)
        pos1 = pos2

if __name__ == "__main__":
    # Test 1: print_positional_list(), clear_positional_list()
    PL = PositionalList()
    for i in range(0, 38, 2):
        PL.add_last(i)
    print("before deletion:")
    print_positional_list(PL)
    print("length =", len(PL))
    clear_positional_list(PL)
    print("after deletion:")
    print_positional_list(PL)
    print("length =", len(PL))

    # Test 2: print_positional_list(), clear_positional_list()
    print()
    PL.add_last("apple")
    PL.add_last("orange")
    PL.add_last("pear")
    PL.add_last("grapes")
    PL.add_last("watermelon")
    PL.add_last("peach")
    PL.add_last("jackfruit")
    PL.add_last("cantaloupe")
    print("before deletion:")
    print_positional_list(PL)
    print("length =", len(PL))
    clear_positional_list(PL)
    print("after deletion:")
    print_positional_list(PL)
    print("length =", len(PL))
