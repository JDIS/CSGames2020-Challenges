import binarytree
import re

class Node:
    def __init__(self, val, leftVal, rightVal):
        super().__init__()
        self.val = val
        self.leftVal = leftVal
        self.rightVal = rightVal
        self.leftNode = None
        self.rightNode = None
    
    def try_insert_child(self, child):
        if child.val == self.leftVal:
            self.leftNode = child
            return True
        elif child.val == self.rightVal:
            self.rightNode = child
            return True
        elif self.leftNode is not None and self.leftNode.try_insert_child(child):
            return True
        elif self.rightNode is not None and self.rightNode.try_insert_child(child):
            return True
        else:
            return False
    
    def to_binary_tree(self):
        node = binarytree.Node(self.val)
        if self.leftNode is not None:
            node.left = self.leftNode.to_binary_tree()
        if self.rightNode is not None:
            node.right = self.rightNode.to_binary_tree()
        
        return node
            

nodes = []

filepath = 'input.txt'
with open(filepath) as fp:
    line = fp.readline()    
    while line:
        line = re.sub('[()\n]', '', line)
        node = list(map(int, line.split(',')))
        nodes.append(Node(node[0], node[1], node[2]))
        
        line = fp.readline()

tree = nodes[0]
nodes.remove(tree)

while len(nodes) > 0:
    to_remove = []
    for node in nodes:
        if tree.try_insert_child(node):
            to_remove.append(node)
    
    if len(to_remove) == 0:
        nodes.append(tree)
        tree = nodes[0]
        nodes.remove(tree)

    for node in to_remove:
        nodes.remove(node)

tree = tree.to_binary_tree()

# This function traverse the skewed binary tree and  
# stores its nodes pointers in vector nodes[] 
def storeBSTNodes(root,nodes): 
      
    # Base case 
    if not root: 
        return
      
    # Store nodes in Inorder (which is sorted  
    # order for BST)  
    storeBSTNodes(root.left,nodes) 
    nodes.append(root) 
    storeBSTNodes(root.right,nodes) 
  
# Recursive function to construct binary tree  
def buildTreeUtil(nodes,start,end): 
      
    # base case  
    if start>end: 
        return None
  
    # Get the middle element and make it root  
    mid=(start+end)//2
    node=nodes[mid] 
  
    # Using index in Inorder traversal, construct  
    # left and right subtress 
    node.left=buildTreeUtil(nodes,start,mid-1) 
    node.right=buildTreeUtil(nodes,mid+1,end) 
    return node 
  
# This functions converts an unbalanced BST to  
# a balanced BST 
def buildTree(root): 
    
    # Store nodes of given BST in sorted order  
    nodes=[] 
    storeBSTNodes(root,nodes) 
  
    # Constucts BST from nodes[]  
    n=len(nodes) 
    return buildTreeUtil(nodes,0,n-1) 
  
# Driver code 
if __name__=='__main__': 
    root = buildTree(tree)
    print("Preorder traversal of balanced BST is :") 
    print('FLAG{', ''.join(str(y) for y in map(lambda x: x.value, root.preorder)), '}', sep='')
