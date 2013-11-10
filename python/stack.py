

class Stack(object):

    def __init__(self, first, rest):
        self.first = first
        self.rest = rest

    def is_empty(self):
        return False
 
    def pop(self):
        return self.rest

    def get_first(self):
        return self.first


class EmptyStack(object):

    def __init__(self):
        pass

    def is_empty(self):
        return True

    def pop(self):
        raise ValueError("can't pop empty stack")

    def get_first(self):
        raise ValueError("can't get first element of empty stack")


matches = {
    '{': '}',
    '[': ']',
    '(': ')',
    '<': '>',
    '-': '+',
    'u': 'i'
}

opens = set(matches.keys())
closes = dict([(v, k) for (k, v) in matches.items()])

def is_balanced(elems):
    stack = EmptyStack()
    for (ix, e) in enumerate(elems, start=1):
        if e in opens:
            stack = Stack(e, stack)
        elif e in closes:
            if stack.is_empty():
                raise ValueError("unmatched close %s at position %d" % (e, ix))
            if closes[e] == stack.get_first():
                stack = stack.pop()
            else:
                raise ValueError("mismatched open %s and close %s at position %d" % (stack.get_first(), e, ix))
        else:
            raise ValueError('unrecognized element -- ' + str(e))
    if not stack.is_empty():
        raise ValueError('unmatched opens at end of input.  last: %s' % stack.get_first())
    return True


class Stack2(object):
    """
    mutable stack
    """
    
    def __init__(self, elems):
        self._elems = elems
        for x in elems:
            self.push(x)
    
    def push(self, x):
        self._elems.append(x)
    
    def pop(self):
        if self.is_empty():
            raise ValueError("can't pop empty stack")
        return self._elems.pop()
    
    def peek(self):
        if self.is_empty():
            raise ValueError("can't peeak at empty stack")
        return self._elems[-1]
    
    def __len__(self):
        return len(self._elems)
    
    def is_empty(self):
        return len(self) == 0
    
    def __repr__(self):
        return '<bottom> ' + repr(self._elems) + ' <top>'



def postfix(elems):
    ops = set('+-*/?')
    st = Stack2([])
    for e in elems:
        if e in ops:
            right = st.pop()
            left = st.pop()
            st.push({'left': left, 'right': right, 'op': e})
        else:
            st.push(e)
    if len(st) != 1:
        raise ValueError('too many values')
    return st.peek()


def tree_to_postfix(tree):
    if isinstance(tree, dict):
        elems = tree_to_postfix(tree['left'])
        elems.extend(tree_to_postfix(tree['right']))
        elems.append(tree['op'])
        return elems
    return [tree]
