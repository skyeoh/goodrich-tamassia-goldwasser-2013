# Goodrich, Tamassia, Goldwasser (2013) Code Fragment 10.3 on page 409
from map_base import MapBase

class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list."""

    def __init__(self):
        """Create an empty map."""
        self._table = []                                                        # list of _Item's

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error:' + repr(k))

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        for item in self._table:
            if k == item._key:                                              # Found a match:
                item._value = v                                              # reassign value
                return                                                             # and quit
       # did not find match for key
        self._table.append(self._Item(k, v))

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        for j in range(len(self._table)):
            if k == self._table[j]._key:                                 # Found a match:
                self._table.pop(j)                                            # remove item
                return                                                              # and quit
        raise KeyError('Key Error:' + repr(k))

    def __len__(self):
        """Return the number of items in the map."""
        return len(self._table)

    def __iter__(self):
        """Generate iteration of the map's keys."""
        for item in self._table:
            yield item._key                                                  # yield the KEY

if __name__ == "__main__":
    T = UnsortedTableMap()

    # Test __len__()
    print('length =', len(T))

    # Test __setitem__(), __getitem__()
    print()
    L = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    for elem in L:
        T[elem] = len(T)
    print('length =', len(T))
    for k in T.keys():
        print('T[' + str(k) +'] =', T[k])
    T['A'] = -1
    T['F'] = 9
    print('After update:')
    for k in T.keys():
        print('T[' + str(k) +'] =', T[k])

    # Test __delitem__()
    print()
    del T['B']
    del T['E']
    print('length =', len(T))
    for k in T.keys():
        print('T[' + str(k) +'] =', T[k])

    # Test __iter__()
    print()
    for key in T:
        print(key)

    # Test miscellanous
    print()
    print('A' in T)   # k in M
    print('I' in T)     # k in M

    print()
    print(T.get('A', 100))
    print(T.get('I', 100))
    for k in T.keys():
        print('T[' + str(k) +'] =', T[k])

    print()
    print(T.setdefault('A', 100))
    for k in T.keys():
        print('T[' + str(k) +'] =', T[k])
    print(T.setdefault('I', 100))
    for k in T.keys():
        print('T[' + str(k) +'] =', T[k])

    print()
    print(T.pop('I'))
    for k in T.keys():
        print('T[' + str(k) +'] =', T[k])

    print()
    print('keys: ' + ', '.join([k for k in T.keys()]))
    print('values: ' + ', '.join([str(v) for v in T.values()]))
    print('key-value pairs: ' + ', '.join(['(' + k +', ' + str(v) + ')' for (k, v) in T.items()]))

    print()
    print('Before clear: length =', len(T))
    T.clear()
    print('After clear: length = ', len(T))
