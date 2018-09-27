class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self, root):
        self.root = Node(root)
    
    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder(self.root, '')
        elif traversal_type == 'inorder':
            return self.inorder(self.root, '')
        elif traversal_type == 'postorder':
            return self.postorder(self.root, '')
        else:
            print('Incorrect traversal type')
            return False
    
    def preorder(self, start, traversal):
        """ parent node -> left child -> right child  """
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal
        
    def inorder(self, start, traversal):
        """ left child -> parent node -> right child """
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder(start.right, traversal)
        return traversal

    def postorder(self, start, traversal):
        """ left child -> right child -> parent node """
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal += (str(start.value) + '-')
        return traversal


# Set up below tree
#       A
#      / \
#     B   C
#    / \   \
#   D   E   G
#          / \
#         F   H

tree = BinaryTree('A')
tree.root.left = Node('B')
tree.root.left.left = Node('D')
tree.root.left.right = Node('E')
tree.root.right = Node('C')
tree.root.right.right = Node('G')
tree.root.right.right.left = Node('F')
tree.root.right.right.right = Node('H')

print('Preorder  (parent node -> left child  -> right child ): ',tree.print_tree('preorder'))
print('Inorder   (left child  -> parent node -> right child ): ',tree.print_tree('inorder'))
print('Postorder (left child  -> right child -> parent node ): ',tree.print_tree('postorder'))