
class Node(object):
    
    def __init__(self, data, next):
        self._data = data
        self._next = next
        
    def remove(self, elem):
        # case 1: found the element
        if elem == self._data:
            return self._next
        # case 2: didn't find it
        if self._next is None:
            return self
        # case 3: still looking
        self._next = self._next.remove(elem)
        return self
    
    def add_at(self, elem, ix):
        if ix < 0:
            raise ValueError("illegal list index")
        if ix == 0:
            return self.add_before(elem)
        if self._next is None:
            raise ValueError("list size exceeded")
        return self._next.add_at(elem, ix - 1)
    
    def add_before(self, elem):
        return Node(elem, self)
    
    def add_after(self, elem):
        if self._next is None:
            self._next = Node(elem, None)
        else:
            self._next = self._next.add_before(elem)
    
        
class List(object):
    
    def __init__(self):
        self._head = None
    
    def getElems(self):
        elems = []
        node = self._head
        while node is not None:
            elems.append(node._data)
            node = node._next
        return elems
    
    def add(self, elem):
        new_node = Node(elem, self._head)
        self._head = new_node
    
    def addAt(self, elem, ix):
        if self._head is None:
            if ix == 0:
                self.add(elem)
            else:
                raise ValueError("invalid index")
        else:
            self._head.add_at(elem, ix)
    
    def size(self):
        i = 0
        node = self._head
        while node is not None:
            i += 1
            node = node._next
        return i
    
    def has(self, elem):
        node = self._head
        while node is not None:
            if node._data == elem:
                return True
            node = node._next
        return False
    
    def remove(self, elem):
        if self._head is not None:
            self._head = self._head.remove(elem)
        
    def __repr__(self):
        elems = self.getElems()
        return repr(elems)
    
    
def tests():
    a = List()
    a.add(3)
    a.add('blar')
    a.add(22)
    print a, a.getElems() == [22, 'blar', 3]
    print a, a.has(2), a.has(3), a.has(4)
    return a


