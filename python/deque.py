
class Deque(object):
    
    def __init__(self, front=[], back=[]):
        self._front = front
        self._back = back
    
    def shift(self):
        if len(self._back) == 0:
            self._flip()
        if len(self._back) == 0:
            raise ValueError("can't shift empty deque")
        return self._back.pop()
    
    def unshift(self, elem):
        self._back.append(elem)
    
    def pop(self):
        if len(self._front) == 0:
            self._flip()
        if len(self._front) == 0:
            raise ValueError("can't pop empty deque")
        return self._front.pop()
    
    def push(self, elem):
        self._front.append(elem)
    
    def _flip(self):
        if len(self._front) != 0 and len(self._back) != 0:
            raise ValueError("can't flip deque with non-empty front and back")
        new_back = self._front[-1::-1]
        new_front = self._back[-1::-1]
        self._front = new_front
        self._back = new_back
    
    def __repr__(self):
        return repr(self._back[-1::-1] + self._front)
    