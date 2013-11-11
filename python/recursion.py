
class Hanoi(object):
    
    def __init__(self, size):
        self.stacks = {
            'a': range(size)[-1::-1],
            'b': [],
            'c': []
        }
        self.moves = 0
    
    def _move(self, from_, to_):
        print 'before move: ', self
        f = self.stacks[from_]
        t = self.stacks[to_]
        if len(t) == 0 or f[-1] < t[-1]:
            t.append(f.pop())
            self.moves += 1
        else:
            raise ValueError('illegal move %s->%s -- %s %s' % (from_, to_, str(f), str(t)))
    
    def a_b(self):
        self._move('a', 'b')
        
    def a_c(self):
        self._move('a', 'c')
        
    def b_c(self):
        self._move('b', 'c')
        
    def b_a(self):
        self._move('b', 'a')
        
    def c_a(self):
        self._move('c', 'a')
        
    def c_b(self):
        self._move('c', 'b')
    
    def __repr__(self):
        s = self.stacks
        return repr([s['a'], s['b'], s['c'], self.moves])

# 1 a->c: 0 a->b, 1 a->c, 0 b->c
# 2 a->c: 1 a->b, 1 a->c, 1 b->c
# 3 a->c: 2 a->b, 1 a->c, 2 b->c
# 4 a->c: 3 a->b, 
def move(n, game, f_, t_, o_):
    if n == 1:
        game._move(f_, t_)
        return
    move(n - 1, game, f_, o_, t_)
    move(    1, game, f_, t_, o_)
    move(n - 1, game, o_, t_, f_)
        
def hanoi(size):
    game = Hanoi(size)
    move(size, game, 'a', 'c', 'b')
    return game
