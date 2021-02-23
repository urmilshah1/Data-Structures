class Node:
    def __init__(self, value ):
        self.value = value
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
        
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preOrder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inOrder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postOrder_print(tree.root, "")
        else:
            print("Traversal type" + str(traversal_type) + "not supported")
            return False
        
        
        
    def preOrder_print(self, start, traversal):
        #  Root-> left -> right 
        # 1->2->4->5->3->6->7->
        if start:
            traversal += (str(start.value) + "->")
            traversal = self.preOrder_print(start.left, traversal)
            traversal = self.preOrder_print(start.right, traversal)
        return traversal
                                 
    def inOrder_print(self, start, traversal):
        #Left -> root -> right
        #4->2->5->1->6->3->7->
        if start:
            traversal = self.inOrder_print(start.left, traversal)
            traversal += (str(start.value) + "->")
            traversal = self.inOrder_print(start.right, traversal)
        return traversal
    def postOrder_print(self,start, traversal):
        #left->right->root
        #4->2->5->6->3->7->1->
        if start:
            traversal = self.inOrder_print(start.left, traversal)
            traversal = self.inOrder_print(start.right, traversal)
            traversal += (str(start.value) + "->")
        return traversal
    
                                            
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)


    
print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
    
