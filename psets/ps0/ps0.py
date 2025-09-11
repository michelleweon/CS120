#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        """
        :param root: the root of the binary tree
        """
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        """
        :param: the key associated with the vertex of the binary tree
        """
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None


#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    # Your code goes here

    # check left child exists
    if v.left == None:
        left_size = 0
    else:
        # calc size if not alr
        if v.left.size == None:
            left_size = calculate_sizes(v.left).size

    # check right child exists
    if v.right == None:
        right_size = 0
    else:
        # calc size if not alr
        if v.right.size == None:
            right_size = calculate_sizes(v.right).size

    v.size = 1 + left_size + right_size

    return v

#
# Problem 1c
#

# Input: a positive integer t, 
# ...BTvertex v, the root of a BinaryTree of size n >= 1
# Output: BTvertex, descendent of v such that its size is between 
# ... t and 2t (inclusive)
# Runtime: O(h) 

def FindDescendantOfSize(t, v):
    u = v
    while True:
        if t <= u.size <= 2*t:
            return u

        heavy = None     
        candidate = None  

        for c in (u.left, u.right):
            if c is None:
                continue
            if c.size is None:
                raise ValueError("Tree must be size-augmented (child.size is None).")
            if c.size > 2*t:
                heavy = c
                break                  
            if c.size >= t:
                candidate = c        

        if heavy is not None:
            u = heavy
            continue

        if candidate is not None:
            return candidate

        # If we reach here, both children (if any) are < t, which contradicts
        raise RuntimeError("No valid descendant found; check preconditions.")