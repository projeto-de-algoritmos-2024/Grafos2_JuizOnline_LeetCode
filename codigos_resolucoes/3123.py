import heapq

class Solution:
    def distances_djikstra(self, n: int, graph: list[list[set]], edges: list[list[int]], start: int):
        """
        Método do algoritmo de Djikstra para encontrar os menores caminhos a partir de um nó inicial
        """

        distances = [float('inf')] * n; distances[start] = 0
        heap_distance = [(distances[start], start)]

        while heap_distance:
            actual_distance, actual_node = heapq.heappop(heap_distance)

            # Essa condição evita lidar com o caminho mais longo da heap (performance)
            if distances[actual_node] == actual_distance:
                for neighbor_weight, neighbor_node in graph[actual_node]:
                
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
        
        # Cria o grafo com base na lista de arestas como lista de adjacências para facilitar a varredura no Djikstra
        graph_from_edges = [[] for _ in range(n)]
        for node_o, node_d, w in edges:
            graph_from_edges[node_o].append((w, node_d))
            graph_from_edges[node_d].append((w, node_o))

        distances_from_first = self.distances_djikstra(n, graph_from_edges, edges, 0)
        total_shortest_path = distances_from_first[n-1]
        
        # Condição que verifica se há um caminho de 0 a n-1
        if total_shortest_path == float('inf'):
            return [False] * len(edges)
        
        distances_from_last = self.distances_djikstra(n, graph_from_edges, edges, n-1)

        result = []
        for node_origin, node_dest, weight in edges:
            # Verifica se a aresta atual faz parte de um dos caminhos mais curtos, seja de ida ou de volta (bidirecional)
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