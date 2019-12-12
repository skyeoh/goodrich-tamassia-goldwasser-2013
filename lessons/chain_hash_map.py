# Goodrich, Tamassia, Goldwasser (2013) Code Fragment 10.5 on page 424
from hash_map_base import HashMapBase
from unsorted_table_map import UnsortedTableMap

class ChainHashMap(HashMapBase):
    """Hash map implemented with separate chaining for collision resolution."""

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error:' + repr(k))                  # no match found
        return bucket[k]                                                        # may raise KeyError

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()                     # bucket is new to the table
        old_size = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j])  > old_size:                                 # key is new to the table
            self._n += 1                                                             # increase overall map size

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error:' + repr(k))                      # no match found
        del bucket[k]                                                                 # may raise KeyError

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:                                                # a nonempty slot
                for key in bucket:
                    yield key

if __name__ == "__main__":
    T = ChainHashMap()

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
