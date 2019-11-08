# Goodrich, Tamassia, Goldwasser (2013) Code Fragment 2.5 on page 79
class SequenceIterator:
    """An iterator for any of Python's sequence types."""

    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence              # keep a reference to the underlying data
        self._k = -1                      # will increment to 0 on first call to next

    def  __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self._k += 1                      # advance to next index
        if self._k < len(self._seq):
            return(self._seq[self._k])    # return the data element
        else:
            raise StopIteration()         # there are no more elements

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self

if __name__ == "__main__":
    sequence = SequenceIterator((1, 4, "apple", -3, [1, 2, "I love cats"], (2.4, -1)))
    print(dir(sequence))

    for element in sequence:
        print(element)
