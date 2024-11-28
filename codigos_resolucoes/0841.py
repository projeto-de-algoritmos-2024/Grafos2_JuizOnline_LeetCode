class Solution:
    
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        """
        Basicamente é uma DFS/BFS que buscará por componentes, se houver apenas um, 
        então é possível chegar em todos os quartos a partir do inicial (0)
        """

        visited = set()
        self.visitRoom(0, rooms, visited)

        return len(visited) == len(rooms) 

    # Função que irá viajar de quarto em quarto por DFS
    def visitRoom(self, roomNumber, rooms, visited):
        visited.add(roomNumber)
        for neighbor in rooms[roomNumber]:
            if neighbor not in visited:
                self.visitRoom(neighbor, rooms, visited)
