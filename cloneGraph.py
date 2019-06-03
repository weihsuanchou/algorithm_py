"""
# Definition for a Node.
"""

class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
        
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        dict = {}
        #take all the neighbors
        def clone(node):
            if node not in dict:
                copy = Node(node.val, None)
                dict[node] = copy #marked as visisted, to set a stop for recursion
                
                #call by reference, so it is fine to update copy's neighbor later than dictionary
                copy.neighbors = list(map( clone, node.neighbors ))
            return dict[node]
        
        # return node if node is None else go for running clone
        return node and clone(node)
        
        
        