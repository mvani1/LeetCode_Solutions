class BrowserHistory:
    def __init__(self, homepage: str):
        self.pages = [homepage]
        self.current_page = 0

    def visit(self, url: str) -> None:
        self.pages[self.current_page+1:] = [url]
        self.current_page = len(self.pages) - 1
        
    def back(self, steps: int) -> str:
        self.current_page = max(0, self.current_page-steps)
        return self.pages[self.current_page]

    def forward(self, steps: int) -> str:
        self.current_page = min(len(self.pages)-1, self.current_page+steps)
        return self.pages[self.current_page]