class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: int
    # item: int
    # size: int
    def __init__(self, debugger = None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

    @property
    def size(self):
         return self._size
       
     # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Part a #######
    '''
    Calculates the size of the tree
    returns the size at a given node
    '''
    def calculate_sizes(self, debugger = None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size

    '''
    Select the ind-th key in the tree
    
    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    '''
    def select(self, ind):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size
        if ind == left_size:
            return self
        elif ind < left_size and self.left is not None:
            return self.left.select(ind)
        elif ind > left_size and self.right is not None:
            return self.right.select(ind - left_size - 1) # FIXED: correctness, when recursing to the right subtree, must skip the left subtree and current vertex
        return None

    '''
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    '''
    # No fix needed, correct and efficient
    def search(self, key):
        if self is None:
            return None
        elif self.key == key:
            return self
        elif self.key < key and self.right is not None:
            return self.right.search(key)
        elif self.left is not None:
            return self.left.search(key)
        return None

    '''
    Inserts a key into the tree
    key: the key for the new node; 
        ... this is NOT a BinarySearchTree/Node, the function creates one
    
    returns the original (top level) tree - allows for easy chaining in tests
    '''
    def insert(self, key):
        if self.key is None:
            self.key = key
        elif self.key > key: 
            if self.left is None:
                self.left = BinarySearchTree(self.debugger)
            self.left.insert(key)
        elif self.key < key:
            if self.right is None:
                self.right = BinarySearchTree(self.debugger)
            self.right.insert(key)

        l_size = 0
        r_size = 0
        if self.left is not None:
            l_size = self.left.size
        if self.right is not None:
            r_size = self.right.size
        self.size = 1 + l_size + r_size
        # self.calculate_sizes()            FIXED: removed line here and kept track of sizes throughout insert to reduce recalculating entire tree
        return self

    
    ####### Part b #######

    '''
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)
    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on
    Returns: the root of the tree/subtree
    Example:
    Original Graph
      10
       \
        11
          \
           12
    
    Execute: NodeFor10.rotate("L", "R") -> Outputs: NodeFor10
    Output Graph
      10
        \
        12
        /
       11 
    '''
    def rotate(self, direction, child_side):
        # Your code goes here
        def calc_size(v):
            if v is not None:
                size = 1
            else:
                size = 0
            if v.left is not None:
                size += v.left.size
            if v.right is not None:
                size += v.right.size
            return size

        def rotate_left(v):
            if v is None or v.right is None:
                return v
            y = v.right
            temp = y.left
            y.left = v
            v.right = temp
            v.size = calc_size(v)
            y.size = calc_size(y)
            return y
        
        def rotate_right(v):
            if v is None or v.left is None:
                return v
            y = v.left
            temp = y.right
            y.right = v
            v.left = temp
            v.size = calc_size(v)
            y.size = calc_size(y)
            return y

        if direction == "L":
            if child_side == "R":
                self.right = rotate_left(self.right)
            elif child_side == "L":
                self.left = rotate_left(self.left)
            else:
                raise ValueError
        elif direction == "R":
            if child_side == "R":
                self.right = rotate_right(self.right)
            elif child_side == "L":
                self.left = rotate_right(self.left)
            else:
                raise ValueError
        else:
            raise ValueError

        self.size = calc_size(self)
        return self

    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print( self.key),
        if self.right is not None:
            self.right.print_bst()
        return self