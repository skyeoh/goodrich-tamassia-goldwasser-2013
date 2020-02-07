# Goodrich, Tamassia, Goldwasser (2013) Code Fragment 14.18 on page 680
from heap_priority_queue import HeapPriorityQueue
from partition import Partition

def MST_Kruskal(g):
    """Compute a minimum spanning tree of a graph using Kruskal's algorithm.

    Return a list of edges that comprise the MST.

    The elements of the graph's edges are assumed to be weights.
    """
    tree = []                                       # list of edges in spanning tree
    pq = HeapPriorityQueue()          # entries are edges in G, with weights as key
    forest = Partition()                       # keeps track of forest clusters
    position = {}                                # map each node to its Partition entry

    for v in g.vertices():
        position[v] = forest.make_group(v)

    for e in g.edges():
        pq.add(e.element(), e)              # edge's element is assumed to be its weight

    size = g.vertex_count()
    while len(tree) != size - 1 and not pq.is_empty():
        # tree not spanning and unprocessed edges remain
        weight, edge = pq.remove_min()
        u, v = edge.endpoints()
        a = forest.find(position[u])
        b = forest.find(position[v])
        if a != b:
            tree.append(edge)
            forest.union(a, b)

    return tree

if __name__ == "__main__":
