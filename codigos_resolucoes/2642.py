class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        
        self.graph = defaultdict(list)
        self.n = n
        for from_node, to_node, cost in edges:
            self.graph[from_node].append((cost, to_node))

    def addEdge(self, edge: List[int]) -> None:
       
        from_node, to_node, cost = edge
        self.graph[from_node].append((cost, to_node))

    def shortestPath(self, node1: int, node2: int) -> int:
        
        distances = [float('inf')] * self.n
        distances[node1] = 0
        heap = [(0, node1)]  # (current_distance, current_node)
        
        while heap:
            current_dist, current_node = heapq.heappop(heap)
            
            if current_node == node2:
                return current_dist
            
            for edge_cost, neighbor in self.graph[current_node]:
                new_dist = current_dist + edge_cost
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))
        
        return -1
