

class Directed(object):
    
    def __init__(self, vertices, edges):
        self._vertices = set(vertices)
        self._edges = []
        for (a, b) in edges:
            if not (a in self._vertices and b in self._vertices):
                raise ValueError('graph edge must be between nodes')
            self._edges.append((a,b))
