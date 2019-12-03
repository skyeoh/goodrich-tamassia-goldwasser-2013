# Goodrich, Tamassia, Goldwasser (2013) Code Fragment 7.14-7.16 on pages 282-284
from doubly_linked_base import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    #-------------------------- nested Position class --------------------------
    class Position:
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def  __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)                    # opposite of __eq__

    #------------------------------- utility method -------------------------------
    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if  p._node._next is None:                  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None                                     # boundary violation
        else:
            return self.Position(self, node)        # legitimate position

    #------------------------------- accessors -------------------------------
    def first(self):
        """Return the first Position in the list (or None if list is empty)."""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last Position in the list (or None if list is empty)."""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return the Position just before Position p (or None if p is first)."""
        node = self._validate(p)
        return self._make_position (node._prev)

    def after(self, p):
        """Return the Position just after Position p (or None if p is last)."""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    #------------------------------- mutators -------------------------------
    # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return new Position."""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element e into list after Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original)       # inherited method returns element

    def replace(self, p, e):
        """Replace the element at Position p with e.

        Return the element formerly at Position p.
        """
        original = self._validate(p)
        old_value = original._element             # temporarily store old element
        original._element = e                           # replace with new element
        return old_value                                   # return the old element value

if __name__ == "__main__":
    # Test add_first(), add_last(), __len__(), __iter__()
    P = PositionalList()
    P.add_first(2)
    P.add_first(1)
    P.add_last(3)
    P.add_last(4)
    print(len(P))
    print(", ".join([str(elem) for elem in P]))

    # Test __iter__()
    print()
    gen = iter(P)
    for i in range(len(P)):
        print(gen.__next__())

    # Test first(), last(), Position.element()
    print()
    print(type(P.first()))
    print(P.first().element())
    print(type(P.last()))
    print(P.last().element())

    # Test Position.__eq__(), Position.__ne__()
    print()
    print(P.first() == P.last())    # False
    print(P.first() != P.last())     # True

    # Test before(), after(), Position.__eq__(), Position.__ne__()
    print()
    pos = P.first()
    for i in range(len(P)):
        print('i =', i, ' elem =', pos.element())
        print('Current pos. first?', P.first() == pos, '| Current pos. not first?', P.first() != pos)
        print('Current pos. last?', P.last() == pos, '| Current pos. not last?', P.last() != pos )
        print('Current pos. after?', P.after(pos) == pos, '| Current pos. not after?', P.after(pos) != pos)
        pos = P.after(pos)

    pos = P.last()
    for i in range(len(P)):
        print('i =', i, ' elem =', pos.element())
        pos = P.before(pos)

    # Test add_before(), add_after()
    print()
    insertion_pos = 3
    pos = P.first()
    for i in range(insertion_pos-1):
        pos = P.after(pos)
        print(pos.element())
    P.add_before(pos, 2.5)
    P.add_after(pos, 3.5)
    print("new length = ", len(P))
    print(", ".join([str(elem) for elem in P]))

    pos = P.first()
    first_elem = pos.element()
    for i in range(3):
        pos = P.add_after(pos, first_elem + 0.25*(i+1))
    print("new length = ", len(P))
    print(", ".join([str(elem) for elem in P]))

    pos = P.last()
    last_elem = pos.element()
    for i in range(3):
        pos = P.add_before(pos, last_elem - 0.1*(i+1))
    print("new length = ", len(P))
    print(", ".join([str(elem) for elem in P]))

    # Test replace()
    print()
    replace_pos = 9
    pos = P.first()
    for i in range(replace_pos-1):
        pos = P.after(pos)
        print(pos.element())
    print("before replace: length =", len(P))
    print("old value = ", P.replace(pos, 3.65))
    print("after replace: length =", len(P))
    print(", ".join([str(elem) for elem in P]))

    # Test delete()
    print()
    pos = P.last()
    print("before delete: length =", len(P))
    print(P.delete(pos))
    print("after delete: length =", len(P))

    delete_pos = 4
    pos = P.last()
    for i in range(len(P)-delete_pos):
        pos = P.before(pos)
        print(pos.element())
    print("before delete: length =", len(P))
    print(P.delete(pos))
    print("after delete: length =", len(P))
    print(", ".join([str(elem) for elem in P]))
