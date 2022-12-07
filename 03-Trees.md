# Using Trees is Python

Welcome to the Trees tutorial!

A **tree** is structure used in programming that links nodes together by pointers. 

## Structure of a Tree 
The top node is called the **root**. A node that has other connected nodes under it is called a **parent**. The nodes under the parent nodes are **child** nodes. A **leaf** is a node that has no other connecting nodes under it. The nodes to the left and right of a parent node are called **subtrees**.

## Binary Search Trees (BST)
When data gets placed into the tree, it is first compared to the value in the parent node. If the data being added is less than the parent node, it will go on to be compared to the next node on the left. If it is greater, it continues down the subtree on the right. It will continue to search and go left or right until there is an open space for the data to be placed.

## Balanced Trees
Trees are called **balanced** when the height of any subtree isn't dramatically different than the other. A tree becomes unbalanced when one subtree is 2 or more nodes longer than the other subtree connected to their parent node.

## BST Operations
### Inserting Recursively
> Smaller problem: Insert a value into a tree by traversing the left or right subtree.

> Base case: Once an empty spot is found, the item can be inserted.

Here's how to insert into a BST:
```Python
def insert(self, data):
    """
    Insert 'data' into the BST. If the BST is empty, then set the root equal to the new mode. Otherwise, use _insert to recursively find the next empty spot to insert.
    """
    if self.root is None:
        self.root = BST.Node(data)
    else:
        self._insert(data, self.root) #Start at the root

def _insert(self, data, node):
    """
    _insert() looks for a place to insert a node with 'data' inside of it. Current subtree = 'node'. This function is intended to be called the first time by the insert function.
    """
    if data < node.data:
        # Lower data belongs on the left side.
        if node.left is Non:
            # We found an empty spot
            node.left = BST.Node(data)
        else:
            # Need to keep looking. Call _insert recursively on the left subtree.
            self._insert(data, node.left)
    elif data >= node.data:
        # Higher data belongs on the right side.
        if node.right is None:
            # We found an empty spot
            node.right = BST.Node(data)
        else:
            # Need to keep looking. Call _insert recursively on the right subtree.
            self._insert(data, node.right)
```

### Traversing
**Traversing** is used to display all the data in the tree. 
* In-order traversal will visit each node smallest to largest.
* Reverse traversal will visit each node largest to smallest.

> Smaller Problem: Traverse the left subtree of a node, using current node, then traverse the right subtree of the node.

> Base Case: If the subtree is empty, don't use recursion.

```Python
def __iter__(self):
"""
 Use an in-order traversal starting from 
 the root of the BST, when called.
"""
    yield from self._traverse_forward(self.root) # Start at the root

def _traverse_forward(self, node):
"""
Does a forward traversal (in-order traversal) through the 
BST. If the node that we are given (which is the current
subtree) exists, then we will keep traversing on the left
side (thus getting the smaller numbers first), then we will 
provide the data in the current node, and finally we will 
traverse on the right side (thus getting the larger numbers last).
This function is intended to be called the first time by 
the __iter__ function.
"""
if node is not None:
yield from self._traverse_forward(node.left)
yield node.data
yield from self._traverse_forward(node.right)
```

## Using BST in Python
Insert a value into the tree:
* insert(value)

Remove a value from the tree:
* remove(value)

Determine if a value is in the tree:
* contains(value)

Visit all object from smallest to largest:
* traverse_forward

Visit all objects from largest to smallest:
* traverse_reverse

Determine the height of a node. If the height of the tree is needed, the root node is provided:
* height(node)

Return the size of the BST:
* size()

Returns true if the root node is empty. This can also be done by checking the size for 0:
* empty()

## Sample Problems
Check to see if any of the nodes in the tree contains specific data.

```Python
def _contains(self, data, node):
    """
    This functions searches for a node that contains 'data'.
    # Create base case
    # Condition statement that return True IF data == node.data
    """
    # Return true if the node matches the data.
    if data == node.data:
        return True
    else:
        # If data is smaller than node, check left side.
        if data < node.data:
            # If no other nodes on left, go back and search again.
            if node.left is None:
                BST.Node(data)
            else:
                # continue searching left subtree.
                return self._contains(data, node.left)
        # If data is larger than node, check right side.
        elif data > node.data:
            # If no other node on right, go back and search again.
            if node.right is None:
                BST.Node(data)
            else: 
                # continue searching right subtree.
                return self._contains(data, node.right)

```

## Try it Yourself!
Use what you know about Python and what you have learned about BST's in this tutorial to create a BST and Node class. Use the code above to insert data into the tree, then write get_height() and _get_height() functions to get the height of the tree. Call the following functions to test your code:

```Python
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
```