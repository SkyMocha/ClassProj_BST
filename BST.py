class Node ():
    def __init__ (self, num, parent=None):
        self.val = num
        self.parent = parent
        self.left = None
        self.right = None
        self.traversed = False

    # def __str__(self):
    #     return str(f"{self.val} \n  l: {self.get_l_val()}\n  r: {self.get_r_val()}")
    def __str__ (self):
        return str (self.val)

    # Gets the value for the right node if it exits
    def get_l_val (self):
        if (self.left != None):
            return self.left.val
        else:
            return None
    
    # Gets the value for the right node if it exits
    def get_r_val (self):
        if (self.right != None):
            return self.right.val
        else:
            return None

    # Sets the left node
    def set_left (self, node):
        self.left = node
        return self

    # Sets the right node
    def set_right (self, node):
        self.right = node
        return self

    # def visit (self, left=True):
    #     print (self)
    #     if (self.left != None):
    #         self.left.visit()
    #     if (self.right != None):
    #         self.right.visit()

    # Checks to see if the left/right node has neither been visited previously or exists
    def l_none_or_traversed(self):
        return self.left == None or self.left.traversed
    def r_none_or_traversed(self):
        return self.right == None or self.right.traversed

class BST ():
    def __init__(self, params=-1):
        self.root = None
        if (type(params) == int):
            if (params != -1):
                self.root = Node(params)
        if (type(params) == list):
            self.root = Node (params[0])
            for i in params:
                self.add(i)
    
    # Adds a node to the tree
    def add (self, num, node=-1):
        if (self.root != None and node == -1):
            node = self.root
        elif (self.root == None):
            self.root = Node(num)
            return

        # print (f"{num}    {node.val}")
        if (num < node.val): # Checks to see if the number entered is lesser than the current nodes value
            # Checks to see if there is a left node to jump to, otherwise set the node's left value to a new node
            if (node.left != None):
                return self.add(num, node.left)
            else:
                return node.set_left(Node(num, node))

        elif (num > node.val): # Checks to see if the number entered is greater than the current nodes value
            if (node.right != None):
                return self.add(num, node.right)
            else:
                return node.set_right(Node(num, node))
        
    def someOrder (self, node=-1, l=[]):
        if (node == -1):
            node = self.root
        if (node == None):
            return l
        # Checks to see if the left node is not empty and has not been traversed
        if (node.left != None and not node.left.traversed):
            return self.someOrder( node.left, l )
        # If the left node has been added, then traverse the right if not empty
        elif (node.right != None and not node.right.traversed):
            return self.someOrder ( node.right, l )
        # If there is no left node, add the current node and traverse the parent
        else:
            l.append(str(node))
            node.traversed = True
            print (node.val)
            return self.someOrder( node.parent, l )

    # In order traversal of the binary search tree
    def traverse (self, node=-1):
        if (node == -1):
            node = self.root

        l = [] # resulted list
        if node: # if the node exists, then
            l = self.traverse(node.left) # traverse the left
            l.append (str(node)) # append the root
            l = l + self.traverse(node.right) # traverse the right
        return l

import random
# A test binary search tree with 50 values ranging from 0, 1000
def test_bst ():
    root = random.randint(0, 1000)
    tree = BST (root)
    for i in range (0, 50):
        tree.add ( random.randint(0, 1000) )
    return tree

print (test_bst().traverse())