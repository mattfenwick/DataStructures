

class Queue(object):
    """
    Composed of two lists:
     - `_front`
     - `_back` -- backwards
    """
    
    def __init__(self, elems):
        self._front = elems
        self._back = []
    
    def unshift(self, elem):
        self._back.append(elem)
    
    def _flip(self):
        if len(self._front) != 0:
            raise ValueError("shouldn't flip a queue with a non-empty front")
        self._front = self._back[-1::-1]
        self._back = []
        
    def pop(self):
        if len(self._front) == 0:
            self._flip()
        if len(self._front) == 0:
            raise ValueError("can't pop empty Queue")
        return self._front.pop()

    def __repr__(self):
        elems = self._back[-1::-1] + self._front
        return repr(elems)
