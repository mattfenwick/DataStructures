

class BinTree(object):
    
    def __init__(self, val, left=None, right=None):
        self._val = val
        self._left = left
        self._right = right
    
    def flatten(self):
        l = self._left.flatten() if self._left is not None else []
        r = self._right.flatten() if self._right is not None else []
        return l + [self._val] + r
    
    def preorder(self):
        l = self._left.preorder() if self._left is not None else []
        r = self._right.preorder() if self._right is not None else []
        return [self._val] + l + r
    
    def inorder(self):
        l = self._left.inorder() if self._left is not None else []
        r = self._right.inorder() if self._right is not None else []
        return l + [self._val] + r
    
    def postorder(self):
        l = self._left.postorder() if self._left is not None else []
        r = self._right.postorder() if self._right is not None else []
        return l + r + [self._val]
    
    def traverse1(self):
        """
        seems to be breadth-first
        """
        nodes, ix = [self], 0
        while ix < len(nodes):
            node = nodes[ix]
            if node._left is not None:
                nodes.append(node._left)
            if node._right is not None:
                nodes.append(node._right)
            ix += 1
        return nodes
    
    def traverse2(self):
        """
        i don't know what this is?
        """
        nodes, ix = [self], 0
        while ix < len(nodes):
            node = nodes[ix]
            if node._right is not None:
                nodes.append(node._right)
            if node._left is not None:
                nodes.append(node._left)
            ix += 1
        return nodes[-1::-1]
    
    def traverse3(self):
        nodes = [self]
        um = []
        while True:
            um.append(nodes[-1])
            if nodes[-1]._left is not None:
                nodes.append(nodes[-1]._left)
            elif nodes[-1]._right is not None:
                nodes.append(nodes[-1]._right)
            else:
                nodes.pop()
        return um
    
    def traverse4(self):
        """
        looks like iterative depth first
        """
        nodes, well = [self], [[0, 0]]
        um = [self]
        while len(nodes) > 0:
            if well[-1][0] == 0:
                well[-1][0] = 1 # okay, so done the left for this node
                if nodes[-1]._left is not None:
                    nodes.append(nodes[-1]._left)
                    well.append([0, 0])
                    um.append(nodes[-1])
                    continue
                # else -- fall through
            elif well[-1][1] == 0:
                well[-1][1] = 1
                if nodes[-1]._right is not None:
                    nodes.append(nodes[-1]._right)
                    well.append([0, 0])
                    um.append(nodes[-1])
                    continue
                # else -- fall through
            else:
                # both sides done -- so pop
                nodes.pop()
                well.pop()
        return um
    
    def traverse5(self):
        """
        looks like depth first
        """
        st1 = [self]
        st2 = []
        while len(st1) > 0:
            node = st1.pop()
            st2.append(node)
            if node._right is not None:
                st1.append(node._right)
            if node._left is not None:
                st1.append(node._left)
        return st2
    
    def traverse6(self):
        """
        intended to be iterative postorder ... I think
        """
        st = [[self, False]]
        um = []
        while len(st) > 0:
            if not st[-1][1]:
                node = st[-1][0]
                st[-1][1] = True
                if node._right is not None:
                    st.append([node._right, 0])
                if node._left is not None:
                    st.append([node._left, 0])
            else:
                um.append(st[-1][0])
                st.pop()
        return um
    
    def traverse7(self):
        """
        should be iterative inorder
        """
        st = [[self, 0]]
        um = []
        while len(st) > 0:
            node = st[-1][0]
            if st[-1][1] == 0:
                st[-1][1] = 1
                if node._left is not None:
                    st.append([node._left, 0])
            elif st[-1][1] == 1:
                st[-1][1] = 2
                um.append(node)
                st.pop()
                if node._right is not None:
                    st.append([node._right, 0])
            else:
                raise ValueError('oops')
        return um
        
    def iter_flatten(self):
        nodes = [self]
        node = self
        while len(nodes) > 0:
            pass

    def toStr(self, depth=0):
        lines = []
        if self._right is not None:
            lines.append(self._right.toStr(depth + 1))
        lines.append((' ' * depth * 2) + '**  ' + str(self._val))
        if self._left is not None:
            lines.append(self._left.toStr(depth + 1))
        return '\n'.join(lines)

    def __repr__(self):
        return self.toStr()

def getVal(n):
    return n._val

B = BinTree

eg1 = B(3, 
        B(4, B(8), B('poop')), 
        B('hi'))

eg2 = B('a', 
        B('b', B('c')), 
        B('d', B('e'), B('f')))

eg3 = B('10',
        B('22', 
          B('34'),
          B('89')),
        B('101',
          B('17',
            B('99'),
            B('1')),
          B('33',
            None,
            B('27'))))
