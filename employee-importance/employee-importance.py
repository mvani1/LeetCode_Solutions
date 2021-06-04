"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        adj = collections.defaultdict(list)
        for i in employees:
            adj[(i.id)].append(i.importance)
            adj[(i.id)].append(i.subordinates)
        
        def fs(ids):
            self.imp += adj[ids][0]
            # print(imp)
            for i in adj[ids][1]:
                # print(i)
                fs(i)
            # return imp
        self.imp = 0
        fs(id)
        return(self.imp)