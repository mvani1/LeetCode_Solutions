class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        dictt = collections.defaultdict(list)
        for i in range(len(pid)):
            dictt[ppid[i]].append(pid[i])
        self.ans=[]
        def traverse(curr,path):
            if not curr: return
            for i in dictt[curr]:
                self.ans.append(i)
                traverse(i,path)
        # if dictt.get(kill,None):
        self.ans.append(kill)
        traverse(kill,"")
        return(self.ans)