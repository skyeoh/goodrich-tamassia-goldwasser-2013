# Goodrich, Tamassia, Goldwasser (2013) Code Fragment 2.9 on page 89
from progression import Progression

class ArithmeticProgression(Progression):               # inherit from Progression
    """Iterator producing an arithmetic progression."""

    def __init__(self, increment=1, start=0):
        """Create a new arithmetic progression.

        increment    the fixed constant to add to each term (default 1)
        start             the first term of the progression (default 0)
        """
        super().__init__(start)                                           # initialize base class
        self._increment = increment

    def _advance(self):                                                    # override inherited version
        """Update current value by adding the fixed increment."""
        self._current += self._increment

if __name__ == "__main__":
    seq1 = ArithmeticProgression()
    seq1.print_progression(10)
    seq2 = ArithmeticProgression(2)
    seq2.print_progression(20)
    seq3 = ArithmeticProgression(3, 8)
    seq3.print_progression(20)
    seq4 = ArithmeticProgression(8, 10)
    for i in range(10):
        print(next(seq4))
