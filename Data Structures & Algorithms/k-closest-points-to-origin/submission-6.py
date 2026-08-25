import math
import heapq

class Solution:
    def distance_from_origin(self, x, y):
        return math.sqrt(x*x + y*y)
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_points_pairs = []
        result = []
        for x, y in points:
            distance_points_pairs.append((self.distance_from_origin(x, y), (x, y)))
        heapq.heapify(distance_points_pairs)

        for i in range(k):
            pair = heapq.heappop(distance_points_pairs)
            result.append(pair[1])
        
        return result
        
        