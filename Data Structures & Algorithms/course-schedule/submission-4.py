from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for u, v in prerequisites:
            if adj.get(v):
                adj[v].append(u)
            else:
                adj[v] = [u]

        indegrees = [0] * numCourses
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
                for nei in adj[node]:
                    indegrees[nei] -= 1
                    if indegrees[nei] == 0:
                        queue.append(nei)

        if len(order) < numCourses:
            return False
        return True

