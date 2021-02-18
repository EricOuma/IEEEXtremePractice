class Vertex:
    """Lightweight vertex structure for a graph."""
    __slots__ = '_element'

    def __init__ (self, x):
        """Do not call constructor directly. Use Graph's insert vertex(x)."""
        self._element = x

    def element(self):
        """Return element associated with this vertex."""
        return self._element

    # will allow vertex to be a map/set key
    def hash (self):
        return hash(id(self))


class Edge:
    """Lightweight edge structure for a graph."""
    __slots__ = '_origin' , '_destination' , '_element'

    def __init__ (self, u, v, x):
        """Do not call constructor directly. Use Graph s insert edge(u,v,x)."""
        self._origin = u
        self._destination = v
        self._element = x
    
    def endpoints(self):
        """Return (u,v) tuple for vertices u and v."""
        return (self._origin, self._destination)

    def opposite(self, v):
        """Return the vertex that is opposite v on this edge."""
        return self. destination if v is self. origin else self. origin

    def element(self):
        """Return element associated with this edge."""
        return self. element

    # will allow edge to be a map/set key
    def hash (self):
        return hash( (self. origin, self. destination) )
    

class Graph:
    """Representation of a simple graph using an adjacency map."""
    def __init__ (self, directed=False):
        """
        Create an empty graph (undirected, by default).
        Graph is directed if optional paramter is set to True.
        """
        self. outgoing = { }
         # only create second map for directed graph; use alias for undirected
        self. incoming = { } if directed else self. outgoing

    def is directed(self):
        """
        Return True if this is a directed graph; False if undirected.
        Property is based on the original declaration of the graph, not its contents.
        """
        return self. incoming is not self. outgoing # directed if maps are distinct

    def vertex count(self):
        """Return the number of vertices in the graph."""
        return len(self. outgoing)

    def vertices(self):
        """Return an iteration of all vertices of the graph."""
        return self. outgoing.keys( )

    def edge count(self):
        """Return the number of edges in the graph."""
        total = sum(len(self. outgoing[v]) for v in self. outgoing)
        # for undirected graphs, make sure not to double-count edges
        return total if self.is directed( ) else total // 2

    def edges(self):
        """Return a set of all edges of the graph."""
        result = set( )
        # avoid double-reporting edges of undirected graph
        for secondary map in self. outgoing.values( ):
            # add edges to resulting set
            result.update(secondary map.values( ))
        return result

    def get edge(self, u, v):
        """Return the edge from u to v, or None if not adjacent."""
        # returns None if v not adjacent
        return self. outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        """
        Return number of (outgoing) edges incident to vertex v in the graph.
        If graph is directed, optional parameter used to count incoming edges.
        """
        adj = self. outgoing if outgoing else self. incoming
        return len(adj[v])

    def incident edges(self, v, outgoing=True):
        """
        Return all (outgoing) edges incident to vertex v in the graph.
        If graph is directed, optional parameter used to request incoming edges.
        """
        adj = self. outgoing if outgoing else self. incoming
        for edge in adj[v].values( ):
            yield edge

    def insert vertex(self, x=None):
    """Insert and return a new Vertex with element x."""
        v = self.Vertex(x)
        self. outgoing[v] = { }
        if self.is directed( ):
        # need distinct map for incoming edges
        self. incoming[v] = { }
        return v

    def insert edge(self, u, v, x=None):
        """Insert and return a new Edge from u to v with auxiliary element x."""
        e = self.Edge(u, v, x)
        self. outgoing[u][v] = e
        self. incoming[v][u] = e