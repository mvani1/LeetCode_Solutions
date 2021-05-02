class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        next_ = {"0": ["1", "9"], 
                 "1": ["2", "0"],
                 "2": ["3", "1"],
                 "3": ["4", "2"],
                 "4": ["5", "3"],
                 "5": ["6", "4"],
                 "6": ["7", "5"],
                 "7": ["8", "6"],
                 "8": ["9", "7"],
                 "9": ["0", "8"]
                }
        queue = deque([("0000", 0)])
        seen = set()
        seen.add("0000")
        set_deadends = set(deadends)
        while queue:
            curr_comb, steps = queue.popleft()
            
            if curr_comb in target:
                return steps
            
            if curr_comb in set_deadends:
                continue
            
            for i in range(len(curr_comb)):
                for digit in next_[curr_comb[i]]:
                    new_comb = curr_comb[:i] + digit + curr_comb[i + 1:]
                    if new_comb not in seen:
                        queue.append((new_comb, steps + 1))
                        seen.add(new_comb)
        return -1
                