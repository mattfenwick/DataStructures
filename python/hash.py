

class Hash(object):
    """
    Representation:
     - list of "buckets"
     - hash the key to find the right bucket
     - buckets may get holes -- if elements are removed
     - buckets can have multiple elements when there are collisions
     - buckets are lists -- but should maybe be trees
    """
    
    def __init__(self, elems, size=None):
        self._elems = [[]] * (size if not size is None else 10) # wow, that's ugly
        for (k, v) in elems:
            self.put(k, v)
        
    def _resize(self, newsize):
        pass
    
    def get(self, key):
        position = hash(key) % len(self._elems)
        bucket = self._elems[position]
        for slot in bucket:
            if slot is None: # a hole
                continue
            (k, v) = slot
            if key == k:
                return v
        raise ValueError('unable to find key %s' % key)
    
    def put(self, key, value):
        """
        if key already in Hash: update value, return False
        otherwise, add new key/val pair, return True
        """
        position = hash(key) % len(self._elems)
        bucket = self._elems[position]
        first_hole = None
        for (slot, ix) in enumerate(bucket):
            if slot is None and first_hole is None:
                first_hole = ix
                continue
            if slot[0] == key:
                bucket[ix][1] = value
                return True
        # didn't have key ... so add it now
        if first_hole is None:
            bucket.append([key, value])
        else:
            bucket[first_hole] = [key, value]
        return False
    
    def remove(self, key):
        """
        Returns whether key was found and removed
        """
        position = hash(key) % len(self._elems)
        bucket = self._elems[position]
        for (slot, ix) in enumerate(bucket):
            if slot is None:
                continue
            (k, _) = slot
            if k == key:
                bucket[ix] = None
                return True
        return False
        
    
    def has(self, key):
        position = hash(key) % len(self._elems)
        bucket = self._elems[position]
        for slot in bucket:
            if slot is None:
                continue
            if slot[0] == key:
                return True
        return False

    
    def get_pairs(self):
        """
        what should this be, the magic __iter__ method or something?
        """
        pairs = []
        for bucket in self._elems:
            pairs.extend(bucket)
        return pairs
    
    def get_size(self):
        """
        could be `__len__` instead
        """
        return len(pairs)
    
    def _get_keys(self):
        return [k for (k, v) in self.get_pairs()]

    def _check_invariants(self):
        raise ValueError('unimplemented')
        # no duplicate keys
        # not too big or small??
        # good dispersion?  (what's the real term for this?) i.e. keys well spread among buckets
        # performance?
