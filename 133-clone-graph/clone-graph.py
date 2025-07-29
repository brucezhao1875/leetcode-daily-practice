"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    '''
    想起springboot里边的那个beanfactory循环依赖的问题,如果没有factory的问题就这么简单。
    '''
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        if not node : 
            return None

        def dfs(node):
            if node in visited :
                return visited[node]
            
            clone = Node(node.val)
            visited[node] = clone
            for x in node.neighbors:
                clone.neighbors.append(dfs(x))
            
            return clone
        
        return dfs(node)

