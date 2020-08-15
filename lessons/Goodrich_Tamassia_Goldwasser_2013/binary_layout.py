# Goodrich, Tamassia, Goldwasser (2013) Code Fragment 8.34 on page 347
from binary_euler_tour import BinaryEulerTour

class BinaryLayout(BinaryEulerTour):
    """Class for computing (x, y) coordinates for each node of a binary tree."""
    def __init__(self, tree):
        super().__init__(tree)                        # must call the parent constructor
        self._count = 0                                   # initialize count of processed nodes

    def _hook_invisit(self, p, d, path):
        p.element().setX(self._count)            # x-coordinate serialized by count
        p.element().setY(d)                            # y-coordinate is depth
        self._count += 1                                 # advance count of processed nodes
