class Solution:
    '''
        We need to keep our positions in hash-table, so we can find loop_len. We do iteration by iteration and if we found a loop, we need to do (N - i) % loop_len more steps.

    Complexity: time and memory is O(64), because the loop size will be not more than 64.
    '''
    def next_step(self, cells):
        res = [0] * 8
        for i in range(1,7):
            res[i] = int(cells[i-1] == cells[i+1])
        return res
    
    def prisonAfterNDays(self, cells, N):
        found_dic = {}
        for i in range(N):
            cells_str = str(cells)
            if cells_str in found_dic:
                loop_len = i - found_dic[cells_str]
                return self.prisonAfterNDays(cells, (N - i) % loop_len)
            else:
                found_dic[cells_str] = i 
                cells = self.next_step(cells) 
                
        return cells