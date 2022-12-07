class BST:
    
    class Node:
        
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else: 
            self._insert(data, self.root)
        
    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = BST.Node(data)
            else:
                self._insert(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = BST.Node(data)
            else:
                self._insert(data, node.right)
                
    def get_height(self):
            """
            Determine the height of the BST.              
            If the tree is empty, then return 0.  Otherwise, call 
            _get_height on the root which will recursively determine the 
            height of the tree.
            """
            if self.root is None:
                return 0
            else:
                return self._get_height(self.root)  # Start at the root
            
    def _get_height(self, node):
        if node == None:
            return 0
        else:
            height_left = self._get_height(node.left)
            height_right = self._get_height(node.right)
            max_value = max(height_left + 1, height_right + 1)
            return max_value
    

tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(10)
tree.insert(12)
tree.insert(8)
tree.insert(1)
for x in tree:
    print(x) # 1, 3, 5, 7, 8, 10, 12

print(tree.get_height()) # 4
tree.insert(14)
print(tree.get_height()) # 5
tree.insert(0)
print(tree.get_height()) # 5
tree.insert(4)