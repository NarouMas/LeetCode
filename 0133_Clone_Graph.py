# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        mp = dict()
        if not node:
            return None
        if len(node.neighbors) == 0:
            clone = Node(node.val)
            return clone

        def dfs(cur):
            nonlocal mp
            neighbor = []
            clone = Node(cur.val)
            mp[cur] = clone
            for it in cur.neighbors:
                if it in mp:
                    neighbor.append(mp[it])
                else:
                    neighbor.append(dfs(it))
            clone.neighbors = neighbor
            return clone

        return dfs(node)