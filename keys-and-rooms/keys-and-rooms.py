class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set()
        n = len(rooms)
        adj = {}
        for room_num,next_keys in enumerate(rooms):
            adj[room_num] = next_keys
        
        def dfs(room):
            if room in seen:
                return
            seen.add(room)
            for next_room in adj[room]:
                if next_room not in seen:
                    dfs(next_room)
        
        dfs(0)
        return len(seen) == n