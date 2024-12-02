import heapq

class Solution:
    def distances_djikstra(self, n: int, edges: list[list[int]], start):
        """
        Método do algoritmo de Djikstra para encontrar os menores caminhos a partir de um nó inicial
        """

        visited = set()
        distances = [float('inf') if i != start else 0 for i in range(n)]
        heap_distance = [(distances[start], start)]

        while heap_distance:
            actual_distance, actual_node= heapq.heappop(heap_distance)

            if actual_node in visited:
                continue

            visited.add(actual_node)

            # Verificação para arestas bidirecionais
            for node_origin, node_dest, weight in edges:
                if node_origin == actual_node:
                    neighbor_node, neighbor_weight = node_dest, weight 
                elif node_dest == actual_node:
                    neighbor_node, neighbor_weight = node_origin, weight
                else:
                    continue
            
                calc_distance = actual_distance + neighbor_weight

                if calc_distance < distances[neighbor_node]:
                    distances[neighbor_node] = calc_distance
                    heapq.heappush(heap_distance, (calc_distance, neighbor_node))

        return distances

    def findAnswer(self, n: int, edges: list[list[int]]) -> list[bool]:
        """
        Este método irá verificar se algum dos nós pertencentes ao grafo participa
        de pelo menos 1 dos menores caminhos de se chegar de 0 à n-1. O grafo entrada é não-direcionado.
        """
        
        distances_from_first = self.distances_djikstra(n, edges, 0)
        distances_from_last = self.distances_djikstra(n, edges, n-1)
        total_shortest_path = distances_from_first[n-1]

        result = []
        for node_origin, node_dest, weight in edges:
            if distances_from_first[node_origin] + weight + distances_from_last[node_dest] == total_shortest_path\
            or \
            distances_from_first[node_dest] + weight + distances_from_last[node_origin] == total_shortest_path:
                result.append(True)
            else:
                result.append(False)

        return result

# edges = [[2,0,1],[0,1,1],[0,3,4],[3,2,2]]
# vertices = 4

# solucao = Solution()

# print(solucao.findAnswer(vertices, edges))