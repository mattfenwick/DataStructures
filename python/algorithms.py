from collections import Counter
import cProfile
import pstats


def profile(f, *args, **kwargs):
    cProfile.runctx('f(*args, **kwargs)', {}, {'f': f, 'args': args, 'kwargs': kwargs}, 'prof.txt')
    stats = pstats.Stats('prof.txt')
    stats.sort_stats('time').print_stats()
    return stats



def ana1(a, b):
    """
    seems to run in O(n*log(n))
    """
    return sorted(a) == sorted(b)


def ana2(a, b):
    """
    seems to run in O(n)
    """
    s1 = Counter(a)
    s2 = Counter(b)
    return s1 == s2


def binary_search(seq, elem):
    """
    assumes seq is sorted
    
    this seems to have some major boundary issues
    """
    bottom, top = 0, len(seq)
    while bottom < (top - 1):
        ix = bottom + (top - bottom) / 2
        print bottom, top, ix
        if seq[ix] == elem:
            return True
        elif seq[ix] < elem:
            bottom = ix
        else: # seq[ix] > elem
            top = ix
    return seq[ix] == elem


def hmm(xs):
    return lambda x: (x, binary_search(xs, x))


def reverse(xs):
    if len(xs) == 0:
        return []
    fst, rst = xs[0], xs[1:]
    rev = reverse(rst)
    rev.append(fst)
    return rev
