from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        for u, v in prerequisites:
            adj[v].append(u)

        indegrees = [0 for i in range(numCourses)]
        for u in adj:
            for v in adj[u]:
                indegrees[v] += 1

        queue = deque([])
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)

        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            if adj.get(node):
                for v in adj[node]:
                    indegrees[v] -= 1
                    if indegrees[v] == 0:
                        queue.append(v)
            
        if len(order) < numCourses:
            return []
        
        return order