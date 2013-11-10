

class List(object):
    """
    mutable linked list
    """

    def __init__(self, first, rest):
        self.first = first
        self.rest = rest

    def insert_before(self, elem):
        return List(elem, self)
    
    def insert_after(self, elem):
        new_rest = List(elem, self.rest)
        self.rest = new_rest
        return self
    
    def append(self, elem):
        self.rest = self.rest.append(elem)
        return self
    
    def remove(self, x):
        if self.first == x:
            return self.rest
        self.rest = self.rest.remove(x)
        return self
    
    def is_empty(self):
        return False
    
    def __repr__(self):
        elems = []
        node = self
        while not node.is_empty():
            elems.append(node.first)
            node = node.rest
        return repr(elems)


class Empty(object):
    
    def __init__(self):
        pass
    
    def insert_before(self, elem):
        return List(elem, self)
    
#    def insert_after(self, elem):
#        return List(elem, self) # is this right? can't insert after an empty list ... ???
    
    def append(self, elem):
        return List(elem, self)
    
    def is_empty(self):
        return True
    
    def remove(self, elem):
        return self
    
    def __repr__(self):
        return repr([])
