# Goodrich, Tamassia, Goldwasser (2013) Code Fragments 8.29-8.32 on pages 344-345
from euler_tour import EulerTour

class PreorderPrintIndentedTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        print(2*d*' ' + str(p.element()))

class PreorderPrintIndentedLabeledTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        label = '.'.join(str(j+1) for j in path)           # labels are one-indexed
        print(2*d*' ' + label, p.element())

class ParenthesizeTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        if path and path[-1] > 0:                             # p follows a sibling
            print(', ', end=' ')                                     # so preface with comma
        print(p.element(), end=' ')                          # then print element
        if not self.tree().is_leaf(p):                         # if p has children
            print(' (', end=' ')                                     # print opening parenthesis

    def _hook_postvisit(self, p, d, path, results):
        if not self.tree().is_leaf(p):                          # if p has children
            print(')', end=' ')                                       # print closing parenthesis

class DiskSpaceTour(EulerTour):
    def _hook_postvisit(self, p, d, path, results):
        # we simply add space associated with p to that of its subtrees
        return p.element().space() + sum(results)

if __name__ == "__main__":
