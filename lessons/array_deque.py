# Goodrich, Tamassia, Goldwasser (2013) Exercise P-6.32 on page 253
from array_stack import Empty

class ArrayDeque:
    """Double-ended queue, or deque, implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10                                      # moderate capacity for all new deques

    def __init__(self):
        """Create an empty deque."""
        self._data = [None]*ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the deque."""
        return self._size

    def is_empty(self):
        """Return True if the deque is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[self._front]

    def last(self):
        """Return (but do not remove) the element at the back of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def add_first(self, e):
        """Add an element to the front of deque."""
        if self._size == len(self._data):
            self._resize(2*len(self._data))                              # double the array size
        self._front = (self._front - 1) % len(self._data)        # cyclic shift
        self._data[self._front] = e
        self._size += 1

    def add_last(self, e):
        """Add an element to the back of deque."""
        if self._size == len(self._data):
            self._resize(2*len(self._data))                              # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def delete_first(self):
        """Remove and return the first element of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        answer = self._data[self._front]
        self._data[self._front] = None                                   # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def delete_last(self):
        """Remove and return the last element of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        back = (self._front + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None                                             # help garbage collection
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def _resize(self, cap):
        """Resize to a new list of a different capacity."""
        old = self._data
        self._data = [None]*cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

if __name__ == "__main__":
    D = ArrayDeque()
    D.add_last(5)
    D.add_first(3)
    D.add_first(7)
    print(D.first())
    print(D.delete_last())
    print(len(D))
    print(D.delete_last())
    print(D.delete_last())
    D.add_first(6)
    print(D.last())
    D.add_first(8)
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
           D.add_first(i)
           print(D.first())
       else:
           D.add_last(i)
           print(D.last())
    print(len(D))
    print(D.is_empty())
    print(", ".join([str(D.delete_first()) for i in range(len(D))]))
    print(D.is_empty())

    print()
    for i in range(12):
        if i < 6:
            D.add_first(i)
        else:
            D.add_last(i)
        print('First:', D.first())
        print('Last:', D.last())
    print(len(D))
    print(D.is_empty())
    print(", ".join([str(D.delete_last()) for i in range(len(D))]))
    print(D.is_empty())

    print()
    print(len(D._data))
    for i in range(10):
        if i < 5:
            D.add_first(i)
        else:
            D.add_last(i)
    print(len(D._data))
    for i in range(10, 20):
        if i < 15:
            D.add_first(i)
        else:
            D.add_last(i)
    print(len(D._data))
    print(", ".join([str(D.delete_first()) for i in range(len(D))]))
    print(D.is_empty())
    print(len(D._data))

    print()
    for i in range(8):
       D.add_last(i)
    print('Length =', len(D))
    for i in range(6):
        print(D.delete_first())
    print('Length =', len(D))
    for i in range(8, 15):
        D.add_last(i)
    print('Length =', len(D))
    print(", ".join([str(D.delete_last()) for i in range(len(D))]))
    print(D.is_empty())

    print()
    for i in range(8):
       D.add_first(i)
    print('Length =', len(D))
    for i in range(6):
        print(D.delete_last())
    print('Length =', len(D))
    for i in range(8, 15):
        D.add_first(i)
    print('Length =', len(D))
    print(", ".join([str(D.delete_first()) for i in range(len(D))]))
    print(D.is_empty())
