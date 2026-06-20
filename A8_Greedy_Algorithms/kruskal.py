from collections import defaultdict

class UnionFind:
    def __init__(self):
        """self.parent is a dictionary (type: dict[str, str]) where 
            each key is a child of the value in the tree. 
            If a node is not in self.parent then its assumed to be a root.
            self.rank is a dictionary (type: dict[str, int]) where
            the value is the height of the (sub)tree at the key. 
        """
        self.parent = {}
        self.rank = {}

    def find(self, x: str) -> str:
        """Return the vertex at the root of the tree containing x.
        :param x: The vertex whos root must be found.
        :type x: str
        :return: The vertex at the root of the tree containing x.
        :rtype: str
        """
        if x not in self.parent:
            return x

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]
    
    def union(self, x: str, y: str) -> bool:
        """Merge the trees containing x and y together and return whether a merge has been done.
    
        :param x: a vertex whos tree must be merged.
        :type x: str
        :param y: a vertex whos tree must be merged.
        :type y: str
        :return: True if two trees were merged. False if x and y are already in the same tree.
        :rtype: bool
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False
        
        if root_x not in self.rank:
            self.rank[root_x] = 0
        if root_y not in self.rank:
            self.rank[root_y] = 0

        # Merge smaller tree under larger tree (union by rank)
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True
        
def kruskal(adj_list: dict[str, list[tuple[str, int]]]):
    """Implement Kruskal's algorithm to find a minimum spanning tree for the undirected graph adj_list.
            1. Sort edges by weight.
            2. Check if adding the edge with the lowest weight creates a cycle.
            3. If not add the edge to the minimum spanning tree.
        Make use of the UnionFind data structure to efficiently check whether adding an 
        edge creates a cycle.
    :param adj_list: A weighted adjecency list where the keys are vertices and the values 
        are lists of tuples of (vertex, weight) where weight denotes the weight of an 
        edge from a key vertex to a value vertex.
    :type adj_list: dict[str, list[tuple[str, int]]]
    :return: a tuple of (weight, mst_adj_list) where weight is the total edge weight of
        mst_adj_list and mst_adj_list is a minimum spanning tree for adj_list
    :rtype: tuple[int, dict[str, list[tuple[str, int]]]]
    """
    edges = []
    seen = set()
    for u in adj_list:
        for v, w in adj_list[u]:
            if (v, u) not in seen:
                edges.append((w, u, v))
                seen.add((u, v))

    edges.sort()    #sort by weight

    uf = UnionFind()
    mst = defaultdict(list)
    total_weight = 0

    for weight, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst[u].append((v, weight))
            mst[v].append((u, weight))
            total_weight += weight

    return total_weight, dict(mst)