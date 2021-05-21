class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        '''
        Time = O(n)
        Space = O(1)
        '''
        
        # north = 0, east = 1, south = 2, west = 3
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # Initial position is in the center
        x = y = 0
        # facing north
        idx = 0
        
        for i in instructions:
            # facing west, idx = 3, turn to the right to face north, idx = 0.
            if i == "L":
                idx = (idx + 3) % 4
            #. A more simple way is to notice that 1 turn to the 
            # left = 3 turns to the right: idx = (idx + 3) % 4.
            elif i == "R":
                idx = (idx + 1) % 4
            # If the current instruction is to move, we simply update the coordinates
            else:
                x += directions[idx][0]
                y += directions[idx][1]
        
        # after one cycle:
        # robot returns into initial position
        # or robot doesn't face north
        return (x == 0 and y == 0) or idx != 0