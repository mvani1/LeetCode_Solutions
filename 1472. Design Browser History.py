class BrowserHistory:

    def __init__(self, homepage: str):
        self.visits = [homepage]
        self.pointer = 0
        
    def visit(self, url: str) -> None:
        # while(len(self.visits)-1!=self.pointer):
        #     self.visits.pop()
        self.visits = self.visits[0:self.pointer+1]
        self.visits.append(url)
        self.pointer +=1

    def back(self, steps: int) -> str:
        if (self.pointer-steps< 0):
            self.pointer=0
        else:
            self.pointer-=steps
        return self.visits[self.pointer]
        

    def forward(self, steps: int) -> str:
        if (self.pointer+steps < len(self.visits)):
            self.pointer+=steps
        else:
            self.pointer = len(self.visits)-1
        return self.visits[self.pointer]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)