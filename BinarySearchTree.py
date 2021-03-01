class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
    
    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left == None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right == None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("The value is already present in the tree.")
            
     
    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            else:
                return False
        else:
            print("The value does not exist in the tree.")
            
            
    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        if data == cur_node.data:
            return True
        
bst = BST()


bst.insert(10)

bst.insert(8)

bst.insert(6)

bst.insert(7)

bst.insert(3)

bst.insert(12)
    
print(bst.find(4))
    
