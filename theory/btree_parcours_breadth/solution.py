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

print(''.join(str(y) for y in tree.to_binary_tree().values))