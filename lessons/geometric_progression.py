# Goodrich, Tamassia, Goldwasser (2013) Code Fragment 2.10 on page 90
from progression import Progression

class GeometricProgression(Progression):                        # inherit from Progression
    """Iterator producing a geometric progression."""

    def __init__(self, base=2, start=1):
        """Create a new geometric progression.

        base            the fixed constant multiplied to each term (default 2)
        start            the first term of the progression (default 1)
        """
        super().__init__(start)
        self._base = base

    def _advance(self):                                                         # override inherited version
        """Update current value by multiplying it by the base value."""
        self._current *= self._base

if __name__ == "__main__":
    seq1 = GeometricProgression()
    seq1.print_progression(10)
    seq2 = GeometricProgression(3)
    seq2.print_progression(8)
    seq3 = GeometricProgression(5, 10)
    seq3.print_progression(10)
    seq4 = GeometricProgression(3, 4)
    print(' '.join([str(seq4.__next__()) for i in range(8)]))
