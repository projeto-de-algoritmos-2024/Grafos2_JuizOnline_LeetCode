class Solution:
    visited = set()
    
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        """
        Basicamente é uma DFS/BFS que buscará por componentes, se houver apenas um, 
        então é possível chegar em todos os quartos a partir do inicial (0)
        """

        self.visitRoom(0, rooms)

        return len(self.visited) == len(rooms) 

    # Função que irá viajar de quarto em quarto por DFS
    def visitRoom(self, roomNumber, rooms):
        for neighbor in rooms[roomNumber]:
            if neighbor not in self.visited:
                self.visited.add(neighbor)
                self.visitRoom(neighbor, rooms)


        


