# Code for Binary Search Tree


# Depth First Search (DFS)
# 1. Create a Stack
# 2. Add the root to the Stack
# 3. If the Stack is not empty pop the
#    node from the Stack and make it the
#    current node.
# 4. If the current node is not None 
#    print the data and add the right child
#    and then the left child of the current
#    node to the Stack.
# 5. Repeat steps 3 and 4 until the Stack
#    is empty.

# Breadth First Search (BFS)
# 1. Create a Queue
# 2. Add the root to the Queue
# 3. If the Queue is not empty remove a node
#    from the Queue and make it the current
#    node.
# 4. If the current node is not None print 
#    the data and add the left child and then
#    the right child of the current node to the
#    Queue.
# 5. Repeat steps 3 and 4 until Queue is empty.



class Node(object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None
    # self.parent = None
    # self.visited = False

class Tree (object):
  def __init__ (self):
    self.root = None


# insert data into the tree
  def insert (self, data):
    new_node = Node (data)

    if (self.root == None):
      self.root = new_node
      return
    else:
      currnt = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (data < current.data):
          current = current.lchild
        else:
          current = current.rchild
      if (data < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node


# search for a node with a given node
  def search (self, data):
    current = self.root
    while (current != None) and (current.data != data):
      if (data < current.data):
        current = current.lchild
      else:
        current = current.rchild
    return current
  
  # in-order traversal (recursive) = left, center, right
  def in_order (self, aNode):
    if (aNode != None):
      self.in_order (aNode.lchild)
      print(aNode.data)
      self.in_order(aNode.rchild)
    # it is a base case, but unnecessary
    else:
      pass


  # find the minimum
  def find_min (self):
    current = self.root
    if current == None:
      return None

    while (current.lchild != None):
      current = current.lchild
    return current

  # find the node with the maximum key
  def find_max (self):
    current = self.root
    parent = self.root
    while (current != None):
      parent = current
      current = current.rchild
    return parent

  # in order traversal - left, center, right
  def in_order (self, aNode):
    if (aNode != None):
      self.in_order (aNode.lchild)
      print (aNode.data)
      self.in_order (aNode.rchild)

  # pre order traversal - center, left, right
  def pre_order (self, aNode):
    if (aNode != None):
      print (aNode.data)
      self.pre_order (aNode.lchild)
      self.pre_order (aNode.rchild)

  # post order traversal - left, right, center
  def post_order (self, aNode):
    if (aNode != None):
      self.post_order (aNode.lchild)
      self.post_order (aNode.rchild)
      print (aNode.data)


# * Deletion of a Node from a Binary Search Tree. Three cases to
#   consider:
#   1. Leaf Node
#   2. Node with one child
#   3. Node with two children
#   Case 1: Find out if the delete node is the left child or right
#           child of its parent. Make the left child or the right
#           child of the parent None.

#   Case 2: Find out if the delete node is the left child or right
#           child of its parent. Attach the child of the delete node
#           to the left child or right child of the parent.

#   Case 3: Find the successor node. The successor node is the node
#           that comes immediately after the delete node during an
#           inorder traversal. Think of the successor node as the
#           minimum node in the right sub-tree of the delete node.
#           The successor node will not have a left child but may
#           have a right child. 
#           Replace the delete node with the successor node.
#           Attach the left child of the delete node to the successor
#           Attach the right child of the successor node as the left
#           child of the successor's parent.
#           Attach the right child of the delete node as the right
#           child of the successor node.
  #  succession node is the next node of the deleted note in_order traversal
  # Delete a node with a given key
  def delete (self, key):
    deleteNode = self.root
    parent = self.root
    isLeft = False

    # If empty tree
    if (deleteNode == None):
      return False

    # Find the delete node
    while ((deleteNode != None ) and (deleteNode.data != key)):
      parent = deleteNode
      if (key < deleteNode.data):
        deleteNode = deleteNode.lChild
        isLeft = True
      else:
        deleteNode = deleteNode.rChild
        isLeft = False
      
    # If node not found
    if (deleteNode == None):
      return False

    # Delete node is a leaf node
    if ((deleteNode.lChild == None) and (deleteNode.rChild == None)):
      if (deleteNode == self.root):
        self.root = None
      elif (isLeft):
        parent.lChild = None
      else:
        parent.rChild = None

    # Delete node is a node with only left child
    elif (deleteNode.rChild == None):
      if (deleteNode == self.root):
        self.root = deleteNode.lChild
      elif (isLeft):
        parent.lChild = deleteNode.lChild
      else:
        parent.rChild = deleteNode.lChild

    # Delete node is a node with only right child
    elif (deleteNode.lChild == None):
      if (deleteNode == self.root):
        self.root = deleteNode.rChild
      elif (isLeft):
        parent.lChild = deleteNode.rChild
      else:
        parent.rChild = deleteNode.rChild

    # Delete node is a node with both left and right child
    else:
      # Find delete node's successor and successor's parent nodes
      successor = deleteNode.rChild
      successorParent = deleteNode

      while (successor.lChild != None):
        successorParent = successor
	successor = successor.lChild

      # Successor node right child of delete node
      if (deleteNode == self.root):
        self.root = successor
      elif (isLeft):
        parent.lChild = successor
      else:
        parent.rChild = successor

      # Connect delete node's left child to be successor's left child
      successor.lChild = deleteNode.lChild

      # Successor node left descendant of delete node
      if (successor != deleteNode.rChild):
        successorParent.lChild = successor.rChild
        successor.rChild = deleteNode.rChild

    return True