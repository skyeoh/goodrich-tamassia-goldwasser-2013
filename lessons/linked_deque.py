# Goodrich, Tamassia, Goldwasser (2013) Code Fragment 7.13 on page 276
from doubly_linked_base import _DoublyLinkedBase
from array_stack import Empty

class LinkedDeque(_DoublyLinkedBase):             # note the use of inheritance
    """Double-ended queue implementation based on a doubly linked list."""

    def first(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Emtpy('Deque is empty')
        return self._header._next._element                  # real item just after header

    def last(self):
        """Return (but do not remove) the element at the back of the deque."""
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._trailer._prev._element                   # real item just before trailer

    def insert_first(self, e):
        """Add an element e to the front of the deque."""
        self._insert_between(e, self._header, self._header._next)   # after header

    def insert_last(self, e):
        """Add an element e to the back of the deque."""
        self._insert_between(e, self._trailer._prev, self._trailer)     # before trailer

    def delete_first(self):
        """Remove and return the element from the front of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._header._next)     # use inherited method

    def delete_last(self):
        """Remove and return the element from the back of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._trailer._prev)     # use inherited method

if __name__ == "__main__":
    D = LinkedDeque()
    D.insert_last(5)
    D.insert_first(3)
    D.insert_first(7)
    print(D.first())
    print(D.delete_last())
    print(len(D))
    print(D.delete_last())
    print(D.delete_last())
    D.insert_first(6)
    print(D.last())
    D.insert_first(8)
    print(D.is_empty())
    print(D.last())

    print()
    print(D.delete_first())
    print(D.delete_first())
    print(len(D))
    print(D.is_empty())

    print()
    for i in range(12):
       if i < 6:
           D.insert_first(i)
           print(D.first())
       else:
           D.insert_last(i)
           print(D.last())
    print(len(D))
    print(D.is_empty())
    print(", ".join([str(D.delete_first()) for i in range(len(D))]))
    print(D.is_empty())

    print()
    for i in range(12):
        if i < 6:
            D.insert_first(i)
        else:
            D.insert_last(i)
        print('First:', D.first())
        print('Last:', D.last())
    print(len(D))
    print(D.is_empty())
    print(", ".join([str(D.delete_last()) for i in range(len(D))]))
    print(D.is_empty())

    print()
    for i in range(10):
        if i < 5:
            D.insert_first(i)
        else:
            D.insert_last(i)
    for i in range(10, 20):
        if i < 15:
            D.insert_first(i)
        else:
            D.insert_last(i)
    print(", ".join([str(D.delete_first()) for i in range(len(D))]))
    print(D.is_empty())

    print()
    for i in range(8):
       D.insert_last(i)
    print('Length =', len(D))
    for i in range(6):
        print(D.delete_first())
    print('Length =', len(D))
    for i in range(8, 15):
        D.insert_last(i)
    print('Length =', len(D))
    print(", ".join([str(D.delete_last()) for i in range(len(D))]))
    print(D.is_empty())

    print()
    for i in range(8):
       D.insert_first(i)
    print('Length =', len(D))
    for i in range(6):
        print(D.delete_last())
    print('Length =', len(D))
    for i in range(8, 15):
        D.insert_first(i)
    print('Length =', len(D))
    print(", ".join([str(D.delete_first()) for i in range(len(D))]))
    print(D.is_empty())
